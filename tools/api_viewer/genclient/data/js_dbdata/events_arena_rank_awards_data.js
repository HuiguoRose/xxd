var events_arena_rank_awards_data = {
		/**
	 * 0 : id, smallint, 
	 * 1 : require_arena_rank, smallint, 需要排名
	 * 2 : ingot, smallint, 奖励元宝
	 * 3 : coins, int, 奖励铜钱
	 * 4 : item1_id, smallint, 物品1
	 * 5 : item1_num, smallint, 物品1数量
	 * 6 : item2_id, smallint, 物品2
	 * 7 : item2_num, smallint, 物品2数量
	 * 8 : item3_id, smallint, 物品3
	 * 9 : item3_num, smallint, 物品3数量
	 * 10 : item4_id, smallint, 物品4
	 * 11 : item4_num, smallint, 物品4数量
	 * 12 : item5_id, smallint, 物品5
	 * 13 : item5_num, smallint, 物品5数量 
	 */

	Id : 0,
	Require_arena_rank : 1,
	Ingot : 2,
	Coins : 3,
	Item1_id : 4,
	Item1_num : 5,
	Item2_id : 6,
	Item2_num : 7,
	Item3_id : 8,
	Item3_num : 9,
	Item4_id : 10,
	Item4_num : 11,
	Item5_id : 12,
	Item5_num : 13,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 1 /*[1]*/, 2000 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/],
		[3 /*[0]*/, 2 /*[1]*/, 1000 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/],
		[4 /*[0]*/, 3 /*[1]*/, 750 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/],
		[11 /*[0]*/, 10 /*[1]*/, 500 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/],
		[14 /*[0]*/, 50 /*[1]*/, 300 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/],
		[15 /*[0]*/, 100 /*[1]*/, 200 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/],
		[16 /*[0]*/, 500 /*[1]*/, 100 /*[2]*/, 0 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/]
	],
};
