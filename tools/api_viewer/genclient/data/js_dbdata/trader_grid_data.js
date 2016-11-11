var trader_grid_data = {
		/**
	 * 0 : id, int, ID
	 * 1 : money_type, tinyint, 货币类型 
	 */

	Id : 0,
	Money_type : 1,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 0 /*[1]*/],
		[2 /*[0]*/, 0 /*[1]*/],
		[3 /*[0]*/, 0 /*[1]*/],
		[4 /*[0]*/, 1 /*[1]*/],
		[5 /*[0]*/, 1 /*[1]*/],
		[7 /*[0]*/, 1 /*[1]*/],
		[8 /*[0]*/, 2 /*[1]*/],
		[21 /*[0]*/, 1 /*[1]*/],
		[22 /*[0]*/, 2 /*[1]*/],
		[23 /*[0]*/, 1 /*[1]*/],
		[24 /*[0]*/, 1 /*[1]*/],
		[25 /*[0]*/, 1 /*[1]*/],
		[26 /*[0]*/, 1 /*[1]*/],
		[27 /*[0]*/, 0 /*[1]*/]
	],
};