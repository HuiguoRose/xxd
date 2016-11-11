var sword_soul_quality_level_data = {
		/**
	 * 0 : id, smallint, 剑心等级ID
	 * 1 : quality_id, smallint, 品质名称
	 * 2 : level, tinyint, 等级
	 * 3 : exp, int, 升到这一级所需的经验 
	 */

	Id : 0,
	Quality_id : 1,
	Level : 2,
	Exp : 3,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 1 /*[1]*/, 1 /*[2]*/, 1000 /*[3]*/],
		[2 /*[0]*/, 2 /*[1]*/, 1 /*[2]*/, 100 /*[3]*/],
		[3 /*[0]*/, 2 /*[1]*/, 2 /*[2]*/, 100 /*[3]*/],
		[4 /*[0]*/, 2 /*[1]*/, 3 /*[2]*/, 250 /*[3]*/],
		[5 /*[0]*/, 2 /*[1]*/, 4 /*[2]*/, 500 /*[3]*/],
		[6 /*[0]*/, 2 /*[1]*/, 5 /*[2]*/, 1000 /*[3]*/],
		[7 /*[0]*/, 2 /*[1]*/, 6 /*[2]*/, 2000 /*[3]*/],
		[8 /*[0]*/, 2 /*[1]*/, 7 /*[2]*/, 4000 /*[3]*/],
		[9 /*[0]*/, 2 /*[1]*/, 8 /*[2]*/, 5000 /*[3]*/],
		[10 /*[0]*/, 2 /*[1]*/, 9 /*[2]*/, 6000 /*[3]*/],
		[11 /*[0]*/, 2 /*[1]*/, 10 /*[2]*/, 7000 /*[3]*/],
		[12 /*[0]*/, 3 /*[1]*/, 1 /*[2]*/, 200 /*[3]*/],
		[13 /*[0]*/, 3 /*[1]*/, 2 /*[2]*/, 250 /*[3]*/],
		[14 /*[0]*/, 3 /*[1]*/, 3 /*[2]*/, 500 /*[3]*/],
		[15 /*[0]*/, 3 /*[1]*/, 4 /*[2]*/, 1000 /*[3]*/],
		[16 /*[0]*/, 3 /*[1]*/, 5 /*[2]*/, 2000 /*[3]*/],
		[17 /*[0]*/, 3 /*[1]*/, 6 /*[2]*/, 4000 /*[3]*/],
		[18 /*[0]*/, 3 /*[1]*/, 7 /*[2]*/, 5000 /*[3]*/],
		[19 /*[0]*/, 3 /*[1]*/, 8 /*[2]*/, 6000 /*[3]*/],
		[20 /*[0]*/, 3 /*[1]*/, 9 /*[2]*/, 7000 /*[3]*/],
		[21 /*[0]*/, 3 /*[1]*/, 10 /*[2]*/, 8000 /*[3]*/],
		[22 /*[0]*/, 4 /*[1]*/, 1 /*[2]*/, 500 /*[3]*/],
		[23 /*[0]*/, 4 /*[1]*/, 2 /*[2]*/, 500 /*[3]*/],
		[24 /*[0]*/, 4 /*[1]*/, 3 /*[2]*/, 1000 /*[3]*/],
		[25 /*[0]*/, 4 /*[1]*/, 4 /*[2]*/, 2000 /*[3]*/],
		[26 /*[0]*/, 4 /*[1]*/, 5 /*[2]*/, 4000 /*[3]*/],
		[27 /*[0]*/, 4 /*[1]*/, 6 /*[2]*/, 5000 /*[3]*/],
		[28 /*[0]*/, 4 /*[1]*/, 7 /*[2]*/, 6000 /*[3]*/],
		[29 /*[0]*/, 4 /*[1]*/, 8 /*[2]*/, 7000 /*[3]*/],
		[30 /*[0]*/, 4 /*[1]*/, 9 /*[2]*/, 8000 /*[3]*/],
		[31 /*[0]*/, 4 /*[1]*/, 10 /*[2]*/, 9000 /*[3]*/],
		[32 /*[0]*/, 5 /*[1]*/, 1 /*[2]*/, 1500 /*[3]*/],
		[33 /*[0]*/, 5 /*[1]*/, 2 /*[2]*/, 1000 /*[3]*/],
		[34 /*[0]*/, 5 /*[1]*/, 3 /*[2]*/, 2000 /*[3]*/],
		[35 /*[0]*/, 5 /*[1]*/, 4 /*[2]*/, 4000 /*[3]*/],
		[36 /*[0]*/, 5 /*[1]*/, 5 /*[2]*/, 5000 /*[3]*/],
		[37 /*[0]*/, 5 /*[1]*/, 6 /*[2]*/, 6000 /*[3]*/],
		[38 /*[0]*/, 5 /*[1]*/, 7 /*[2]*/, 7000 /*[3]*/],
		[39 /*[0]*/, 5 /*[1]*/, 8 /*[2]*/, 8000 /*[3]*/],
		[40 /*[0]*/, 5 /*[1]*/, 9 /*[2]*/, 9000 /*[3]*/],
		[41 /*[0]*/, 5 /*[1]*/, 10 /*[2]*/, 10000 /*[3]*/],
		[42 /*[0]*/, 6 /*[1]*/, 1 /*[2]*/, 3000 /*[3]*/],
		[43 /*[0]*/, 6 /*[1]*/, 2 /*[2]*/, 2000 /*[3]*/],
		[44 /*[0]*/, 6 /*[1]*/, 3 /*[2]*/, 4000 /*[3]*/],
		[45 /*[0]*/, 6 /*[1]*/, 4 /*[2]*/, 5000 /*[3]*/],
		[46 /*[0]*/, 6 /*[1]*/, 5 /*[2]*/, 6000 /*[3]*/],
		[47 /*[0]*/, 6 /*[1]*/, 6 /*[2]*/, 7000 /*[3]*/],
		[48 /*[0]*/, 6 /*[1]*/, 7 /*[2]*/, 8000 /*[3]*/],
		[49 /*[0]*/, 6 /*[1]*/, 8 /*[2]*/, 9000 /*[3]*/],
		[50 /*[0]*/, 6 /*[1]*/, 9 /*[2]*/, 10000 /*[3]*/],
		[51 /*[0]*/, 6 /*[1]*/, 10 /*[2]*/, 11000 /*[3]*/],
		[52 /*[0]*/, 2 /*[1]*/, 11 /*[2]*/, 8000 /*[3]*/],
		[53 /*[0]*/, 2 /*[1]*/, 12 /*[2]*/, 9000 /*[3]*/],
		[54 /*[0]*/, 2 /*[1]*/, 13 /*[2]*/, 10000 /*[3]*/],
		[55 /*[0]*/, 2 /*[1]*/, 14 /*[2]*/, 11000 /*[3]*/],
		[56 /*[0]*/, 2 /*[1]*/, 15 /*[2]*/, 12000 /*[3]*/],
		[57 /*[0]*/, 2 /*[1]*/, 16 /*[2]*/, 13000 /*[3]*/],
		[58 /*[0]*/, 2 /*[1]*/, 17 /*[2]*/, 14000 /*[3]*/],
		[59 /*[0]*/, 2 /*[1]*/, 18 /*[2]*/, 15000 /*[3]*/],
		[60 /*[0]*/, 2 /*[1]*/, 19 /*[2]*/, 16000 /*[3]*/],
		[61 /*[0]*/, 2 /*[1]*/, 20 /*[2]*/, 17000 /*[3]*/],
		[62 /*[0]*/, 3 /*[1]*/, 11 /*[2]*/, 9000 /*[3]*/],
		[63 /*[0]*/, 3 /*[1]*/, 12 /*[2]*/, 10000 /*[3]*/],
		[64 /*[0]*/, 3 /*[1]*/, 13 /*[2]*/, 11000 /*[3]*/],
		[65 /*[0]*/, 3 /*[1]*/, 14 /*[2]*/, 12000 /*[3]*/],
		[66 /*[0]*/, 3 /*[1]*/, 15 /*[2]*/, 13000 /*[3]*/],
		[67 /*[0]*/, 3 /*[1]*/, 16 /*[2]*/, 14000 /*[3]*/],
		[68 /*[0]*/, 3 /*[1]*/, 17 /*[2]*/, 15000 /*[3]*/],
		[69 /*[0]*/, 3 /*[1]*/, 18 /*[2]*/, 16000 /*[3]*/],
		[70 /*[0]*/, 3 /*[1]*/, 19 /*[2]*/, 17000 /*[3]*/],
		[71 /*[0]*/, 3 /*[1]*/, 20 /*[2]*/, 18000 /*[3]*/],
		[72 /*[0]*/, 4 /*[1]*/, 11 /*[2]*/, 10000 /*[3]*/],
		[73 /*[0]*/, 4 /*[1]*/, 12 /*[2]*/, 11000 /*[3]*/],
		[74 /*[0]*/, 4 /*[1]*/, 13 /*[2]*/, 12000 /*[3]*/],
		[75 /*[0]*/, 4 /*[1]*/, 14 /*[2]*/, 13000 /*[3]*/],
		[76 /*[0]*/, 4 /*[1]*/, 15 /*[2]*/, 14000 /*[3]*/],
		[77 /*[0]*/, 4 /*[1]*/, 16 /*[2]*/, 15000 /*[3]*/],
		[78 /*[0]*/, 4 /*[1]*/, 17 /*[2]*/, 16000 /*[3]*/],
		[79 /*[0]*/, 4 /*[1]*/, 18 /*[2]*/, 17000 /*[3]*/],
		[80 /*[0]*/, 4 /*[1]*/, 19 /*[2]*/, 18000 /*[3]*/],
		[81 /*[0]*/, 4 /*[1]*/, 20 /*[2]*/, 19000 /*[3]*/],
		[82 /*[0]*/, 5 /*[1]*/, 11 /*[2]*/, 11000 /*[3]*/],
		[83 /*[0]*/, 5 /*[1]*/, 12 /*[2]*/, 12000 /*[3]*/],
		[84 /*[0]*/, 5 /*[1]*/, 13 /*[2]*/, 13000 /*[3]*/],
		[85 /*[0]*/, 5 /*[1]*/, 14 /*[2]*/, 14000 /*[3]*/],
		[86 /*[0]*/, 5 /*[1]*/, 15 /*[2]*/, 15000 /*[3]*/],
		[87 /*[0]*/, 5 /*[1]*/, 16 /*[2]*/, 16000 /*[3]*/],
		[88 /*[0]*/, 5 /*[1]*/, 17 /*[2]*/, 17000 /*[3]*/],
		[89 /*[0]*/, 5 /*[1]*/, 18 /*[2]*/, 18000 /*[3]*/],
		[90 /*[0]*/, 5 /*[1]*/, 19 /*[2]*/, 19000 /*[3]*/],
		[91 /*[0]*/, 5 /*[1]*/, 20 /*[2]*/, 20000 /*[3]*/],
		[92 /*[0]*/, 6 /*[1]*/, 11 /*[2]*/, 12000 /*[3]*/],
		[93 /*[0]*/, 6 /*[1]*/, 12 /*[2]*/, 13000 /*[3]*/],
		[94 /*[0]*/, 6 /*[1]*/, 13 /*[2]*/, 14000 /*[3]*/],
		[95 /*[0]*/, 6 /*[1]*/, 14 /*[2]*/, 15000 /*[3]*/],
		[96 /*[0]*/, 6 /*[1]*/, 15 /*[2]*/, 16000 /*[3]*/],
		[97 /*[0]*/, 6 /*[1]*/, 16 /*[2]*/, 17000 /*[3]*/],
		[98 /*[0]*/, 6 /*[1]*/, 17 /*[2]*/, 18000 /*[3]*/],
		[99 /*[0]*/, 6 /*[1]*/, 18 /*[2]*/, 19000 /*[3]*/],
		[100 /*[0]*/, 6 /*[1]*/, 19 /*[2]*/, 20000 /*[3]*/],
		[101 /*[0]*/, 6 /*[1]*/, 20 /*[2]*/, 21000 /*[3]*/]
	],
};
