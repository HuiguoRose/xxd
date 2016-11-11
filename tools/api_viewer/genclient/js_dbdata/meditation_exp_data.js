var meditation_exp_data = {
		/**
	 * 0 : id, int, 
	 * 1 : require_level, int, 要求等级
	 * 2 : exp, int, 15秒奖励经验 
	 */

	Id : 0,
	Require_level : 1,
	Exp : 2,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[3 /*[0]*/, 16 /*[1]*/, 1 /*[2]*/],
		[4 /*[0]*/, 40 /*[1]*/, 2 /*[2]*/],
		[5 /*[0]*/, 60 /*[1]*/, 3 /*[2]*/],
		[6 /*[0]*/, 80 /*[1]*/, 4 /*[2]*/],
		[7 /*[0]*/, 90 /*[1]*/, 5 /*[2]*/],
		[8 /*[0]*/, 100 /*[1]*/, 6 /*[2]*/],
		[9 /*[0]*/, 110 /*[1]*/, 7 /*[2]*/],
		[10 /*[0]*/, 120 /*[1]*/, 8 /*[2]*/]
	],
};
