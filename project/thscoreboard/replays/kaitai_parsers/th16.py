# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Th16(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Th16.Header(self._io, self, self._root)
        self.stages = []
        for i in range(self.header.stage_count):
            self.stages.append(Th16.Stage(self._io, self, self._root))


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(12), 0, False)).decode(u"ASCII")
            self.timestamp = self._io.read_u8le()
            self.score = self._io.read_u4le()
            self.unknown_1 = self._io.read_bytes(100)
            self.slowdown = self._io.read_f4le()
            self.stage_count = self._io.read_u4le()
            self.shot = self._io.read_u4le()
            self.subshot_unused = self._io.read_u4le()
            self.difficulty = self._io.read_u4le()
            self.cleared = self._io.read_u4le()
            self.unknown_2 = self._io.read_u4le()
            self.spell_practice_id = self._io.read_u4le()
            self.season = self._io.read_u4le()


    class Stage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.stage_num = self._io.read_u2le()
            self.rng = self._io.read_u2le()
            self.frame_count = self._io.read_u4le()
            self.end_off = self._io.read_u4le()
            self.pos_subpixel_x = self._io.read_u4le()
            self.pos_subpixel_y = self._io.read_u4le()
            self.stage_num_2 = self._io.read_u4le()
            self.stage_num_3 = self._io.read_u4le()
            self.chapter = self._io.read_u4le()
            self.time_in_stage = self._io.read_u4le()
            self.time_in_chapter_possibly_broken = self._io.read_u4le()
            self.shot = self._io.read_u4le()
            self.subshot_unused = self._io.read_u4le()
            self.season = self._io.read_u4le()
            self.score = self._io.read_u4le()
            self.difficulty = self._io.read_u4le()
            self.continues = self._io.read_u4le()
            self.rank_unused = self._io.read_u4le()
            self.graze = self._io.read_u4le()
            self.graze_chapter_possibly_broken = self._io.read_u4le()
            self.spell_practice_id = self._io.read_u4le()
            self.miss_count = self._io.read_u4le()
            self.point_items_collected = self._io.read_u4le()
            self.unknown_2 = self._io.read_u4le()
            self.piv = self._io.read_u4le()
            self.piv_min = self._io.read_u4le()
            self.piv_max = self._io.read_u4le()
            self.power = self._io.read_u4le()
            self.power_max = self._io.read_u4le()
            self.power_levelup = self._io.read_u4le()
            self.unknown_3 = self._io.read_u4le()
            self.lives = self._io.read_u4le()
            self.life_pieces = self._io.read_u4le()
            self.next_score_extend_id = self._io.read_u4le()
            self.bombs = self._io.read_u4le()
            self.bomb_pieces = self._io.read_u4le()
            self.season_power = self._io.read_u4le()
            self.season_power_max = self._io.read_u4le()
            self.unknown_4 = []
            for i in range(10):
                self.unknown_4.append(self._io.read_u4le())

            self.season_power_required = []
            for i in range(6):
                self.season_power_required.append(self._io.read_u4le())

            self.season_power_max_2 = self._io.read_u4le()
            self.unknown_5 = []
            for i in range(7):
                self.unknown_5.append(self._io.read_u4le())

            self.last_item_collected_pos = []
            for i in range(3):
                self.last_item_collected_pos.append(self._io.read_f4le())

            self.th14_item_spawn_count = self._io.read_u4le()
            self.unknown_6 = self._io.read_bytes(308)
            self.unknown_7 = self._io.read_u4le()
            self.unknown_8 = self._io.read_u4le()
            self.spellcard_real_times = []
            for i in range(21):
                self.spellcard_real_times.append(self._io.read_u4le())

            self.stage_data = self._io.read_bytes(self.end_off)



