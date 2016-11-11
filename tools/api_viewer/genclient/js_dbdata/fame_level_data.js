var fame_level_data = {
		/**
	 * 0 : id, int, ID
	 * 1 : level, smallint, 等级
	 * 2 : required_fame, int, 要求声望 
	 */

	Id : 0,
	Level : 1,
	Required_fame : 2,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 1 /*[1]*/, 0 /*[2]*/],
		[2 /*[0]*/, 2 /*[1]*/, 30 /*[2]*/],
		[3 /*[0]*/, 3 /*[1]*/, 200 /*[2]*/],
		[4 /*[0]*/, 4 /*[1]*/, 500 /*[2]*/],
		[5 /*[0]*/, 5 /*[1]*/, 1000 /*[2]*/],
		[6 /*[0]*/, 6 /*[1]*/, 1500 /*[2]*/],
		[7 /*[0]*/, 7 /*[1]*/, 2000 /*[2]*/],
		[8 /*[0]*/, 8 /*[1]*/, 3000 /*[2]*/],
		[9 /*[0]*/, 9 /*[1]*/, 5000 /*[2]*/],
		[10 /*[0]*/, 10 /*[1]*/, 7000 /*[2]*/],
		[11 /*[0]*/, 11 /*[1]*/, 15000 /*[2]*/],
		[12 /*[0]*/, 12 /*[1]*/, 30000 /*[2]*/],
		[13 /*[0]*/, 13 /*[1]*/, 50000 /*[2]*/],
		[14 /*[0]*/, 14 /*[1]*/, 75000 /*[2]*/],
		[15 /*[0]*/, 15 /*[1]*/, 100000 /*[2]*/],
		[16 /*[0]*/, 16 /*[1]*/, 130000 /*[2]*/],
		[17 /*[0]*/, 17 /*[1]*/, 160000 /*[2]*/],
		[18 /*[0]*/, 18 /*[1]*/, 200000 /*[2]*/],
		[19 /*[0]*/, 19 /*[1]*/, 240000 /*[2]*/],
		[20 /*[0]*/, 20 /*[1]*/, 290000 /*[2]*/],
		[21 /*[0]*/, 21 /*[1]*/, 340000 /*[2]*/],
		[22 /*[0]*/, 22 /*[1]*/, 400000 /*[2]*/],
		[23 /*[0]*/, 23 /*[1]*/, 460000 /*[2]*/],
		[24 /*[0]*/, 24 /*[1]*/, 530000 /*[2]*/],
		[25 /*[0]*/, 25 /*[1]*/, 600000 /*[2]*/],
		[26 /*[0]*/, 26 /*[1]*/, 700000 /*[2]*/],
		[27 /*[0]*/, 27 /*[1]*/, 900000 /*[2]*/],
		[28 /*[0]*/, 28 /*[1]*/, 1200000 /*[2]*/],
		[29 /*[0]*/, 29 /*[1]*/, 1600000 /*[2]*/],
		[30 /*[0]*/, 30 /*[1]*/, 2100000 /*[2]*/],
		[31 /*[0]*/, 31 /*[1]*/, 2700000 /*[2]*/],
		[32 /*[0]*/, 32 /*[1]*/, 3500000 /*[2]*/],
		[33 /*[0]*/, 33 /*[1]*/, 4400000 /*[2]*/],
		[34 /*[0]*/, 34 /*[1]*/, 5400000 /*[2]*/],
		[35 /*[0]*/, 35 /*[1]*/, 6500000 /*[2]*/]
	],
};