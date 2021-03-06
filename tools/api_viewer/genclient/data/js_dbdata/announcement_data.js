var announcement_data = {
		/**
	 * 0 : id, int, 公告模版ID
	 * 1 : type, tinyint, 0-走马灯公告
	 * 2 : parameters, varchar, 参数
	 * 3 : content, varchar, 内容
	 * 4 : duration, int, 消息存活时间（秒）
	 * 5 : show_cyle, int, 重复展示时间间隔（秒） 
	 */

	Id : 0,
	Type : 1,
	Parameters : 2,
	Content : 3,
	Duration : 4,
	Show_cyle : 5,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 0 /*[1]*/, "p1,参数一" /*[2]*/, "欢迎来到仙侠道{0}" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/],
		[2 /*[0]*/, 0 /*[1]*/, "" /*[2]*/, "测试用公告登录滚动播放" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/],
		[3 /*[0]*/, 0 /*[1]*/, "" /*[2]*/, "亲爱的各位玩家，服务器将在10分钟后关闭。我们为对广大玩家对来的不便深表歉意，各个关卡将在服务器关闭前2分钟停止进入。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/],
		[4 /*[0]*/, 0 /*[1]*/, "timing,出现时间;disappear,消失时间" /*[2]*/, "巡游商人将在{0]出现，在{1}离开" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/]
	],
};
