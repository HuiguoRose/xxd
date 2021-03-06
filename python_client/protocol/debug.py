#!/usr/bin/evn python
#  -*- coding: utf8 -*-

import struct

import interface

class AddBuddyUp(object):
    _module = 99
    _action = 0

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
        return 3
        

class AddBuddyDown(object):
    _module = 99
    _action = 0

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
        

class AddItemUp(object):
    _module = 99
    _action = 2

    def __init__(self):
        pass
        self.item_id = 0
        self.number = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.number))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.number = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 6
        

class AddItemDown(object):
    _module = 99
    _action = 2

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
        

class SetRoleLevelUp(object):
    _module = 99
    _action = 3

    def __init__(self):
        pass
        self.role_id = 0
        self.level = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<h", self.level))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 5
        

class SetRoleLevelDown(object):
    _module = 99
    _action = 3

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
        

class SetCoinsUp(object):
    _module = 99
    _action = 4

    def __init__(self):
        pass
        self.number = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.number))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.number = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class SetCoinsDown(object):
    _module = 99
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
        return 0
        

class SetIngotUp(object):
    _module = 99
    _action = 5

    def __init__(self):
        pass
        self.number = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.number))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.number = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class SetIngotDown(object):
    _module = 99
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
        

class AddGhostUp(object):
    _module = 99
    _action = 11

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
        return 4
        

class AddGhostDown(object):
    _module = 99
    _action = 11

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
        

class SetPlayerPhysicalUp(object):
    _module = 99
    _action = 12

    def __init__(self):
        pass
        self.physical = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.physical))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.physical = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class SetPlayerPhysicalDown(object):
    _module = 99
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
        return 0
        

class ResetLevelEnterCountUp(object):
    _module = 99
    _action = 13

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
        

class ResetLevelEnterCountDown(object):
    _module = 99
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
        return 0
        

class AddExpUp(object):
    _module = 99
    _action = 14

    def __init__(self):
        pass
        self.role_id = 0
        self.add_exp = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<q", self.add_exp))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.add_exp = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 11
        

class AddExpDown(object):
    _module = 99
    _action = 14

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
        

class OpenGhostMissionUp(object):
    _module = 99
    _action = 15

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
        

class OpenGhostMissionDown(object):
    _module = 99
    _action = 15

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
        

class SendMailUp(object):
    _module = 99
    _action = 16

    def __init__(self):
        pass
        self.mail_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.mail_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.mail_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class SendMailDown(object):
    _module = 99
    _action = 16

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
        

class ClearMailUp(object):
    _module = 99
    _action = 17

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
        

class ClearMailDown(object):
    _module = 99
    _action = 17

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
        

class OpenMissionLevelUp(object):
    _module = 99
    _action = 18

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
        

class OpenMissionLevelDown(object):
    _module = 99
    _action = 18

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
        

class StartBattleUp(object):
    _module = 99
    _action = 19

    def __init__(self):
        pass
        self.battle_type = 0
        self.enemy_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.battle_type))
        buff.extend(struct.pack("<l", self.enemy_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.battle_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.enemy_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 7
        

class StartBattleDown(object):
    _module = 99
    _action = 19

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
        

class ListenByNameUp(object):
    _module = 99
    _action = 20

    def __init__(self):
        pass
        self.name = ''

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<H', len(self.name)))
        buff.extend(self.name)
        return buff

    def decode(self, raw_msg):
        idx = 0

        _name_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.name = str(raw_msg[idx:idx+_name_size])
        idx += _name_size

    def size(self):
        size = 4
        size += len(self.name)
        return size


class ListenByNameDown(object):
    _module = 99
    _action = 20

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
        

class OpenQuestUp(object):
    _module = 99
    _action = 21

    def __init__(self):
        pass
        self.quest_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.quest_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.quest_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class OpenQuestDown(object):
    _module = 99
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
        return 0
        

class OpenFuncUp(object):
    _module = 99
    _action = 22

    def __init__(self):
        pass
        self.lock = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.lock))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.lock = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class OpenFuncDown(object):
    _module = 99
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
        

class AddSwordSoulUp(object):
    _module = 99
    _action = 23

    def __init__(self):
        pass
        self.sword_soul_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.sword_soul_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.sword_soul_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class AddSwordSoulDown(object):
    _module = 99
    _action = 23

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
        

class AddBattlePetUp(object):
    _module = 99
    _action = 25

    def __init__(self):
        pass
        self.petId = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.petId))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.petId = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class AddBattlePetDown(object):
    _module = 99
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
        

class ResetMultiLevelEnterCountUp(object):
    _module = 99
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
        return 2
        

class ResetMultiLevelEnterCountDown(object):
    _module = 99
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
        

class OpenMultiLevelUp(object):
    _module = 99
    _action = 27

    def __init__(self):
        pass
        self.level_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.level_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class OpenMultiLevelDown(object):
    _module = 99
    _action = 27

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
        

class OpenAllPetGridUp(object):
    _module = 99
    _action = 28

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
        

class OpenAllPetGridDown(object):
    _module = 99
    _action = 28

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
        

class CreateAnnouncementUp(object):
    _module = 99
    _action = 29

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
        

class CreateAnnouncementDown(object):
    _module = 99
    _action = 29

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
        

class AddHeartUp(object):
    _module = 99
    _action = 30

    def __init__(self):
        pass
        self.number = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.number))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.number = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class AddHeartDown(object):
    _module = 99
    _action = 30

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
        

class ResetHardLevelEnterCountUp(object):
    _module = 99
    _action = 31

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
        

class ResetHardLevelEnterCountDown(object):
    _module = 99
    _action = 31

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
        

class OpenHardLevelUp(object):
    _module = 99
    _action = 32

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
        

class OpenHardLevelDown(object):
    _module = 99
    _action = 32

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
        

class SetVipLevelUp(object):
    _module = 99
    _action = 33

    def __init__(self):
        pass
        self.level = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.level))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class SetVipLevelDown(object):
    _module = 99
    _action = 33

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
        

class SetResourceLevelOpenDayUp(object):
    _module = 99
    _action = 34

    def __init__(self):
        pass
        self.level_type = 0
        self.open_day = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.level_type))
        buff.extend(struct.pack("<b", self.open_day))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.level_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.open_day = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 4
        

class SetResourceLevelOpenDayDown(object):
    _module = 99
    _action = 34

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
        

class ResetResourceLevelOpenDayUp(object):
    _module = 99
    _action = 35

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
        

class ResetResourceLevelOpenDayDown(object):
    _module = 99
    _action = 35

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
        

class ResetArenaDailyCountUp(object):
    _module = 99
    _action = 36

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
        

class ResetArenaDailyCountDown(object):
    _module = 99
    _action = 36

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
        

class ResetSwordSoulDrawCdUp(object):
    _module = 99
    _action = 37

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
        

class ResetSwordSoulDrawCdDown(object):
    _module = 99
    _action = 37

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
        

class SetFirstLoginTimeUp(object):
    _module = 99
    _action = 38

    def __init__(self):
        pass
        self.timestamp = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.timestamp))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.timestamp = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class SetFirstLoginTimeDown(object):
    _module = 99
    _action = 38

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
        

class EarlierFirstLoginTimeUp(object):
    _module = 99
    _action = 39

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
        

class EarlierFirstLoginTimeDown(object):
    _module = 99
    _action = 39

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
        

class ResetServerOpenTimeUp(object):
    _module = 99
    _action = 40

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
        

class ResetServerOpenTimeDown(object):
    _module = 99
    _action = 40

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
        

class ClearTraderRefreshTimeUp(object):
    _module = 99
    _action = 41

    def __init__(self):
        pass
        self.trader_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.trader_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.trader_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class ClearTraderRefreshTimeDown(object):
    _module = 99
    _action = 41

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
        

class AddTraderRefreshTimeUp(object):
    _module = 99
    _action = 42

    def __init__(self):
        pass
        self.trader_id = 0
        self.timing = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.trader_id))
        buff.extend(struct.pack("<q", self.timing))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.trader_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.timing = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 12
        

class AddTraderRefreshTimeDown(object):
    _module = 99
    _action = 42

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
        

class ClearTraderScheduleUp(object):
    _module = 99
    _action = 43

    def __init__(self):
        pass
        self.trader_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.trader_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.trader_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class ClearTraderScheduleDown(object):
    _module = 99
    _action = 43

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
        

class AddTraderScheduleUp(object):
    _module = 99
    _action = 44

    def __init__(self):
        pass
        self.trader_id = 0
        self.expire = 0
        self.showup = 0
        self.disappear = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.trader_id))
        buff.extend(struct.pack("<q", self.expire))
        buff.extend(struct.pack("<q", self.showup))
        buff.extend(struct.pack("<q", self.disappear))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.trader_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.expire = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.showup = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.disappear = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 28
        

class AddTraderScheduleDown(object):
    _module = 99
    _action = 44

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
        

class OpenTownUp(object):
    _module = 99
    _action = 45

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
        

class OpenTownDown(object):
    _module = 99
    _action = 45

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
        

class AddGlobalMailUp(object):
    _module = 99
    _action = 46

    def __init__(self):
        pass
        self.send_delay = 0
        self.expire_delay = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.send_delay))
        buff.extend(struct.pack("<q", self.expire_delay))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.send_delay = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.expire_delay = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 18
        

class AddGlobalMailDown(object):
    _module = 99
    _action = 46

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
        

class CreateAnnouncementWithoutTplUp(object):
    _module = 99
    _action = 47

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
        

class CreateAnnouncementWithoutTplDown(object):
    _module = 99
    _action = 47

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
        

class SetLoginDayUp(object):
    _module = 99
    _action = 48

    def __init__(self):
        pass
        self.days = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.days))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.days = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class SetLoginDayDown(object):
    _module = 99
    _action = 48

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
        

class ResetLoginAwardUp(object):
    _module = 99
    _action = 49

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
        

class ResetLoginAwardDown(object):
    _module = 99
    _action = 49

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
        

class RestPlayerAwardLockUp(object):
    _module = 99
    _action = 50

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
        

class RestPlayerAwardLockDown(object):
    _module = 99
    _action = 50

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
        

class ResetRainbowLevelUp(object):
    _module = 99
    _action = 51

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
        

class ResetRainbowLevelDown(object):
    _module = 99
    _action = 51

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
        

class SetRainbowLevelUp(object):
    _module = 99
    _action = 52

    def __init__(self):
        pass
        self.segment = 0
        self.order = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.segment))
        buff.extend(struct.pack("<b", self.order))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.segment = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.order = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 5
        

class SetRainbowLevelDown(object):
    _module = 99
    _action = 52

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
        

class SendPushNotificationUp(object):
    _module = 99
    _action = 53

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
        

class SendPushNotificationDown(object):
    _module = 99
    _action = 53

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
        

class ResetPetVirtualEnvUp(object):
    _module = 99
    _action = 54

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
        

class ResetPetVirtualEnvDown(object):
    _module = 99
    _action = 54

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
        

class AddFameUp(object):
    _module = 99
    _action = 55

    def __init__(self):
        pass
        self.system = 0
        self.val = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.system))
        buff.extend(struct.pack("<l", self.val))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.system = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.val = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 8
        

class AddFameDown(object):
    _module = 99
    _action = 55

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
        

class AddWorldChatMessageUp(object):
    _module = 99
    _action = 56

    def __init__(self):
        pass
        self.num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class AddWorldChatMessageDown(object):
    _module = 99
    _action = 56

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
        

class MonthCardUp(object):
    _module = 99
    _action = 57

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
        

class MonthCardDown(object):
    _module = 99
    _action = 57

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
        

class EnterSandboxUp(object):
    _module = 99
    _action = 58

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
        

class EnterSandboxDown(object):
    _module = 99
    _action = 58

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
        

class SandboxRollbackUp(object):
    _module = 99
    _action = 59

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
        

class SandboxRollbackDown(object):
    _module = 99
    _action = 59

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
        

class ExitSandboxUp(object):
    _module = 99
    _action = 60

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
        

class ExitSandboxDown(object):
    _module = 99
    _action = 60

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
        

class ResetShadedMissionsUp(object):
    _module = 99
    _action = 61

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
        

class ResetShadedMissionsDown(object):
    _module = 99
    _action = 61

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
        

class CleanCornucopiaUp(object):
    _module = 99
    _action = 62

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
        

class CleanCornucopiaDown(object):
    _module = 99
    _action = 62

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
        

class AddTotemUp(object):
    _module = 99
    _action = 63

    def __init__(self):
        pass
        self.totem_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.totem_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.totem_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class AddTotemDown(object):
    _module = 99
    _action = 63

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
        

class AddRuneUp(object):
    _module = 99
    _action = 64

    def __init__(self):
        pass
        self.jade_num = 0
        self.rock_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.jade_num))
        buff.extend(struct.pack("<l", self.rock_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.jade_num = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.rock_num = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 10
        

class AddRuneDown(object):
    _module = 99
    _action = 64

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
        

class SendRareItemMessageUp(object):
    _module = 99
    _action = 65

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
        

class SendRareItemMessageDown(object):
    _module = 99
    _action = 65

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
        

class AddSwordDrivingActionUp(object):
    _module = 99
    _action = 66

    def __init__(self):
        pass
        self.point = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.point))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.point = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class AddSwordDrivingActionDown(object):
    _module = 99
    _action = 66

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
        

class ResetDrivingSwordDataUp(object):
    _module = 99
    _action = 67

    def __init__(self):
        pass
        self.cloud = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.cloud))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.cloud = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class ResetDrivingSwordDataDown(object):
    _module = 99
    _action = 67

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
        

class AddSwordSoulFragmentUp(object):
    _module = 99
    _action = 68

    def __init__(self):
        pass
        self.number = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.number))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.number = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class AddSwordSoulFragmentDown(object):
    _module = 99
    _action = 68

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
        

class ResetMoneyTreeStatusUp(object):
    _module = 99
    _action = 69

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
        

class ResetMoneyTreeStatusDown(object):
    _module = 99
    _action = 69

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
        

class ResetTodayMoneyTreeUp(object):
    _module = 99
    _action = 70

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
        

class ResetTodayMoneyTreeDown(object):
    _module = 99
    _action = 70

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
        

class CleanSwordSoulIngotDrawNumsUp(object):
    _module = 99
    _action = 71

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
        

class CleanSwordSoulIngotDrawNumsDown(object):
    _module = 99
    _action = 71

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
        

class PunchDrivingSwordCloudUp(object):
    _module = 99
    _action = 72

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
        

class PunchDrivingSwordCloudDown(object):
    _module = 99
    _action = 72

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
        

class ClearCliqueDailyDonateUp(object):
    _module = 99
    _action = 73

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
        

class ClearCliqueDailyDonateDown(object):
    _module = 99
    _action = 73

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
        

class SetCliqueContribUp(object):
    _module = 99
    _action = 74

    def __init__(self):
        pass
        self.contrib = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.contrib))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.contrib = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class SetCliqueContribDown(object):
    _module = 99
    _action = 74

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
        

class RefreshCliqueWorshipUp(object):
    _module = 99
    _action = 75

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
        

class RefreshCliqueWorshipDown(object):
    _module = 99
    _action = 75

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
        

class CliqueEscortHijackBattleWinUp(object):
    _module = 99
    _action = 76

    def __init__(self):
        pass
        self.boat_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.boat_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.boat_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class CliqueEscortHijackBattleWinDown(object):
    _module = 99
    _action = 76

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
        

class CliqueEscortRecoverBattleWinUp(object):
    _module = 99
    _action = 77

    def __init__(self):
        pass
        self.boat_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.boat_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.boat_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class CliqueEscortRecoverBattleWinDown(object):
    _module = 99
    _action = 77

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
        

class CliqueEscortNotifyMessageUp(object):
    _module = 99
    _action = 87

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
        

class CliqueEscortNotifyMessageDown(object):
    _module = 99
    _action = 87

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
        

class CliqueEscortNotifyDailyQuestUp(object):
    _module = 99
    _action = 88

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
        

class CliqueEscortNotifyDailyQuestDown(object):
    _module = 99
    _action = 88

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
        

class SetCliqueBuildingLevelUp(object):
    _module = 99
    _action = 89

    def __init__(self):
        pass
        self.building = 0
        self.level = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.building))
        buff.extend(struct.pack("<h", self.level))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.building = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 8
        

class SetCliqueBuildingLevelDown(object):
    _module = 99
    _action = 89

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
        

class SetCliqueBuildingMoneyUp(object):
    _module = 99
    _action = 90

    def __init__(self):
        pass
        self.building = 0
        self.money = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.building))
        buff.extend(struct.pack("<q", self.money))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.building = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.money = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 14
        

class SetCliqueBuildingMoneyDown(object):
    _module = 99
    _action = 90

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
        

class EscortBenchUp(object):
    _module = 99
    _action = 91

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
        

class EscortBenchDown(object):
    _module = 99
    _action = 91

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
        

class ResetCliqueEscortDailyNumUp(object):
    _module = 99
    _action = 92

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
        

class ResetCliqueEscortDailyNumDown(object):
    _module = 99
    _action = 92

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
        

class TakeAdditionQuestUp(object):
    _module = 99
    _action = 93

    def __init__(self):
        pass
        self.first_quest_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.first_quest_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.first_quest_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class TakeAdditionQuestDown(object):
    _module = 99
    _action = 93

    def __init__(self):
        pass
        self.msg = ''

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<H', len(self.msg)))
        buff.extend(self.msg)
        return buff

    def decode(self, raw_msg):
        idx = 0

        _msg_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.msg = str(raw_msg[idx:idx+_msg_size])
        idx += _msg_size

    def size(self):
        size = 2
        size += len(self.msg)
        return size


class SetMissionStarMaxUp(object):
    _module = 99
    _action = 94

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
        

class SetMissionStarMaxDown(object):
    _module = 99
    _action = 94

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
        

class CliqueBankCdUp(object):
    _module = 99
    _action = 95

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
        

class CliqueBankCdDown(object):
    _module = 99
    _action = 95

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
        

class CleanRechargeInfoUp(object):
    _module = 99
    _action = 96

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
        

class CleanRechargeInfoDown(object):
    _module = 99
    _action = 96

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
        

class DebugModule(interface.BaseModule):
    decoder_map = {
        0: AddBuddyDown, 
        2: AddItemDown, 
        3: SetRoleLevelDown, 
        4: SetCoinsDown, 
        5: SetIngotDown, 
        11: AddGhostDown, 
        12: SetPlayerPhysicalDown, 
        13: ResetLevelEnterCountDown, 
        14: AddExpDown, 
        15: OpenGhostMissionDown, 
        16: SendMailDown, 
        17: ClearMailDown, 
        18: OpenMissionLevelDown, 
        19: StartBattleDown, 
        20: ListenByNameDown, 
        21: OpenQuestDown, 
        22: OpenFuncDown, 
        23: AddSwordSoulDown, 
        25: AddBattlePetDown, 
        26: ResetMultiLevelEnterCountDown, 
        27: OpenMultiLevelDown, 
        28: OpenAllPetGridDown, 
        29: CreateAnnouncementDown, 
        30: AddHeartDown, 
        31: ResetHardLevelEnterCountDown, 
        32: OpenHardLevelDown, 
        33: SetVipLevelDown, 
        34: SetResourceLevelOpenDayDown, 
        35: ResetResourceLevelOpenDayDown, 
        36: ResetArenaDailyCountDown, 
        37: ResetSwordSoulDrawCdDown, 
        38: SetFirstLoginTimeDown, 
        39: EarlierFirstLoginTimeDown, 
        40: ResetServerOpenTimeDown, 
        41: ClearTraderRefreshTimeDown, 
        42: AddTraderRefreshTimeDown, 
        43: ClearTraderScheduleDown, 
        44: AddTraderScheduleDown, 
        45: OpenTownDown, 
        46: AddGlobalMailDown, 
        47: CreateAnnouncementWithoutTplDown, 
        48: SetLoginDayDown, 
        49: ResetLoginAwardDown, 
        50: RestPlayerAwardLockDown, 
        51: ResetRainbowLevelDown, 
        52: SetRainbowLevelDown, 
        53: SendPushNotificationDown, 
        54: ResetPetVirtualEnvDown, 
        55: AddFameDown, 
        56: AddWorldChatMessageDown, 
        57: MonthCardDown, 
        58: EnterSandboxDown, 
        59: SandboxRollbackDown, 
        60: ExitSandboxDown, 
        61: ResetShadedMissionsDown, 
        62: CleanCornucopiaDown, 
        63: AddTotemDown, 
        64: AddRuneDown, 
        65: SendRareItemMessageDown, 
        66: AddSwordDrivingActionDown, 
        67: ResetDrivingSwordDataDown, 
        68: AddSwordSoulFragmentDown, 
        69: ResetMoneyTreeStatusDown, 
        70: ResetTodayMoneyTreeDown, 
        71: CleanSwordSoulIngotDrawNumsDown, 
        72: PunchDrivingSwordCloudDown, 
        73: ClearCliqueDailyDonateDown, 
        74: SetCliqueContribDown, 
        75: RefreshCliqueWorshipDown, 
        76: CliqueEscortHijackBattleWinDown, 
        77: CliqueEscortRecoverBattleWinDown, 
        87: CliqueEscortNotifyMessageDown, 
        88: CliqueEscortNotifyDailyQuestDown, 
        89: SetCliqueBuildingLevelDown, 
        90: SetCliqueBuildingMoneyDown, 
        91: EscortBenchDown, 
        92: ResetCliqueEscortDailyNumDown, 
        93: TakeAdditionQuestDown, 
        94: SetMissionStarMaxDown, 
        95: CliqueBankCdDown, 
        96: CleanRechargeInfoDown, 
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

    def add_add_buddy(self, callback):
        self.add_callback(0, callback)

    def add_add_item(self, callback):
        self.add_callback(2, callback)

    def add_set_role_level(self, callback):
        self.add_callback(3, callback)

    def add_set_coins(self, callback):
        self.add_callback(4, callback)

    def add_set_ingot(self, callback):
        self.add_callback(5, callback)

    def add_add_ghost(self, callback):
        self.add_callback(11, callback)

    def add_set_player_physical(self, callback):
        self.add_callback(12, callback)

    def add_reset_level_enter_count(self, callback):
        self.add_callback(13, callback)

    def add_add_exp(self, callback):
        self.add_callback(14, callback)

    def add_open_ghost_mission(self, callback):
        self.add_callback(15, callback)

    def add_send_mail(self, callback):
        self.add_callback(16, callback)

    def add_clear_mail(self, callback):
        self.add_callback(17, callback)

    def add_open_mission_level(self, callback):
        self.add_callback(18, callback)

    def add_start_battle(self, callback):
        self.add_callback(19, callback)

    def add_listen_by_name(self, callback):
        self.add_callback(20, callback)

    def add_open_quest(self, callback):
        self.add_callback(21, callback)

    def add_open_func(self, callback):
        self.add_callback(22, callback)

    def add_add_sword_soul(self, callback):
        self.add_callback(23, callback)

    def add_add_battle_pet(self, callback):
        self.add_callback(25, callback)

    def add_reset_multi_level_enter_count(self, callback):
        self.add_callback(26, callback)

    def add_open_multi_level(self, callback):
        self.add_callback(27, callback)

    def add_open_all_pet_grid(self, callback):
        self.add_callback(28, callback)

    def add_create_announcement(self, callback):
        self.add_callback(29, callback)

    def add_add_heart(self, callback):
        self.add_callback(30, callback)

    def add_reset_hard_level_enter_count(self, callback):
        self.add_callback(31, callback)

    def add_open_hard_level(self, callback):
        self.add_callback(32, callback)

    def add_set_vip_level(self, callback):
        self.add_callback(33, callback)

    def add_set_resource_level_open_day(self, callback):
        self.add_callback(34, callback)

    def add_reset_resource_level_open_day(self, callback):
        self.add_callback(35, callback)

    def add_reset_arena_daily_count(self, callback):
        self.add_callback(36, callback)

    def add_reset_sword_soul_draw_cd(self, callback):
        self.add_callback(37, callback)

    def add_set_first_login_time(self, callback):
        self.add_callback(38, callback)

    def add_earlier_first_login_time(self, callback):
        self.add_callback(39, callback)

    def add_reset_server_open_time(self, callback):
        self.add_callback(40, callback)

    def add_clear_trader_refresh_time(self, callback):
        self.add_callback(41, callback)

    def add_add_trader_refresh_time(self, callback):
        self.add_callback(42, callback)

    def add_clear_trader_schedule(self, callback):
        self.add_callback(43, callback)

    def add_add_trader_schedule(self, callback):
        self.add_callback(44, callback)

    def add_open_town(self, callback):
        self.add_callback(45, callback)

    def add_add_global_mail(self, callback):
        self.add_callback(46, callback)

    def add_create_announcement_without_tpl(self, callback):
        self.add_callback(47, callback)

    def add_set_login_day(self, callback):
        self.add_callback(48, callback)

    def add_reset_login_award(self, callback):
        self.add_callback(49, callback)

    def add_rest_player_award_lock(self, callback):
        self.add_callback(50, callback)

    def add_reset_rainbow_level(self, callback):
        self.add_callback(51, callback)

    def add_set_rainbow_level(self, callback):
        self.add_callback(52, callback)

    def add_send_push_notification(self, callback):
        self.add_callback(53, callback)

    def add_reset_pet_virtual_env(self, callback):
        self.add_callback(54, callback)

    def add_add_fame(self, callback):
        self.add_callback(55, callback)

    def add_add_world_chat_message(self, callback):
        self.add_callback(56, callback)

    def add_month_card(self, callback):
        self.add_callback(57, callback)

    def add_enter_sandbox(self, callback):
        self.add_callback(58, callback)

    def add_sandbox_rollback(self, callback):
        self.add_callback(59, callback)

    def add_exit_sandbox(self, callback):
        self.add_callback(60, callback)

    def add_reset_shaded_missions(self, callback):
        self.add_callback(61, callback)

    def add_clean_cornucopia(self, callback):
        self.add_callback(62, callback)

    def add_add_totem(self, callback):
        self.add_callback(63, callback)

    def add_add_rune(self, callback):
        self.add_callback(64, callback)

    def add_send_rare_item_message(self, callback):
        self.add_callback(65, callback)

    def add_add_sword_driving_action(self, callback):
        self.add_callback(66, callback)

    def add_reset_driving_sword_data(self, callback):
        self.add_callback(67, callback)

    def add_add_sword_soul_fragment(self, callback):
        self.add_callback(68, callback)

    def add_reset_money_tree_status(self, callback):
        self.add_callback(69, callback)

    def add_reset_today_money_tree(self, callback):
        self.add_callback(70, callback)

    def add_clean_sword_soul_ingot_draw_nums(self, callback):
        self.add_callback(71, callback)

    def add_punch_driving_sword_cloud(self, callback):
        self.add_callback(72, callback)

    def add_clear_clique_daily_donate(self, callback):
        self.add_callback(73, callback)

    def add_set_clique_contrib(self, callback):
        self.add_callback(74, callback)

    def add_refresh_clique_worship(self, callback):
        self.add_callback(75, callback)

    def add_clique_escort_hijack_battle_win(self, callback):
        self.add_callback(76, callback)

    def add_clique_escort_recover_battle_win(self, callback):
        self.add_callback(77, callback)

    def add_clique_escort_notify_message(self, callback):
        self.add_callback(87, callback)

    def add_clique_escort_notify_daily_quest(self, callback):
        self.add_callback(88, callback)

    def add_set_clique_building_level(self, callback):
        self.add_callback(89, callback)

    def add_set_clique_building_money(self, callback):
        self.add_callback(90, callback)

    def add_escort_bench(self, callback):
        self.add_callback(91, callback)

    def add_reset_clique_escort_daily_num(self, callback):
        self.add_callback(92, callback)

    def add_take_addition_quest(self, callback):
        self.add_callback(93, callback)

    def add_set_mission_star_max(self, callback):
        self.add_callback(94, callback)

    def add_clique_bank_cd(self, callback):
        self.add_callback(95, callback)

    def add_clean_recharge_info(self, callback):
        self.add_callback(96, callback)
