
// enum
var MOD_NOTIFY = {
		    
		  BUFF_MODE_POWER: 0,
  BUFF_MODE_SPEED: 1,
  BUFF_MODE_ATTACK: 2,
  BUFF_MODE_DEFEND: 3,
  BUFF_MODE_HEALTH: 4,
  BUFF_MODE_DIZZINESS: 5,
  BUFF_MODE_POISONING: 6,
  BUFF_MODE_CLEAN_BAD: 7,
  BUFF_MODE_CLEAN_GOOD: 8,
  BUFF_MODE_REDUCE_HURT: 9,
  BUFF_MODE_RANDOM: 10,
  BUFF_MODE_BLOCK: 11,
  BUFF_MODE_BLOCK_LEVEL: 12,
  BUFF_MODE_DODGE_LEVEL: 13,
  BUFF_MODE_CRITIAL_LEVEL: 14,
  BUFF_MODE_HIT_LEVEL: 15,
  BUFF_MODE_HURT_ADD: 16,
  BUFF_MODE_MAX_HEALTH: 17,
  BUFF_MODE_KEEPER_REDUCE_HURT: 18,
  BUFF_MODE_ATTRACT_FIRE: 19,
  BUFF_MODE_DESTROY_LEVEL: 20,
  BUFF_MODE_TENACITY_LEVEL: 21,
  BUFF_MODE_SUNDER: 22,
  BUFF_MODE_SLEEP: 23,
  BUFF_MODE_DISABLE_SKILL: 24,
  BUFF_MODE_DIRECT_REDUCE_HURT: 25,
  BUFF_MODE_ABSORB_HURT: 26,
  BUFF_MODE_GHOST_POWER: 27,
  BUFF_MODE_PET_LIVE_ROUND: 28,
  BUFF_MODE_BUDDY_SKILL: 29,
  BUFF_MODE_CLEAR_ABSORB_HURT: 30,
  BUFF_MODE_SLEEP_LEVEL: 31,
  BUFF_MODE_DIZZINESS_LEVEL: 32,
  BUFF_MODE_RANDOM_LEVEL: 33,
  BUFF_MODE_DISABLE_SKILL_LEVEL: 34,
  BUFF_MODE_BUFF_POISONING_LEVEL: 35,
  BUFF_MODE_BUFF_RECOVER_BUDDY_SKILL: 36,
  BUFF_MODE_BUFF_MAKE_POWER_FULL: 37,
  BUFF_MODE_BUFF_DOGE: 38,
  BUFF_MODE_BUFF_HIT: 39,
  BUFF_MODE_BUFF_CRITIAL: 40,
  BUFF_MODE_BUFF_TENACITY: 41,
  BUFF_MODE_BUFF_TAKE_SUNSER: 42,
  BUFF_MODE_BUFF_DEFEND_PERSENT: 43,
  BUFF_MODE_BUFF_SUNDER_STATE: 44,

}

PIModule.Notify = PIModule.Notify || {};

PIModule.Notify.sendPlayer_key_changed = function() {
  PIProtocol.getInstance().send_packet( ((arguments[0]===undefined) ? 'def' : arguments[0]), 8,0, {
  });
};

