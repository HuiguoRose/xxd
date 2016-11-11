package tlog

import (
	"game_server/mdb"
	"io"
	"net"
	"strings"
	"time"
)

var (
	s_hostAddr string
	s_udpConn  *net.UDPConn

	g_GamePlatID int32 // 0 ios; 1 android
	g_GameAppID  string
	g_GameSrvID  string
)

// tlog模块要求所有日志类型都实现Log接口
type Log interface {
	Packet() []byte
}

// tlog模块对外只提供一个统一的Send方法
func Send(log Log) (int, error) {
	return s_udpConn.Write(log.Packet())
}

func SendRaw(raw []byte) (int, error) {
	return s_udpConn.Write(raw)
}

// 初始化服务器地址
func Start(server, appID, srvID string, platID int32) error {
	addr, err := net.ResolveUDPAddr("udp4", server)
	if err != nil {
		return err
	}

	s_udpConn, err = net.DialUDP("udp4", nil, addr)
	if err != nil {
		return err
	}

	s_hostAddr = strings.Split(s_udpConn.LocalAddr().String(), ":")[0]

	g_GamePlatID = platID
	g_GameAppID = appID
	g_GameSrvID = srvID

	logHeart()

	return err
}

func Stop() {
	if s_udpConn != nil {
		s_udpConn.Close()
	}
}

func UpdateTlogPlatId(id int32) {
	g_GamePlatID = id
}

func logHeart() {
	time.AfterFunc(time.Minute*1, func() {
		mdb.Transaction(mdb.TRANS_TAG_TlogHeart, func() {
			mdb.GlobalExecute(func(db *mdb.Database) {
				db.AddTLog(NewGameSvrState(s_hostAddr))
			})
		})

		logHeart()
	})
}

// 测试用，packet写入文件，使用工具检查是否正确
func debugWriteToFile(log Log, f io.Writer) {
	buf := log.Packet()
	buf = append(buf, []byte("\n")...)
	f.Write(buf)
}
