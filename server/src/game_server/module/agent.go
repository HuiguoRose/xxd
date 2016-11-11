package module

import (
	"core/net"
	"game_server/api/protocol/arena_api"
	"game_server/api/protocol/channel_api"
	"game_server/api/protocol/notify_api"
	"game_server/api/protocol/role_api"
	"game_server/battle"
	"game_server/dat/channel_dat"
	"game_server/dat/daily_sign_in_dat"
	"game_server/dat/ghost_dat"
	"game_server/dat/item_dat"
	"game_server/dat/mail_dat"
	"game_server/mdb"
	"time"
)

var (
	Player       iPlayerModule
	PlayerRPC    iPlayerRPCModule
	Notify       iNotifyModule
	Mission      iMissionModule
	Town         iTownModule
	Team         iTeamModule
	Role         iRoleModule
	Skill        iSkillModule
	Battle       iBattleModule
	Item         iItemModule
	Physical     iPhysicalModule
	API          iAPIModule
	Ghost        iGhostModule
	Mail         iMail
	MailRPC      iMailRPC
	Heart        iHeart
	SwordSoul    iSwordSoulModule
	Quest        iQuest
	Friend       iFriend
	DrivingSword iDrivingSwordModule
	//Tower         iTowerLevel //废弃
	MultiLevel      iMultiLevel
	BattlePet       iBattlePet
	Arena           iArena
	ArenaRPC        iArenaRPC
	VIP             iVIP
	Draw            iDraw
	Event           iEvent
	Rainbow         iRainbow
	DailySignIn     iDailySignIn
	Fashion         iFashion
	PushNotify      iPushNotify
	Meditation      iMeditation
	PetVirtualEnv   iPetVirtualEnv
	Totem           iTotem
	Chan            iChan
	CliqueRPC       iCliqueRPC
	CliqueQuestRPC  iCliqueQuestRPC
	CliqueEscortRPC iCliqueEscortRPC
	ChatRPC         iChatRPC
)

type Awarder interface {
	Coins() int32
	Ingot() int32
	Item() map[int16]int16
	Exp() int32
}

type iAPIModule interface {
	// 广播消息
	Broadcast(sessions net.SessionList, response net.Response)
}

type iPlayerModule interface {
	// 从互动服务器退出
	LogoutFromGlobal(cid int32, playerId int64, session *net.Session)
	// 退出跨服
	LogoutFromCross(playerId int64, session *net.Session)
	// 获取在线玩家
	GetPlayerOnline(pid int64) (session *net.Session, ok bool)

	//检查货币是否足够,mtype:COINS,INGOT
	CheckMoney(state *SessionState, num int64, mtype int) bool
	// 查询元宝数
	GetIngot(db *mdb.Database, moneyState *MoneyState) int64
	//增加货币,mtype:COINS(0),INGOT(1)
	IncMoney(db *mdb.Database, moneyState *MoneyState, num int64, mtype int, moneyFlowReason, xdEventType int32, xdEventParam string)
	//减少货币,mtype:COINS(0),INGOT(1)
	DecMoney(db *mdb.Database, moneyState *MoneyState, num int64, mtype int, moneyFlowReason, xdEventType int32)

	//增加魂侍碎片，ftype:3
	IncSwordSoulFragment(db *mdb.Database, num int64, ftype int, moneyFlowReason, xdEventType int32)
	//扣除魂侍碎片，ftype:3
	DecSwordSoulFragment(db *mdb.Database, num int64, ftype int, moneyFlowReason, xdEventType int32)

	// 刷新玩家功能开放权值
	RefreshPlayerFuncKey(db *mdb.Database, newFuncLock int16)
	// 根据用户名返回玩家pid
	GetPlayerByUsername(name string) (pid int64, ok bool)
	// 根据玩家昵称返回pid
	GetPlayerByNick(nick string) (pid int64, ok bool)
	// 检查功能是否开放
	IsOpenFunc(db *mdb.Database, funcId int32) bool
	// 检查功能是否已经初始化
	IsFuncInited(db *mdb.Database, funcId int32) bool
	// 对在线玩家做批量操作
	Fetch(func(session *net.Session))
	//根据pid查询账号信息
	GetPlayer(db *mdb.Database) *mdb.Player
	//开启新等级功能
	RefreshPlayerLevelFuncKey(db *mdb.Database, level int16)
	//检查是否拥有一项权限
	MustOpenFunc(db *mdb.Database, funcId int32)
	//获取游戏服务器在线人数
	OnlinePlayerNum() map[int32]int64
	//检查玩家是否为qq会员
	QQVipStatus(state *SessionState) int16
	//增加声望
	AddFame(db *mdb.Database, val int32)
	ActiveMonthCard(db *mdb.Database) bool

	//排行榜
	AddUpdateFightNum(*mdb.Database, int32)
	AddUpdateLevel(*mdb.Database, int16, int64)
	AddUpdateMainRoleFightNum(*mdb.Database, int32)
	ForceUpdateLevel()
	ForceUpdateFightNum()
	AddUpdateInGot(db *mdb.Database, timestamp int64)
}

type iPlayerRPCModule interface {
	LoadGlobal()
}

type iTownModule interface {
	LeaveTown(session *net.Session)
	SetTownLock(state *SessionState, newLock int32)
}

type iTeamModule interface {
	IncRelationship(db *mdb.Database, value int32)
	GetFormPosArray(db *mdb.Database) (posArray [9]*int8)
	IsRoleInForm(db *mdb.Database, roleId int8) bool
	DownFormRole(db *mdb.Database, roleId int8)
}

type iArenaRPC interface {
	SendTopRank(session *net.Session)
	GetAwardBox(session *net.Session, num int8)
	GetPlayerRank(pid int64) int32
	AddPlayerRank(db *mdb.Database, pid int64) int32
	UpdatePlayerRank(db *mdb.Database, pid int64, rank int32)
	GetPlayerRankWithRank(db *mdb.Database, rank int32) []arena_api.Enter_Out_Ranks
}

type iArena interface {
	OpenFunc(db *mdb.Database)
	BattleDoWin(session *net.Session)
	BattleDoLose(session *net.Session)
	GetPlayerArenaRank(db *mdb.Database, callback func(int32))
	RefreshAwardBox(playerRank *mdb.PlayerArenaRank, rank int32) bool
	InitPlayerArenaRank(db *mdb.Database, pid int64)
}

type iQuest interface {
	// 刷新任务
	RefreshQuest(state *SessionState, action int, xdEventType int32)
	// 刷新每日任务
	RefreshDailyQuest(state *SessionState, class int16)
	// 更新玩家日常任务（登陆、升级、每日凌晨）
	UpdatePlayerDailyQuest(db *mdb.Database, roleLevel int16)
	// 启动日常任务定时器
	StartDailyQuestTimer(state *SessionState)
	//伙伴招募任务进度刷新：连续登陆
	RefreshLoginExtendQuest(state *SessionState, continueLogin bool)
	//任务刷新：打败怪物
	RefreshQuestForBeatEnemyGroup(db *mdb.Database, enemyId int32)
	//任务刷新：通关关卡
	RefreshQuestForPassMissionLevel(db *mdb.Database, missionLevelId, xdEventType int32) map[int16]int16
	//任务刷新：区域评星改变
	RefreshQuestForMissionStarChange(db *mdb.Database, missionId int16, incStar int16)
	//任务刷新：获得新伙伴
	RefreshQuestForNewBuddy(db *mdb.Database, roleId int8)
	//任务刷新：主线任务变化
	RefreshQuestOnMainQuestChange(db *mdb.Database, mainQuestId int16)
	//任务刷新：等级变化
	RefreshQuestOnLevelUp(db *mdb.Database, oldLv, newLv int16)
	//刷新伙伴招募任务
	RefreshExtendQuest(db *mdb.Database, mainQuestId int16)
	//领取支线任务
	TakeAdditionQuest4Debug(session *net.Session, questId int32)
}

type iBattlePet interface {
	// 功能开启
	OpenFunc(db *mdb.Database)
	//根据格子ID获取当前宠物信息
	GetBattlePetByGrid(db *mdb.Database, grid int8) *mdb.PlayerBattlePet
	//获取上阵灵宠信息
	GetAvailableBattlePet(db *mdb.Database) map[int8]int32
	//增加灵宠 petid 是灵宠表的主键
	AddPet(db *mdb.Database, petid int32, itemFlowReason, xdEventType int32)
	//根据格子ID查找格子信息
	GetPlayerGridById(db *mdb.Database, gridId int8) *mdb.PlayerBattlePetGrid
	//增加灵宠 petid 是灵宠表的主键
	AddPetWihoutNotify(db *mdb.Database, petid int32, itemFlowReason, xdEventType int32)
}

type iMultiLevel interface {
	// 开启多人关卡
	OpenFunc(db *mdb.Database)
	// 开始多人关卡战斗
	StartBattle(state *SessionState, levelId int32)
	// 多人关卡奖励
	AwardWinner(db *mdb.Database, buddyRoleId int8, levelId int16, online bool)
	//获取指定房间的某一玩家是否合适接受通知
	IsMultiInvitePlayerSuitable(roomId int64, inviterId int64) bool
	LeaveMultiLevel(session *net.Session)
}

type iMissionModule interface {
	// 开始关卡战斗
	StartLevelBattle(battleType int8, enemy_id int32, session *net.Session)
	// 关卡固定奖励(铜钱，经验，钥匙等资源,不是开宝箱)
	AwardLevel(state *SessionState, xdEventType int32)
	// 获取关卡记录
	GetMissionLevelRecord(db *mdb.Database, levelId int32) *mdb.PlayerMissionLevelRecord
	// 离开区域关卡
	LeaveMissionLevel(state *SessionState)
	// 检查是否需要重构区域关卡，需要会主动向客户端发送mission::rebuild通知
	CheckIsNeedRebuildMissionLevel(session *net.Session)
	SetMissionLevelLock(state *SessionState, newLock int32, playerLevel *mdb.PlayerMissionLevel, isNotify bool)
	// 关卡开启
	OpenFuncForExtendLevel(db *mdb.Database, funcId int32)
	// 服务端直接奖励（扫荡，纵云梯用到）
	ServerDirectAward(state *SessionState, playerLevel *mdb.PlayerMissionLevel, levelId int32, boxOpenCount int8, xdEventType int32)
	// 奖励成功捕捉的灵宠
	AwardCatchedBattlePet(state *SessionState, xdEventType int32)
	// 灵宠捕捉通知
	NotifyCatchBattlePet(session *net.Session, petId int32)
	// 获取难度关卡记录
	GetHardLevelRecordById(db *mdb.Database, levelId int32) (levelRecord *mdb.PlayerHardLevelRecord)
	// 难度关卡失败处理
	HardLevelLose(state *SessionState, defendSide *battle.SideInfo)
	// 统计当前区域评分
	CountMissoinStar(db *mdb.Database, missionId int16) (star int16)
	//开始难命锁宝箱战斗
	StartFateBoxLevelBattle(session *net.Session, enemy_id int32)
}

type iRoleModule interface {
	// 获取主角数据
	GetMainRole(db *mdb.Database) *mdb.PlayerRole
	// 获取伙伴数据
	GetBuddyRole(db *mdb.Database, roleId int8) *mdb.PlayerRole
	// 获取在队伍中的伙伴
	GetBuddyRoleInTeam(db *mdb.Database, roleId int8) *mdb.PlayerRole
	// 添加伙伴
	AddBuddyRole(state *SessionState, roleId int8, level int16) int8
	// 给角色加经验
	AddRoleExp(db *mdb.Database, roleId int8, addExp int64, mainRoleId int8, playerFlowReason int32)
	// 给所有上阵角色加经验(包括主角)
	AddFormRoleExp(state *SessionState, addExp int64, playerFlowReason int32)
	// 获取其他玩家信息
	GetOtherPlayerInfo(playerId int64, db *mdb.Database, playerInfo *role_api.PlayerInfo)
	//获取上阵角色ID
	GetFormRoleId(state *SessionState) (roleIds []int8)
	// 返回新的level, exp, 返回参数为 level int16, exp int64
	GetNewLevelAndExp(level int16, exp int64) (int16, int64)
	GetFormFightNum(db *mdb.Database) (fightNum int32)
	//解除协力关系
	BreakBuddyCoop(db *mdb.Database, roleId int8)
}

type iNotifyModule interface {
	// 通知玩家区域钥匙变更
	SendPlayerKeyChanged(session *net.Session, key int32, max_order int8)
	// 通知玩家区域关卡权值变更
	SendMissionLevelLockChanged(session *net.Session, max_lock int32, award_lock int32)
	// 通知角色经验改变
	SendRoleExpChanged(session *net.Session, roleId int8, addExp int64, exp int64, level int16)
	// 通知玩家体力更变
	SendPhysicalChange(session *net.Session, value int16)
	// 通知玩家货币更新
	SendMoneyChange(session *net.Session, moneytype int8, value int64)
	// 通知玩家绝招增加
	SendSkillAdd(session *net.Session, roleId int8, skillId int16)
	// 通知玩家物品变动
	SendItemChange(session *net.Session, items *notify_api.ItemChange_Out)
	// 通知玩家角色上的状态变化（通常是关卡内使用道具影响buff、生命值）
	RoleBattleStatusChange(session *net.Session)
	// 新邮件
	NewMail(session *net.Session)
	// 通知爱心变动
	SendHeartChange(session *net.Session, value int16)
	// 任务状态变更
	SendQuestChange(session *net.Session, questId int16, state int8)
	// 城镇权值变更
	SendTownLockChange(session *net.Session, lock int32)
	// 功能权值改变
	SendFuncKeyChange(session *net.Session, funcKey int16)
	// 通知重建装备重铸
	SendItemRecastStateRebuild(session *net.Session)
	//VIP等级变更
	VIPLevelChange(session *net.Session, level int16)
	// 添加新伙伴
	SendNewBuddy(session *net.Session, roleId int8, level int16)
	// 通知难度关卡功能权值变化
	SendHardLevelLockChange(session *net.Session, lock int32)
	// 通知剑心拔剑次数变更
	SendSwordSoulDrawNumChange(session *net.Session, num int16, cdTime int64)
	//通知获得新魂侍
	SendHaveNewGhost(session *net.Session, ghostId int64)
	//通知下次爱心恢复时间
	SendHeartRecoverTime(session *net.Session, timestamp int64)
	//通知下次体力恢复时间
	SendPhysicalRecoverTime(session *net.Session, timestamp int64)
	//通知战场有新上阵怪物
	//SendBattleCallEnemys(session *net.Session, enemys []notify_api.SendBattleCallEnemys_Out_CallInfo)
	//发送时装变化通知
	SendFashionChange(session *net.Session, playerFashion *mdb.PlayerFashion)
}

type iSkillModule interface {
	// 初始化玩家伙伴的技能
	InitRoleSkill(state *SessionState, roleId int8)
	// 增加绝招
	UpdateSkill(db *mdb.Database, roleId int8, friendshipLevel, fameLevel, level int16)
}

type iBattleModule interface {
	// 关卡战场
	NewBattleForLevel(session *net.Session, battleType int8, enemyId int32, notAward bool) IBattle
	// 互动战场
	NewBattleRoom(battleType int, atkSide, defSide *battle.SideInfo, playerChannel *net.Channel, onBattleRoom IBattleRoom, roundTime time.Duration)
	NewBattleForPVE(session *net.Session, battleType int, attackerSide, defendSide *battle.SideInfo, forbidOP, notAward bool) IBattle
	//彩虹关卡战场
	NewBattleForRainbowLevel(session *net.Session, enemyId int32) IBattle
	//灵宠幻境
	NewBattleForPetVirtualEnv(session *net.Session, missionLvId int32) IBattle
	//仙山探险
	NewBattleForDriving(session *net.Session, missionLvId int32) IBattle
	//仙山拜访
	NewBattleForVisiting(session *net.Session, attackSide, defendSide *battle.SideInfo) IBattle
	//镖船战斗
	// NewBattleForEscortBoat(session *net.Session, battleType int, attackerSide, defendSide *battle.SideInfo, boatId int64) IBattle
	//劫镖战斗
	NewBattleForHiJackBoat(session *net.Session, battleType int, attackerSide, defendSide *battle.SideInfo, boatId int64) IBattle
	//夺镖战斗
	NewBattleForRecoverBoat(session *net.Session, battleType int, attackerSide, defendSide *battle.SideInfo, boatId int64) IBattle
}

type iItemModule interface {
	//添加物品
	AddItem(db *mdb.Database, itemId int16, num int16, itemFlowReason, xdEventType int32, xdEventParam string)
	//通过物品ID删除物品
	DelItemByItemId(db *mdb.Database, itemId int16, num int16, itemFlowReason, xdEventType int32)
	//检查物品数量
	CheckItemNum(state *SessionState, itemId int16, num int16) bool
	//返回物品数量
	GetItemNum(db *mdb.Database, itemId int16) int16
	//初始化角色装备
	InitRoleEquipment(state *SessionState, roleId int8)
	//主动发送物品信息
	SendAllItems(session *net.Session)
	//记录物品消费流水
	ItemMoneyFlow(db *mdb.Database, item *item_dat.Item, num, Price, iMoneyType int32)
	//批量增加物品 items itemId -> num
	BatchAddItem(db *mdb.Database, items map[int16]int16, itemFLowReason, xdEventType int32)
	//统计物品数量
	CountItemNumByType(db *mdb.Database, itemType int32) map[int16]int32
	//奖励同意接口
	Award(state *SessionState, awarder Awarder, itemFlowReason, moneyFlowReason, expFlowReason, xdEventType int32)
	//聚宝盆开启次数
	CornucopiaCount(db *mdb.Database) int16
}

type iPhysicalModule interface {
	// 登陆时更新体力
	LoginUpdatePhysical(state *SessionState, playerPhysical *mdb.PlayerPhysical)
	// 购买体力
	BuyPhysical(session *net.Session) (int16, bool)
	// 扣除体力
	Decrease(db *mdb.Database, decVal int16, reason int32) bool
	// 增加体力
	AwardIncrease(state *SessionState, val int16, pfrReason int32)
	// 如果体力大于等于检查值，返回true
	CheckGE(state *SessionState, val int16) bool
}

type iGhostModule interface {
	// 魂侍功能
	OpenFuncForGhost(db *mdb.Database)
	// 角色魂侍装备表初始化
	InitRoleGhostEquipment(db *mdb.Database, roleId int8)
	// 添加魂侍
	AddGhost(state *SessionState, ghostId int16, itemFlowReason, xdEventType int32)
	// 获得魂侍加成属性
	GetGhostAddData(playerGhost *mdb.PlayerGhost) (ghostAddData *ghost_dat.GhostAddData)
	//设置魂侍等级
	SetLevel(db *mdb.Database, playerGhostId int64, ghostLevel int16)
}

type iMail interface {
	// 发邮件,用户自己产生的邮件
	SendMail(db *mdb.Database, mail mail_dat.Mailer)
}

type iMailRPC interface {
	//如果玩家因为不在线导致有全局邮件没有领取那么就在这里发送（仅在互动服被调用）
	SendGlobaldMail(db *mdb.Database, pid int64)
	AddGlobalMail(db *mdb.Database, title string, content string, attachments []*mail_dat.Attachment, sendTime int64, expireTime int64, priority int8, minLevel, minVIPLevel, maxLevel, maxVIPLevel int16)
	//帮派发工资
	SendSalaryMail(pid int64, mail mail_dat.Mailer)
}

type iHeart interface {
	//登陆更新爱心
	LoginUpdateHeartNum(state *SessionState, playerHeart *mdb.PlayerHeart)
	//增加爱心
	IncHeart(state *SessionState, val int16)
	//减少爱心
	DecHeart(db *mdb.Database, val int16)
	//从好友处获得爱心
	IncHeartFromFriend(state *SessionState, val int16)
	//获取当前从好友出获取的爱心数量
	GetHeartDailyNum(state *SessionState) int32
}

type iSwordSoulModule interface {
	// 剑心功能
	OpenFuncForSwordSoul(db *mdb.Database)
	// 初始化角色剑心装备
	InitRoleSwordSoulEquipment(state *SessionState, roleId int8)
	// 增加剑心
	AddSwordSoul(state *SessionState, swordSoulId int16, itemReason int32)
	//登录时通知拔剑次数满
	SendSwordSoulWhenMaxDrawNum(session *net.Session)
	//设置剑心等级
	SetSwordSoulLevel(db *mdb.Database, roleid int8, swordpos int8, swordlevel int8)
}

type iFriend interface {
	//通过用户名添加好友
	ListenByName(state *SessionState, name string)
	//通知玩家离线消息
	SendOfflineMessages(session *net.Session)
	// 获取多人关卡在线好友
	GetMultiLevelOnlineFriends(db *mdb.Database) net.Response
	SendHeart(db *mdb.Database, friendPid int64)
	GetSendHeartRecord(db *mdb.Database, friendPid int64) *mdb.PlayerSendHeartRecord
}

//废弃
type iTowerLevel interface {
	// 功能开放
	OpenFunc(db *mdb.Database)
	// 通天塔战斗
	StartTownBattle(session *net.Session, battleId int32)

	BattleWin(state *SessionState)
	BattleLose(state *SessionState)
}

type iVIP interface {
	//更新元宝数量以及VIP等级
	UpdateIngot(db *mdb.Database, count int64)
	//获取玩家VIP信息
	VIPInfo(db *mdb.Database) *mdb.PlayerVip
	//获取VIP特权次数
	PrivilegeTimes(state *SessionState, privilege int16) int16
	//VIP特权检查
	CheckPrivilege(state *SessionState, privilege int16)
	//VIP是否拥有指定VIP特权
	HavePrivileve(state *SessionState, privilege int16) bool
	//是VIP
	IsVIP(db *mdb.Database) bool
	//获取VIP特权次数
	GetPrivilegeTimesByDB(db *mdb.Database, privilege int16) int16
	//增加VIP经验
	AddVipExp(db *mdb.Database, presentExp int32)
}

type iDraw interface {
	OpenFuncForChestDraw(db *mdb.Database)
	OpenFuncForFateBox(db *mdb.Database)
}

type iEvent interface {
	LevelUp(db *mdb.Database, level, newLevel int16)
	//登录时更新玩家登录次数
	UpdatePlayerLoginAwardInfo(db *mdb.Database)
	//活跃度活动
	UpdateEventActivityStatus(session *net.Session, decreVal int16)
	//获取json文件版本号
	GetVersion() int32
	//获取月卡赠送元宝数
	GetMonthCardPresentIngot() int64
	//累计消耗元宝和累计充值元宝记录
	UpdateEventsIngot(db *mdb.Database, val int64, isIn bool)
	//获取累计消耗或者累计充值的元宝
	GetEventsIngot(db *mdb.Database, isIn bool) int64
	//冲值时刷新首冲奖励表
	UpdateFirstRecharge(db *mdb.Database)
	//json十连抽活动
	UpdateJsonEventTenDraw(session *net.Session)
	//json累计充值活动
	UpdateJsonEventTotalRecharge(db *mdb.Database, val int32)
	//json累计消费活动
	UpdateJsonEventTotalConsume(db *mdb.Database, val int32)
	//json 单条消费
	UpdateJsonEventSingleConsume(db *mdb.Database, val int32)
	//json冲值时刷新首冲奖励表
	UpdateJsonFirstRecharge(db *mdb.Database)
	//比武场排名
	UpdateJsonEventArenaRank(db *mdb.Database, rank int32)
	//新年红包活动更新
	ChangeNewYearConsumeStatus(db *mdb.Database, ingot int32)
	//QQ会员特权礼包发放检查
	CheckQQVIPGift(db *mdb.Database, status int16)
}

type iRainbow interface {
	//为玩家初始化彩虹关卡所需的数据
	OpenFunc(db *mdb.Database)
	StartRainbowLevel(session *net.Session, enemy_id int32)
	BattleWin(state *SessionState, xdEventType int32)
	BattleLose(state *SessionState)
}

type iDailySignIn interface {
	GetAwardForToday(db *mdb.Database) *daily_sign_in_dat.DailySignInAward
	SignedToday(db *mdb.Database) bool
	AwardByMail(db *mdb.Database, awardConfig *daily_sign_in_dat.DailySignInAward)
}

type iFashion interface {
	//增加一件时装
	AddFashion(db *mdb.Database, fashionId int16, validHours int64) *mdb.PlayerFashion
	//登录时删除过期时装
	LoginUpdateFashion(db *mdb.Database)
	//时装属性是否生效
	FashionEnable(db *mdb.Database) bool
}

type iPushNotify interface {
	EnabledPushNotify(db *mdb.Database, notificationId int32) bool
	SendNotification(pid int64, notificationId int32)
}

type iMeditation interface {
	//登录时更新打坐状态（离线未满10分钟）
	LoginUpdateMeditationState(session *net.Session)
	//在城镇中离线设置离线打坐状态
	LogoutStartMeditation(state *SessionState)
	//是否在打坐状态
	InMeditationState(db *mdb.Database) bool
	//初始化打坐功能
	OpenFunc(db *mdb.Database)
}

type iPetVirtualEnv interface {
	//灵宠幻境战斗胜利
	BattleWin(*net.Session, int32)
	//开启战斗
	StartPetVirtualEnvLevel(*net.Session, int32)
	//灵宠幻境战败
	BattleLose(*net.Session, int32)
	//开启功能
	OpenFuncForPetVirtualEnv(db *mdb.Database)
	//动态增加怪物组
	WarnupNextEnemyGroup(state *SessionState, battleState *battle.BattleState) (fighters []*battle.Fighter)
}

type iTotem interface {
	//增加一个阵印
	AddTotem(db *mdb.Database, totemId int16)
	//开启功能
	OpenFuncForTotem(db *mdb.Database)
}

type iChan interface {
	//模版消息
	AddWorldTplMessage(pid int64, nick []byte, msgType int8, msgTpl channel_dat.MessageTpl)
}

type iDrivingSwordModule interface {
	//开启功能
	OpenFunc(*mdb.Database)
	//增加行动点
	IncActionPoint(*mdb.Database, int16)
	//重置云层数据
	ResetCloudData(*SessionState, int16)
	//云层自动开图
	PunchCloudData(*SessionState)
	//仙山探险战斗胜利
	BattleWin(*net.Session, int32)
	//仙山探险战败
	BattleLose(*net.Session)
	//开启战斗
	StartExploreLevel(session *net.Session)
	//动态增加怪物组
	WarnupNextEnemyGroup(state *SessionState, battleState *battle.BattleState) (fighters []*battle.Fighter)
	//仙山拜访奖励
	VisitingAward(session *net.Session, xdEventType int32)
	////判断角色是否处于驻守状态
	//IsRoleInGarrison(db *mdb.Database, roleId int8) bool
	////取消驻守
	//EndGarrisonByRole(db *mdb.Database, roleId int8)
}

type CliqueCountInfo struct {
	CliqueCount map[int64]int16
}

type iCliqueRPC interface {
	Broadcast(cliqueId int64, response net.Response)
	LeaveCliqueChannel(cliqueId int64, session *net.Session)
	GetLatestMessages(cliqueId int64) []channel_api.CliqueMessage
	//AddCliqueChat(cliqueId int64, msg channel_api.ChatMessage)
	AddCliqueChat(cliqueId int64, pid int64, nick []byte, msgTpl channel_dat.MessageTpl)
	AddCliqueNews(cliqueId int64, msgTpl channel_dat.MessageTpl)
	BroadcastClubhouse(cliqueId int64, response net.Response)
	LoginUpdateCliqueInfo(session *net.Session)
	Logout(session *net.Session)
	GetMemberNum(cliqueId int64) int16
	//增加贡献(暂时不用)
	//AddCliqueContrib(db *mdb.Database, money int64)
	//扣除贡献(暂时不用)
	//DelCliqueContrib(db *mdb.Database, money int64)
	//lookup global_clique表，并在周一清空
	CliqueInfoLookUp(db *mdb.Database, cliqueId int64) *mdb.GlobalClique
	CliqueInfoListPid(cliuqeid int64) []int64
	//增加贡献
	AddPlayerCliqueContrib(db *mdb.Database, contrib int64)
	//扣除贡献
	DecPlayerCliqueContrib(db *mdb.Database, contrib int64) bool
	//检查是否是帮派成员
	IsCliqueMember(cliqueId, pid int64) bool
	//获取帮派名字
	GetCliqueNameById(cliqueId int64) string
}
type iCliqueQuestRPC interface {
	UpDatePlayerCliqueDailyQuest(db *mdb.Database, class int16)
	AddCliqueBuildingQuest(cliqueInfo *mdb.GlobalClique, db *mdb.Database, pid int64)
	CleanCliqueBuildingQuest(db *mdb.Database, pid int64)
}

type iCliqueEscortRPC interface {
	//夺回胜利
	RecoverBattleWin(db *mdb.Database, fighterPid, boatId int64)
	//夺回胜利
	RecoverBattleLose(db *mdb.Database, fighterPid, boatId int64)
	//劫持胜利
	HijackBattleWin(db *mdb.Database, fighterPid, boatId int64)
	//登陆时候检查 劫持完成 或者 护送完成 通知
	LoginEscortNotify(session *net.Session)
	//增加镖船动态
	NewBoatMessage(db *mdb.Database, msg channel_dat.MessageTpl)
	//加入帮派时把镖船迁移到新帮派
	MigrateBoatToNewClique(db *mdb.Database, newCliqueId int64)
	//运镖测试负责接口
	ForceEscort(db *mdb.Database)
}

type iChatRPC interface {
	SetBanState(db *mdb.Database, banTime int64)
	CanChat(db *mdb.Database) bool
}

// ! coding here, add more...
