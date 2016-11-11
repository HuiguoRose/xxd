var events_level_up_data = {
		/**
	 * 0 : id, smallint, 
	 * 1 : require_level, smallint, 需要等级
	 * 2 : ingot, smallint, 奖励元宝
	 * 3 : item1_id, smallint, 物品1
	 * 4 : item1_num, smallint, 物品1数量
	 * 5 : item2_id, smallint, 物品2
	 * 6 : item2_num, smallint, 物品2数量
	 * 7 : item3_id, smallint, 物品3
	 * 8 : item3_num, smallint, 物品3数量
	 * 9 : coins, int, 奖励铜钱 
	 */

	Id : 0,
	Require_level : 1,
	Ingot : 2,
	Item1_id : 3,
	Item1_num : 4,
	Item2_id : 5,
	Item2_num : 6,
	Item3_id : 7,
	Item3_num : 8,
	Coins : 9,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[3 /*[0]*/, 15 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 500 /*[9]*/],
		[4 /*[0]*/, 20 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 1000 /*[9]*/],
		[5 /*[0]*/, 25 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 5000 /*[9]*/],
		[13 /*[0]*/, 30 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 10000 /*[9]*/],
		[7 /*[0]*/, 35 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 15000 /*[9]*/],
		[8 /*[0]*/, 40 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 20000 /*[9]*/],
		[9 /*[0]*/, 45 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 25000 /*[9]*/],
		[10 /*[0]*/, 50 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 30000 /*[9]*/],
		[11 /*[0]*/, 55 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 35000 /*[9]*/],
		[14 /*[0]*/, 60 /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 40000 /*[9]*/]
	],
};