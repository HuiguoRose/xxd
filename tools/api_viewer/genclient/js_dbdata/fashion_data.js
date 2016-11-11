var fashion_data = {
		/**
	 * 0 : id, smallint, 时装ID
	 * 1 : name, varchar, 时装名称
	 * 2 : level, int, 需求等级
	 * 3 : desc, varchar, 时装描述
	 * 4 : source, varchar, 时装来源
	 * 5 : sign, varchar, 资源标识
	 * 6 : health, int, 生命
	 * 7 : speed, int, 速度
	 * 8 : cultivation, int, 内力
	 * 9 : attack, int, 攻击
	 * 10 : defence, int, 防御
	 * 11 : item_sign, varchar, 对应物品资源标识 
	 */

	Id : 0,
	Name : 1,
	Level : 2,
	Desc : 3,
	Source : 4,
	Sign : 5,
	Health : 6,
	Speed : 7,
	Cultivation : 8,
	Attack : 9,
	Defence : 10,
	Item_sign : 11,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[2 /*[0]*/, "大漠惊鸿" /*[1]*/, 5 /*[2]*/, "手把金刀，横行大漠，男儿志岂万里；纵马西行，惊鸿翩飞，一去落日暗尘沙" /*[3]*/, "时装团购获得" /*[4]*/, "DaMoJingHong" /*[5]*/, 100 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, "DaMoJingHong" /*[11]*/],
		[7 /*[0]*/, "武道" /*[1]*/, 10 /*[2]*/, "以武为道，以仁心推己及人，化干戈为知己，合天地于一气" /*[3]*/, "仙尊8级获得" /*[4]*/, "WuDao" /*[5]*/, 500 /*[6]*/, 50 /*[7]*/, 0 /*[8]*/, 100 /*[9]*/, 0 /*[10]*/, "WuDao" /*[11]*/],
		[8 /*[0]*/, "风云" /*[1]*/, 30 /*[2]*/, "风云一起天下变，惊雷天神下苍穹" /*[3]*/, "敬请期待" /*[4]*/, "FengYun" /*[5]*/, 1000 /*[6]*/, 100 /*[7]*/, 0 /*[8]*/, 100 /*[9]*/, 0 /*[10]*/, "FengYun" /*[11]*/]
	],
};
