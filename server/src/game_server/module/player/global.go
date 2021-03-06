/*
玩家相关全局变量和常量
*/
package player

import (
	"core/fail"
	"core/net"
	"core/time"
	"game_server/api/protocol/player_api"
	"game_server/config"
	. "game_server/config"
	"game_server/dat/player_dat"
	"game_server/mdb"
	"game_server/module"
	"game_server/module/rpc"
	"game_server/tencent"
	"game_server/tlog"
	"game_server/xdlog"
	"sync"
)

func init() {
	module.Player = PlayerMod{}
	module.PrepareStoreEvent.Regisiter(PerpareStoreHandler)
}

type PlayerMod struct {
}

var (
	// 用户昵称 => 用户ID
	g_NicknameIndex = make(map[string]int64)
	// 平台账号 => 用户ID
	g_UsernameIndex = make(map[string]int64)
	// 用户ID ＝> 平台账号 (在线表)
	g_OnlineIndex = make(map[int64]*net.Session)

	g_OnlineCount = make(map[int32]map[int64]bool)

	g_OnlineMutex sync.RWMutex
)

/* ###################

	玩家相关的公共接口

################### */

func GetPlayerIdByNickname(name string) (pid int64, ok bool) {
	pid, ok = g_NicknameIndex[name]
	return
}

func GetPlayerIdByUsername(name string) (pid int64, ok bool) {
	pid, ok = g_UsernameIndex[name]
	return
}

func SetPlayerOnline(cid int32, pid int64, session *net.Session) {
	g_OnlineMutex.Lock()
	defer g_OnlineMutex.Unlock()

	g_OnlineIndex[pid] = session
	if g_OnlineCount[cid] == nil {
		g_OnlineCount[cid] = make(map[int64]bool)
	}
	g_OnlineCount[cid][pid] = true
}

func SetPlayerOffline(cid int32, pid int64) {
	g_OnlineMutex.Lock()
	defer g_OnlineMutex.Unlock()

	delete(g_OnlineIndex, pid)
	if g_OnlineCount[cid] != nil {
		delete(g_OnlineCount[cid], pid)
	}
}

func SendReLogin(session *net.Session) func() {
	return func() {
		session.Send(&player_api.Relogin_Out{})
	}
}

// 会话保存前准备
func PerpareStoreHandler(session *net.Session) {
	state := module.State(session)

	//登出时设置打坐状态
	module.Meditation.LogoutStartMeditation(state)

	SetPlayerOffline(state.CId, state.PlayerId)
	module.Town.LeaveTown(session)

	//记录离线时间
	playerInfo := state.Database.Lookup.PlayerInfo(state.PlayerId)
	playerInfo.LastOfflineTime = time.GetNowTime()

	var onlineTime int64
	onlineTime = playerInfo.LastOfflineTime - playerInfo.LastLoginTime

	if playerInfo.LastLoginTime > 0 {
		playerInfo.TotalOnlineTime += onlineTime
	}
	state.Database.Update.PlayerInfo(playerInfo)
	// 更新离线时间到互动服
	rpc.RemoteUpdatePlayerOfflineTime(state.PlayerId, playerInfo.LastOfflineTime)

	user := state.Database.Lookup.Player(state.PlayerId).User
	level := int32(module.Role.GetMainRole(state.Database).Level)

	rpc.RemoteTssUserLogout(user, int(config.ServerCfg.XGSdk.PlatformType))

	role_vip := module.VIP.VIPInfo(state.Database)

	state.Database.AddTLog(tlog.NewPlayerLogout(user, int32(onlineTime), level, 0, state.TlogClientVersion, "" /*SystemSoftware*/, state.TlogSystemHardware,
		state.TlogTelecomOper, state.TlogNetwork, 0, 0, 0.0, 0, "" /*CpuHardware*/, 0, "" /*GLRender*/, "" /*GLVersion*/, "" /*DeviceId*/, int32(role_vip.Level)))

	xdlog.PlayerLoginLog(state.Database, state.Ip, xdlog.LOGOUT)
	// 只有玩家在线时长至少达到60s才将总战力上报(避免闪断重连情况频繁上传战力)
	if onlineTime >= 60 {
		playerFightNum := state.Database.Lookup.PlayerFightNum(state.PlayerId)
		if ServerCfg.EnableTlog {
			tencent.SendFightNumToTencent(state.MoneyState, playerFightNum.FightNum)
		}
		xdlog.FightNumLog(state.Database, int64(playerFightNum.FightNum))

	}
}

func (mod PlayerMod) OnlinePlayerNum() map[int32]int64 {
	g_OnlineMutex.RLock()
	defer g_OnlineMutex.RUnlock()

	onlineCount := make(map[int32]int64)
	for k, v := range g_OnlineCount {
		onlineCount[k] = int64(len(v))
	}

	return onlineCount
}

/*
   提供模块间接口
*/
func (mod PlayerMod) GetPlayerOnline(pid int64) (session *net.Session, ok bool) {
	g_OnlineMutex.RLock()
	defer g_OnlineMutex.RUnlock()

	session, ok = g_OnlineIndex[pid]
	return
}

// 刷新玩家功能权值
func (mod PlayerMod) RefreshPlayerFuncKey(db *mdb.Database, newFuncLock int16) {
	setFuncKey(db, newFuncLock)
}

//获取新等级的功能
func (mod PlayerMod) RefreshPlayerLevelFuncKey(db *mdb.Database, level int16) {
	setLevelFuncKey(db, level)
}

//获取新等级的功能（废弃）
//func (mod PlayerMod) OpenLevelFunc(db *mdb.Database, level int16) {
//	functions := player_dat.GetLevelFuncs(level)
//	for _, function := range functions {
//		openLevelFunc(db, function.Id)
//	}
//}

//获取账号信息
func (mod PlayerMod) GetPlayer(db *mdb.Database) *mdb.Player {
	return db.Lookup.Player(db.PlayerId())
}

func (mod PlayerMod) GetPlayerByUsername(name string) (pid int64, ok bool) {
	pid, ok = GetPlayerIdByUsername(name)
	return
}

func (mod PlayerMod) GetPlayerByNick(nick string) (pid int64, ok bool) {
	pid, ok = GetPlayerIdByNickname(nick)
	return
}

//对全体在线玩家做一件事情
func (mod PlayerMod) Fetch(cb func(session *net.Session)) {
	g_OnlineMutex.RLock()
	defer g_OnlineMutex.RUnlock()
	for _, session := range g_OnlineIndex {
		cb(session)
	}
}

//检查玩家是否开启一项功能
func (mod PlayerMod) MustOpenFunc(db *mdb.Database, id int32) {
	fail.When(!module.Player.IsOpenFunc(db, id), "功能尚未开启")
}

//检查玩家是否已经初始化了一项功能
func (mod PlayerMod) IsFuncInited(db *mdb.Database, id int32) bool {
	function := player_dat.GetFuncById(id)
	playerFuncKey := db.Lookup.PlayerFuncKey(db.PlayerId())
	return (playerFuncKey.UniqueKey & function.UniqueKey) != 0
}

//检查玩家是否开启一项功能
func (mod PlayerMod) IsOpenFunc(db *mdb.Database, id int32) bool {
	function := player_dat.GetFuncById(id)
	if function.Type == player_dat.FUNC_OPEN_TYPE_BY_LOCK {
		playerFuncKey := db.Lookup.PlayerFuncKey(db.PlayerId())
		return playerFuncKey.Key >= function.Lock
	}
	if function.Type == player_dat.FUNC_OPEN_TYPE_BY_LEVEL {
		mainRoleLevel := module.Role.GetMainRole(db).Level
		return mainRoleLevel >= function.Level
	}
	panic("undefin function open type")
	return false
}

//增加声望
func (mod PlayerMod) AddFame(db *mdb.Database, val int32) {
	addFame(db, val)
}

func (mod PlayerMod) ActiveMonthCard(db *mdb.Database) bool {
	return activeMonthcard(db)
}
