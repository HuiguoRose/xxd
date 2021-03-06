#!/usr/bin/evn python
#  -*- coding: utf8 -*-

import struct

import interface

OUT_RESULT_FAILED = 0
OUT_RESULT_SUCCEED = 1


EXTEND_TYPE_RESOURCE = 1
EXTEND_TYPE_ACTIVITY = 2


EXTEND_LEVEL_TYPE_RESOURCE = 1
EXTEND_LEVEL_TYPE_BUDDY = 9
EXTEND_LEVEL_TYPE_PET = 10
EXTEND_LEVEL_TYPE_GHOST = 11


EXTEND_LEVEL_SUB_TYPE_NONE = 0
EXTEND_LEVEL_SUB_TYPE_COIN = 1
EXTEND_LEVEL_SUB_TYPE_EXP = 2


BATTLE_TYPE_MISSION = 0
BATTLE_TYPE_RESOURCE = 1
BATTLE_TYPE_TOWER = 2
BATTLE_TYPE_MULTILEVEL = 3
BATTLE_TYPE_HARD = 8
BATTLE_TYPE_BUDDY = 9
BATTLE_TYPE_PET = 10
BATTLE_TYPE_GHOST = 11
BATTLE_TYPE_RAINBOW = 12
BATTLE_TYPE_PVE = 13


class OpenUp(object):
    _module = 4
    _action = 0

    def __init__(self):
        pass
        self.mission_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.mission_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.mission_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class OpenDown(object):
    _module = 4
    _action = 0

    def __init__(self):
        pass
        self.result = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class GetMissionLevelUp(object):
    _module = 4
    _action = 1

    def __init__(self):
        pass
        self.mission_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.mission_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.mission_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class GetMissionLevelDown(object):
    _module = 4
    _action = 1

    def __init__(self):
        pass
        self.result = 0
        self.levels = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        buff.extend(struct.pack('<B', len(self.levels)))
        for item in self.levels:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        _levels_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_levels_size):
            obj = GetMissionLevelDownLevels()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.levels.append(obj)

    def size(self):
        size = 2
        for item in self.levels:
            size += item.size()
        return size


class GetMissionLevelDownLevels(object):
    def __init__(self):
        pass
        self.level_id = 0
        self.round_num = 0
        self.daily_num = 0
        self.waiting_shadows = 0
        self.remain_buy_times = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.level_id))
        buff.extend(struct.pack("<b", self.round_num))
        buff.extend(struct.pack("<b", self.daily_num))
        buff.extend(struct.pack("<b", self.waiting_shadows))
        buff.extend(struct.pack("<h", self.remain_buy_times))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.round_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.daily_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.waiting_shadows = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.remain_buy_times = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 9
        

class EnterLevelUp(object):
    _module = 4
    _action = 2

    def __init__(self):
        pass
        self.mission_level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.mission_level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.mission_level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class EnterLevelDown(object):
    _module = 4
    _action = 2

    def __init__(self):
        pass
        self.result = 0
        self.smallbox = []
        self.meng_yao = []
        self.shadow = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        buff.extend(struct.pack('<B', len(self.smallbox)))
        for item in self.smallbox:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.meng_yao)))
        for item in self.meng_yao:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.shadow)))
        for item in self.shadow:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        _smallbox_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_smallbox_size):
            obj = EnterLevelDownSmallbox()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.smallbox.append(obj)

        _meng_yao_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_meng_yao_size):
            obj = EnterLevelDownMengYao()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.meng_yao.append(obj)

        _shadow_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_shadow_size):
            obj = EnterLevelDownShadow()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.shadow.append(obj)

    def size(self):
        size = 4
        for item in self.smallbox:
            size += item.size()
        for item in self.meng_yao:
            size += item.size()
        for item in self.shadow:
            size += item.size()
        return size


class EnterLevelDownSmallbox(object):
    def __init__(self):
        pass
        self.box_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.box_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class EnterLevelDownMengYao(object):
    def __init__(self):
        pass
        self.my_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.my_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.my_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class EnterLevelDownShadow(object):
    def __init__(self):
        pass
        self.shaded_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.shaded_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.shaded_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class OpenLevelBoxUp(object):
    _module = 4
    _action = 3

    def __init__(self):
        pass
        self.pos = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.pos))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class OpenLevelBoxDown(object):
    _module = 4
    _action = 3

    def __init__(self):
        pass
        self.box_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.box_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class UseIngotReliveUp(object):
    _module = 4
    _action = 4

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 2
        

class UseIngotReliveDown(object):
    _module = 4
    _action = 4

    def __init__(self):
        pass
        self.ingot = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.ingot))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ingot = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class UseItemUp(object):
    _module = 4
    _action = 5

    def __init__(self):
        pass
        self.role_id = 0
        self.item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<h", self.item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 5
        

class UseItemDown(object):
    _module = 4
    _action = 5

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class RebuildDown(object):
    _module = 4
    _action = 6

    def __init__(self):
        pass
        self.level_type = 0
        self.level_id = 0
        self.relive_ingot = 0
        self.total_round = 0
        self.buddy_role_id = 0
        self.main_role_pos = 0
        self.buddy_pos = 0
        self.last_fighting_map = 0
        self.pass_ = []
        self.smallbox = []
        self.meng_yao = []
        self.shadow = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.level_type))
        buff.extend(struct.pack("<l", self.level_id))
        buff.extend(struct.pack("<l", self.relive_ingot))
        buff.extend(struct.pack("<h", self.total_round))
        buff.extend(struct.pack("<b", self.buddy_role_id))
        buff.extend(struct.pack("<b", self.main_role_pos))
        buff.extend(struct.pack("<b", self.buddy_pos))
        buff.extend(struct.pack("<l", self.last_fighting_map))
        buff.extend(struct.pack('<B', len(self.pass_)))
        for item in self.pass_:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.smallbox)))
        for item in self.smallbox:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.meng_yao)))
        for item in self.meng_yao:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.shadow)))
        for item in self.shadow:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.relive_ingot = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.total_round = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.buddy_role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.main_role_pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.buddy_pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.last_fighting_map = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        _pass__size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_pass__size):
            obj = RebuildDownPass()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.pass_.append(obj)

        _smallbox_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_smallbox_size):
            obj = RebuildDownSmallbox()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.smallbox.append(obj)

        _meng_yao_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_meng_yao_size):
            obj = RebuildDownMengYao()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.meng_yao.append(obj)

        _shadow_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_shadow_size):
            obj = RebuildDownShadow()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.shadow.append(obj)

    def size(self):
        size = 22
        for item in self.pass_:
            size += item.size()
        for item in self.smallbox:
            size += item.size()
        for item in self.meng_yao:
            size += item.size()
        for item in self.shadow:
            size += item.size()
        return size


class RebuildDownPass(object):
    def __init__(self):
        pass
        self.enemy_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.enemy_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.enemy_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class RebuildDownSmallbox(object):
    def __init__(self):
        pass
        self.box_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.box_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class RebuildDownMengYao(object):
    def __init__(self):
        pass
        self.my_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.my_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.my_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class RebuildDownShadow(object):
    def __init__(self):
        pass
        self.shaded_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.shaded_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.shaded_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class EnterExtendLevelUp(object):
    _module = 4
    _action = 7

    def __init__(self):
        pass
        self.level_type = 0
        self.level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.level_type))
        buff.extend(struct.pack("<l", self.level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 7
        

class EnterExtendLevelDown(object):
    _module = 4
    _action = 7

    def __init__(self):
        pass
        self.result = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class GetExtendLevelInfoUp(object):
    _module = 4
    _action = 8

    def __init__(self):
        pass
        self.level_type = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.level_type))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class GetExtendLevelInfoDown(object):
    _module = 4
    _action = 8

    def __init__(self):
        pass
        self.info = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.info)))
        for item in self.info:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _info_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_info_size):
            obj = GetExtendLevelInfoDownInfo()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.info.append(obj)

    def size(self):
        size = 1
        for item in self.info:
            size += item.size()
        return size


class GetExtendLevelInfoDownInfo(object):
    def __init__(self):
        pass
        self.level_type = 0
        self.level_sub_type = 0
        self.daily_num = 0
        self.max_level = 0
        self.buy_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.level_type))
        buff.extend(struct.pack("<B", self.level_sub_type))
        buff.extend(struct.pack("<b", self.daily_num))
        buff.extend(struct.pack("<h", self.max_level))
        buff.extend(struct.pack("<h", self.buy_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.level_sub_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.daily_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.max_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.buy_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 7
        

class OpenSmallBoxUp(object):
    _module = 4
    _action = 9

    def __init__(self):
        pass
        self.box_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.box_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class OpenSmallBoxDown(object):
    _module = 4
    _action = 9

    def __init__(self):
        pass
        self.items = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.items)))
        for item in self.items:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _items_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_items_size):
            obj = OpenSmallBoxDownItems()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.items.append(obj)

    def size(self):
        size = 1
        for item in self.items:
            size += item.size()
        return size


class OpenSmallBoxDownItems(object):
    def __init__(self):
        pass
        self.box_item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.box_item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_item_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class NotifyCatchBattlePetDown(object):
    _module = 4
    _action = 10

    def __init__(self):
        pass
        self.petId = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.petId))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.petId = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class EnterHardLevelUp(object):
    _module = 4
    _action = 11

    def __init__(self):
        pass
        self.level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class EnterHardLevelDown(object):
    _module = 4
    _action = 11

    def __init__(self):
        pass
        self.result = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class GetHardLevelUp(object):
    _module = 4
    _action = 12

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 2
        

class GetHardLevelDown(object):
    _module = 4
    _action = 12

    def __init__(self):
        pass
        self.levels = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.levels)))
        for item in self.levels:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _levels_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_levels_size):
            obj = GetHardLevelDownLevels()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.levels.append(obj)

    def size(self):
        size = 1
        for item in self.levels:
            size += item.size()
        return size


class GetHardLevelDownLevels(object):
    def __init__(self):
        pass
        self.level_id = 0
        self.daily_num = 0
        self.round_num = 0
        self.buy_times = 0
        self.remain_buy_times = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.level_id))
        buff.extend(struct.pack("<b", self.daily_num))
        buff.extend(struct.pack("<b", self.round_num))
        buff.extend(struct.pack("<h", self.buy_times))
        buff.extend(struct.pack("<h", self.remain_buy_times))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.daily_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.round_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.buy_times = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.remain_buy_times = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 10
        

class GetBuddyLevelRoleIdUp(object):
    _module = 4
    _action = 13

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 2
        

class GetBuddyLevelRoleIdDown(object):
    _module = 4
    _action = 13

    def __init__(self):
        pass
        self.role_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class SetBuddyLevelTeamUp(object):
    _module = 4
    _action = 14

    def __init__(self):
        pass
        self.role_pos = 0
        self.buddy_pos = 0
        self.tactical = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_pos))
        buff.extend(struct.pack("<b", self.buddy_pos))
        buff.extend(struct.pack("<b", self.tactical))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.buddy_pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.tactical = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 5
        

class SetBuddyLevelTeamDown(object):
    _module = 4
    _action = 14

    def __init__(self):
        pass
        self.result = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.result))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class AutoFightLevelUp(object):
    _module = 4
    _action = 15

    def __init__(self):
        pass
        self.level_type = 0
        self.level_id = 0
        self.times = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.level_type))
        buff.extend(struct.pack("<l", self.level_id))
        buff.extend(struct.pack("<b", self.times))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.times = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 8
        

class AutoFightLevelDown(object):
    _module = 4
    _action = 15

    def __init__(self):
        pass
        self.result = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.result)))
        for item in self.result:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _result_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_result_size):
            obj = AutoFightLevelDownResult()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.result.append(obj)

    def size(self):
        size = 1
        for item in self.result:
            size += item.size()
        return size


class AutoFightLevelDownResult(object):
    def __init__(self):
        pass
        self.level_box = []
        self.battle_pet = []
        self.small_box = []
        self.random_award_box = []
        self.addition_quest_item = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.level_box)))
        for item in self.level_box:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.battle_pet)))
        for item in self.battle_pet:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.small_box)))
        for item in self.small_box:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.random_award_box)))
        for item in self.random_award_box:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.addition_quest_item)))
        for item in self.addition_quest_item:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _level_box_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_level_box_size):
            obj = AutoFightLevelDownResultLevelBox()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.level_box.append(obj)

        _battle_pet_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_battle_pet_size):
            obj = AutoFightLevelDownResultBattlePet()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.battle_pet.append(obj)

        _small_box_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_small_box_size):
            obj = AutoFightLevelDownResultSmallBox()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.small_box.append(obj)

        _random_award_box_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_random_award_box_size):
            obj = AutoFightLevelDownResultRandomAwardBox()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.random_award_box.append(obj)

        _addition_quest_item_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_addition_quest_item_size):
            obj = AutoFightLevelDownResultAdditionQuestItem()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.addition_quest_item.append(obj)

    def size(self):
        size = 5
        for item in self.level_box:
            size += item.size()
        for item in self.battle_pet:
            size += item.size()
        for item in self.small_box:
            size += item.size()
        for item in self.random_award_box:
            size += item.size()
        for item in self.addition_quest_item:
            size += item.size()
        return size


class AutoFightLevelDownResultLevelBox(object):
    def __init__(self):
        pass
        self.box_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.box_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class AutoFightLevelDownResultBattlePet(object):
    def __init__(self):
        pass
        self.pet_id = 0
        self.catched = False
        self.consume_balls = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.pet_id))
        buff.extend(struct.pack("<?", self.catched))
        buff.extend(struct.pack("<b", self.consume_balls))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pet_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.catched = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.consume_balls = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 6
        

class AutoFightLevelDownResultSmallBox(object):
    def __init__(self):
        pass
        self.box_item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.box_item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_item_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class AutoFightLevelDownResultRandomAwardBox(object):
    def __init__(self):
        pass
        self.box_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.box_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class AutoFightLevelDownResultAdditionQuestItem(object):
    def __init__(self):
        pass
        self.item_id = 0
        self.item_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.item_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.item_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class EnterRainbowLevelUp(object):
    _module = 4
    _action = 16

    def __init__(self):
        pass
        self.mission_level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.mission_level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.mission_level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class EnterRainbowLevelDown(object):
    _module = 4
    _action = 16

    def __init__(self):
        pass
        self.used_ghost = []
        self.called_pet = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.used_ghost)))
        for item in self.used_ghost:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.called_pet)))
        for item in self.called_pet:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _used_ghost_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_used_ghost_size):
            obj = EnterRainbowLevelDownUsedGhost()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.used_ghost.append(obj)

        _called_pet_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_called_pet_size):
            obj = EnterRainbowLevelDownCalledPet()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.called_pet.append(obj)

    def size(self):
        size = 2
        for item in self.used_ghost:
            size += item.size()
        for item in self.called_pet:
            size += item.size()
        return size


class EnterRainbowLevelDownUsedGhost(object):
    def __init__(self):
        pass
        self.ghost_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.ghost_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ghost_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 2
        

class EnterRainbowLevelDownCalledPet(object):
    def __init__(self):
        pass
        self.pet_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.pet_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pet_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class OpenMengYaoUp(object):
    _module = 4
    _action = 17

    def __init__(self):
        pass
        self.meng_yao_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.meng_yao_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.meng_yao_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class OpenMengYaoDown(object):
    _module = 4
    _action = 17

    def __init__(self):
        pass
        self.meng_yao_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.meng_yao_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.meng_yao_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 4
        

class GetMissionLevelByItemIdUp(object):
    _module = 4
    _action = 18

    def __init__(self):
        pass
        self.item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class GetMissionLevelByItemIdDown(object):
    _module = 4
    _action = 18

    def __init__(self):
        pass
        self.levels = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.levels)))
        for item in self.levels:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _levels_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_levels_size):
            obj = GetMissionLevelByItemIdDownLevels()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.levels.append(obj)

    def size(self):
        size = 1
        for item in self.levels:
            size += item.size()
        return size


class GetMissionLevelByItemIdDownLevels(object):
    def __init__(self):
        pass
        self.level_id = 0
        self.round_num = 0
        self.daily_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.level_id))
        buff.extend(struct.pack("<b", self.round_num))
        buff.extend(struct.pack("<b", self.daily_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.round_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.daily_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 6
        

class BuyHardLevelTimesUp(object):
    _module = 4
    _action = 19

    def __init__(self):
        pass
        self.level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class BuyHardLevelTimesDown(object):
    _module = 4
    _action = 19

    def __init__(self):
        pass
        self.result = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class OpenRandomAwardBoxUp(object):
    _module = 4
    _action = 20

    def __init__(self):
        pass
        self.level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class OpenRandomAwardBoxDown(object):
    _module = 4
    _action = 20

    def __init__(self):
        pass
        self.box_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.box_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class EvaluateLevelUp(object):
    _module = 4
    _action = 21

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 2
        

class EvaluateLevelDown(object):
    _module = 4
    _action = 21

    def __init__(self):
        pass
        self.additional_quest_items = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.additional_quest_items)))
        for item in self.additional_quest_items:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _additional_quest_items_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_additional_quest_items_size):
            obj = EvaluateLevelDownAdditionalQuestItems()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.additional_quest_items.append(obj)

    def size(self):
        size = 1
        for item in self.additional_quest_items:
            size += item.size()
        return size


class EvaluateLevelDownAdditionalQuestItems(object):
    def __init__(self):
        pass
        self.item_id = 0
        self.item_cnt = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.item_cnt))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.item_cnt = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class OpenShadedBoxUp(object):
    _module = 4
    _action = 22

    def __init__(self):
        pass
        self.shaded_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.shaded_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.shaded_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class OpenShadedBoxDown(object):
    _module = 4
    _action = 22

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class GetMissionTotalStarInfoUp(object):
    _module = 4
    _action = 23

    def __init__(self):
        pass
        self.town_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.town_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.town_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class GetMissionTotalStarInfoDown(object):
    _module = 4
    _action = 23

    def __init__(self):
        pass
        self.town_id = 0
        self.total_star = 0
        self.box_type_list = []
        self.missionstars = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.town_id))
        buff.extend(struct.pack("<h", self.total_star))
        buff.extend(struct.pack('<B', len(self.box_type_list)))
        for item in self.box_type_list:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.missionstars)))
        for item in self.missionstars:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.town_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.total_star = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        _box_type_list_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_box_type_list_size):
            obj = GetMissionTotalStarInfoDownBoxTypeList()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.box_type_list.append(obj)

        _missionstars_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_missionstars_size):
            obj = GetMissionTotalStarInfoDownMissionstars()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.missionstars.append(obj)

    def size(self):
        size = 6
        for item in self.box_type_list:
            size += item.size()
        for item in self.missionstars:
            size += item.size()
        return size


class GetMissionTotalStarInfoDownBoxTypeList(object):
    def __init__(self):
        pass
        self.box_type = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.box_type))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.box_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class GetMissionTotalStarInfoDownMissionstars(object):
    def __init__(self):
        pass
        self.missionid = 0
        self.stars = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.missionid))
        buff.extend(struct.pack("<h", self.stars))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.missionid = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.stars = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class GetMissionTotalStarAwardsUp(object):
    _module = 4
    _action = 24

    def __init__(self):
        pass
        self.town_id = 0
        self.box_type = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.town_id))
        buff.extend(struct.pack("<b", self.box_type))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.town_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.box_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 5
        

class GetMissionTotalStarAwardsDown(object):
    _module = 4
    _action = 24

    def __init__(self):
        pass
        self.town_id = 0
        self.box_type = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.town_id))
        buff.extend(struct.pack("<b", self.box_type))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.town_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.box_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class ClearMissionLevelStateUp(object):
    _module = 4
    _action = 25

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 2
        

class ClearMissionLevelStateDown(object):
    _module = 4
    _action = 25

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class BuyResourceMissionLevelTimesUp(object):
    _module = 4
    _action = 26

    def __init__(self):
        pass
        self.sub_type = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.sub_type))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.sub_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class BuyResourceMissionLevelTimesDown(object):
    _module = 4
    _action = 26

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class BuyBossLevelTimesUp(object):
    _module = 4
    _action = 27

    def __init__(self):
        pass
        self.level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class BuyBossLevelTimesDown(object):
    _module = 4
    _action = 27

    def __init__(self):
        pass
        self.result = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class MissionModule(interface.BaseModule):
    decoder_map = {
        0: OpenDown, 
        1: GetMissionLevelDown, 
        2: EnterLevelDown, 
        3: OpenLevelBoxDown, 
        4: UseIngotReliveDown, 
        5: UseItemDown, 
        6: RebuildDown, 
        7: EnterExtendLevelDown, 
        8: GetExtendLevelInfoDown, 
        9: OpenSmallBoxDown, 
        10: NotifyCatchBattlePetDown, 
        11: EnterHardLevelDown, 
        12: GetHardLevelDown, 
        13: GetBuddyLevelRoleIdDown, 
        14: SetBuddyLevelTeamDown, 
        15: AutoFightLevelDown, 
        16: EnterRainbowLevelDown, 
        17: OpenMengYaoDown, 
        18: GetMissionLevelByItemIdDown, 
        19: BuyHardLevelTimesDown, 
        20: OpenRandomAwardBoxDown, 
        21: EvaluateLevelDown, 
        22: OpenShadedBoxDown, 
        23: GetMissionTotalStarInfoDown, 
        24: GetMissionTotalStarAwardsDown, 
        25: ClearMissionLevelStateDown, 
        26: BuyResourceMissionLevelTimesDown, 
        27: BuyBossLevelTimesDown, 
    }
    receive_callback = {}

    def decode(self, message):
        action = ord(message[0])
        decoder_maker = self.decoder_map[action]
        msg = decoder_maker()
        msg.decode(message[1:])
        return msg

    def add_callback(self, action, callback):
        if self.receive_callback.has_key(action):
            self.receive_callback[action].append(callback)
        else:
            self.receive_callback[action] = [callback,]

    def clear_callback(self):
        self.receive_callback = {}

    def add_open(self, callback):
        self.add_callback(0, callback)

    def add_get_mission_level(self, callback):
        self.add_callback(1, callback)

    def add_enter_level(self, callback):
        self.add_callback(2, callback)

    def add_open_level_box(self, callback):
        self.add_callback(3, callback)

    def add_use_ingot_relive(self, callback):
        self.add_callback(4, callback)

    def add_use_item(self, callback):
        self.add_callback(5, callback)

    def add_rebuild(self, callback):
        self.add_callback(6, callback)

    def add_enter_extend_level(self, callback):
        self.add_callback(7, callback)

    def add_get_extend_level_info(self, callback):
        self.add_callback(8, callback)

    def add_open_small_box(self, callback):
        self.add_callback(9, callback)

    def add_notify_catch_battle_pet(self, callback):
        self.add_callback(10, callback)

    def add_enter_hard_level(self, callback):
        self.add_callback(11, callback)

    def add_get_hard_level(self, callback):
        self.add_callback(12, callback)

    def add_get_buddy_level_role_id(self, callback):
        self.add_callback(13, callback)

    def add_set_buddy_level_team(self, callback):
        self.add_callback(14, callback)

    def add_auto_fight_level(self, callback):
        self.add_callback(15, callback)

    def add_enter_rainbow_level(self, callback):
        self.add_callback(16, callback)

    def add_open_meng_yao(self, callback):
        self.add_callback(17, callback)

    def add_get_mission_level_by_item_id(self, callback):
        self.add_callback(18, callback)

    def add_buy_hard_level_times(self, callback):
        self.add_callback(19, callback)

    def add_open_random_award_box(self, callback):
        self.add_callback(20, callback)

    def add_evaluate_level(self, callback):
        self.add_callback(21, callback)

    def add_open_shaded_box(self, callback):
        self.add_callback(22, callback)

    def add_get_mission_total_star_info(self, callback):
        self.add_callback(23, callback)

    def add_get_mission_total_star_awards(self, callback):
        self.add_callback(24, callback)

    def add_clear_mission_level_state(self, callback):
        self.add_callback(25, callback)

    def add_buy_resource_mission_level_times(self, callback):
        self.add_callback(26, callback)

    def add_buy_boss_level_times(self, callback):
        self.add_callback(27, callback)
