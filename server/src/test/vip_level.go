package main

import (
	"fmt"
	"time"

	"client_test"
	"game_server/api/protocol/notify_api"
	"game_server/api/protocol/player_api"
	"game_server/api/protocol/vip_api"
)

func main() {
	client := client_test.NewClient("127.0.0.1:8080")
	//client.Player_FromPlatformLogin("vip01", "vip01", 1, "", 0, false)
	client.Player_FromPlatformLogin("coins1", "coins1", 1, "", 0, false)

	//注册回调函数
	client.OutPlayer_Info = func(out *player_api.Info_Out) {
		fmt.Println("\n==============")
		fmt.Printf("player_api.InfoOut:\n%#v\n", out)
		fmt.Println("==============\n")
	}

	client.OutNotify_VipLevelChange = func(out *notify_api.VipLevelChange_Out) {
		fmt.Println("==============")
		fmt.Printf("notify_api.VipLevelChange_Out:\n%#v\n", out)
		fmt.Println("==============")
	}

	client.OutNotify_MoneyChange = func(out *notify_api.MoneyChange_Out) {
		fmt.Println("==============")
		fmt.Printf("notify_api.MoneyChange_Out:\n%#v\n", out)
		fmt.Println("==============")
	}

	client.OutVip_Info = func(out *vip_api.Info_Out) {
		fmt.Println("==============")
		fmt.Printf("vip_api.Info:\n%#v\n", out)
		fmt.Println("==============")
	}

	//获取用户信息，期待里面会有新的字段
	client.Player_Info()
	client.Vip_Info(148)

	//调用调试接口获取设置一定数量的元宝
	client.Debug_SetIngot(109)

	//再次查看用户信息
	client.Player_Info()
	client.Vip_Info(148)


	b := time.Tick(5 * time.Second)
	<-b
}
