var coins_exchange_data = {
		/**
	 * 0 : unique_key, smallint, 第几次兑换
	 * 1 : ingot, bigint, 消耗元宝
	 * 2 : coins, bigint, 获得铜币 
	 */

	Unique_key : 0,
	Ingot : 1,
	Coins : 2,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 40 /*[1]*/, 100000 /*[2]*/],
		[2 /*[0]*/, 80 /*[1]*/, 100000 /*[2]*/],
		[3 /*[0]*/, 80 /*[1]*/, 100000 /*[2]*/],
		[4 /*[0]*/, 80 /*[1]*/, 100000 /*[2]*/],
		[5 /*[0]*/, 80 /*[1]*/, 100000 /*[2]*/],
		[6 /*[0]*/, 120 /*[1]*/, 100000 /*[2]*/],
		[7 /*[0]*/, 120 /*[1]*/, 100000 /*[2]*/],
		[8 /*[0]*/, 120 /*[1]*/, 100000 /*[2]*/],
		[9 /*[0]*/, 120 /*[1]*/, 100000 /*[2]*/],
		[10 /*[0]*/, 120 /*[1]*/, 100000 /*[2]*/],
		[11 /*[0]*/, 180 /*[1]*/, 100000 /*[2]*/],
		[12 /*[0]*/, 180 /*[1]*/, 100000 /*[2]*/],
		[13 /*[0]*/, 180 /*[1]*/, 100000 /*[2]*/],
		[14 /*[0]*/, 180 /*[1]*/, 100000 /*[2]*/],
		[15 /*[0]*/, 180 /*[1]*/, 100000 /*[2]*/],
		[16 /*[0]*/, 240 /*[1]*/, 100000 /*[2]*/],
		[17 /*[0]*/, 240 /*[1]*/, 100000 /*[2]*/],
		[18 /*[0]*/, 240 /*[1]*/, 100000 /*[2]*/],
		[19 /*[0]*/, 240 /*[1]*/, 100000 /*[2]*/],
		[20 /*[0]*/, 240 /*[1]*/, 100000 /*[2]*/],
		[21 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[22 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[23 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[24 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[25 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[26 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[27 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[28 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[29 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[30 /*[0]*/, 280 /*[1]*/, 100000 /*[2]*/],
		[31 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[32 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[33 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[34 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[35 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[36 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[37 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[38 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[39 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[40 /*[0]*/, 320 /*[1]*/, 100000 /*[2]*/],
		[41 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[42 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[43 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[44 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[45 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[46 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[47 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[48 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[49 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[50 /*[0]*/, 360 /*[1]*/, 100000 /*[2]*/],
		[51 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[52 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[53 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[54 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[55 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[56 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[57 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[58 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[59 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[60 /*[0]*/, 400 /*[1]*/, 100000 /*[2]*/],
		[61 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[62 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[63 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[64 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[65 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[66 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[67 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[68 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[69 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[70 /*[0]*/, 440 /*[1]*/, 100000 /*[2]*/],
		[71 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[72 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[73 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[74 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[75 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[76 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[77 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[78 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[79 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/],
		[80 /*[0]*/, 480 /*[1]*/, 100000 /*[2]*/]
	],
};
