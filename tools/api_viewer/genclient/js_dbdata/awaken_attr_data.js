var awaken_attr_data = {
		/**
	 * 0 : id, smallint, 觉醒属性ID
	 * 1 : name, varchar, 觉醒名称
	 * 2 : is_skill, tinyint, 是否为技能
	 * 3 : skill_id, smallint, 技能ID
	 * 4 : type, tinyint, 属性类型
	 * 5 : attr, int, 加成数值
	 * 6 : lights, tinyint, 希望之光需求量 
	 */

	Id : 0,
	Name : 1,
	Is_skill : 2,
	Skill_id : 3,
	Type : 4,
	Attr : 5,
	Lights : 6,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[5098 /*[0]*/, "生命觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 1 /*[4]*/, 500 /*[5]*/, 10 /*[6]*/],
		[5099 /*[0]*/, "攻击觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 2 /*[4]*/, 100 /*[5]*/, 10 /*[6]*/],
		[5100 /*[0]*/, "防御觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 3 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5101 /*[0]*/, "内力觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 4 /*[4]*/, 100 /*[5]*/, 10 /*[6]*/],
		[5102 /*[0]*/, "速度觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 5 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5103 /*[0]*/, "护甲觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 6 /*[4]*/, 10 /*[5]*/, 10 /*[6]*/],
		[5104 /*[0]*/, "命中觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 7 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5105 /*[0]*/, "闪避觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 8 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5106 /*[0]*/, "格挡觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 9 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5107 /*[0]*/, "破击觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 10 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5108 /*[0]*/, "暴击觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 11 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5109 /*[0]*/, "韧性觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 12 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5110 /*[0]*/, "中毒抗性觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 13 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5111 /*[0]*/, "封魔抗性觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 14 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5112 /*[0]*/, "睡眠抗性觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 15 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5113 /*[0]*/, "晕眩抗性觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 16 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5114 /*[0]*/, "混乱抗性觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 17 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5115 /*[0]*/, "仙灵伤害觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 18 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5116 /*[0]*/, "人兽伤害觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 19 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5117 /*[0]*/, "妖魔伤害觉醒" /*[1]*/, 0 /*[2]*/, 0 /*[3]*/, 20 /*[4]*/, 50 /*[5]*/, 10 /*[6]*/],
		[5118 /*[0]*/, "万剑长空" /*[1]*/, 1 /*[2]*/, 1671 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5119 /*[0]*/, "般若行龙" /*[1]*/, 1 /*[2]*/, 1672 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5120 /*[0]*/, "收妖诀" /*[1]*/, 1 /*[2]*/, 1673 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5121 /*[0]*/, "妙手回春" /*[1]*/, 1 /*[2]*/, 1659 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5122 /*[0]*/, "风击暴袭" /*[1]*/, 1 /*[2]*/, 1660 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5123 /*[0]*/, "怒风沙爆" /*[1]*/, 1 /*[2]*/, 1661 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5124 /*[0]*/, "断水斩" /*[1]*/, 1 /*[2]*/, 1656 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5125 /*[0]*/, "百炼狂刀" /*[1]*/, 1 /*[2]*/, 1657 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5126 /*[0]*/, "斩魄刀" /*[1]*/, 1 /*[2]*/, 1658 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5127 /*[0]*/, "九转重阳" /*[1]*/, 1 /*[2]*/, 1662 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5128 /*[0]*/, "回春续劲" /*[1]*/, 1 /*[2]*/, 1663 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5129 /*[0]*/, "青竹神咒" /*[1]*/, 1 /*[2]*/, 1664 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5130 /*[0]*/, "影狼突袭" /*[1]*/, 1 /*[2]*/, 1665 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5131 /*[0]*/, "巫雀奇袭" /*[1]*/, 1 /*[2]*/, 1666 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5132 /*[0]*/, "墨画灵山" /*[1]*/, 1 /*[2]*/, 1667 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5133 /*[0]*/, "冷云烟" /*[1]*/, 1 /*[2]*/, 1668 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5134 /*[0]*/, "落樱斩" /*[1]*/, 1 /*[2]*/, 1669 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5135 /*[0]*/, "影舞斩" /*[1]*/, 1 /*[2]*/, 1670 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5136 /*[0]*/, "水行者" /*[1]*/, 1 /*[2]*/, 1674 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5137 /*[0]*/, "金钟罩" /*[1]*/, 1 /*[2]*/, 1675 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5138 /*[0]*/, "金刚庇护" /*[1]*/, 1 /*[2]*/, 1676 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5139 /*[0]*/, "真灵守护" /*[1]*/, 1 /*[2]*/, 1677 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5140 /*[0]*/, "狮子吼" /*[1]*/, 1 /*[2]*/, 1678 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5141 /*[0]*/, "金刚怒目" /*[1]*/, 1 /*[2]*/, 1679 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5142 /*[0]*/, "致命" /*[1]*/, 1 /*[2]*/, 1680 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5143 /*[0]*/, "寒冰凛冽" /*[1]*/, 1 /*[2]*/, 1681 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5144 /*[0]*/, "寒冰甲" /*[1]*/, 1 /*[2]*/, 1682 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5145 /*[0]*/, "落星式" /*[1]*/, 1 /*[2]*/, 1683 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5146 /*[0]*/, "冬夜之拥" /*[1]*/, 1 /*[2]*/, 1684 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5147 /*[0]*/, "吸星锁" /*[1]*/, 1 /*[2]*/, 1685 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5148 /*[0]*/, "龙麟盾" /*[1]*/, 1 /*[2]*/, 1686 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5149 /*[0]*/, "千钧破" /*[1]*/, 1 /*[2]*/, 1687 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5150 /*[0]*/, "降妖伞" /*[1]*/, 1 /*[2]*/, 1688 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5151 /*[0]*/, "撼天狂掌" /*[1]*/, 1 /*[2]*/, 1689 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5152 /*[0]*/, "韦驮拳" /*[1]*/, 1 /*[2]*/, 1690 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5153 /*[0]*/, "星沉地动" /*[1]*/, 1 /*[2]*/, 1691 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5154 /*[0]*/, "寒月剑法" /*[1]*/, 1 /*[2]*/, 1692 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5155 /*[0]*/, "万剑藏锋" /*[1]*/, 1 /*[2]*/, 1693 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/],
		[5156 /*[0]*/, "雷动九天" /*[1]*/, 1 /*[2]*/, 1694 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 100 /*[6]*/]
	],
};
