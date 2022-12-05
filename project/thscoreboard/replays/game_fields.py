"""A class that provides methods used to properly format and display replay data"""

from immutabledict import immutabledict
from . import game_ids

_table_fields_th06 = immutabledict({
    'stage': True,
    'score': True,
    'piv': False,
    'graze': False,
    'point_items': False,
    'power': True,
    'lives': True,
    'life_pieces': False,
    'bombs': True,
    'bomb_pieces': False,
    'th06_rank': True,
    'th07_cherry': False,
    'th07_cherrymax': False,
})

_table_fields_th07 = immutabledict({
    'stage': True,
    'score': True,
    'piv': True,
    'graze': True,
    'point_items': True,
    'power': True,
    'lives': True,
    'life_pieces': False,
    'bombs': True,
    'bomb_pieces': False,
    'th06_rank': False,
    'th07_cherry': True,
    'th07_cherrymax': True,
})

_table_fields_th10 = immutabledict({
    'stage': True,
    'score': True,
    'piv': True,
    'graze': False,
    'point_items': False,
    'power': True,
    'lives': True,
    'life_pieces': False,
    'bombs': False,
    'bomb_pieces': False,
    'th06_rank': False,
    'th07_cherry': False,
    'th07_cherrymax': False,
})

_table_fields_th08 = immutabledict({
    'stage': True,
    'score': True,
    'piv': True,
    'graze': True,
    'point_items': True,
    'power': True,
    'lives': True,
    'life_pieces': False,
    'bombs': True,
    'bomb_pieces': False,
    'th06_rank': False,
    'th07_cherry': False,
    'th07_cherrymax': False,
})

_table_fields_th11 = immutabledict({
    'stage': True,
    'score': True,
    'piv': True,
    'graze': True,
    'point_items': False,
    'power': True,
    'lives': True,
    'life_pieces': True,
    'bombs': False,
    'bomb_pieces': False,
    'th06_rank': False,
    'th07_cherry': False,
    'th07_cherrymax': False,
})

_game_fields = immutabledict({
    'th01': None,
    'th05': None,
    'th06': _table_fields_th06,
    'th07': _table_fields_th07,
    'th08': _table_fields_th08,
    'th10': _table_fields_th10,
    'th11': _table_fields_th11
})


def GetFormatPower(game_id: str, power: int) -> str:
    if game_id in (game_ids.GameIDs.TH06, game_ids.GameIDs.TH07, game_ids.GameIDs.TH08):
        return str(power)
    if game_id in (game_ids.GameIDs.TH10, game_ids.GameIDs.TH11):
        return "%.2f" % (float(power) * 0.05)

    return str(power)


_life_pieces = immutabledict({
    'th01': None,
    'th05': None,
    'th06': None,
    'th07': None,
    'th08': None,
    'th10': None,
    'th11': 5
})


def GetFormatLives(game_id: str, lives: int, life_pieces: int) -> str:
    total_life_pieces = _life_pieces[game_id]
    if total_life_pieces is None:
        return str(lives)
    else:
        return f"{lives} ({life_pieces}/{total_life_pieces})"


def GetGameField(gameid: str):
    if gameid in _game_fields:
        return _game_fields[gameid]
    return None


def GetGameLifePieces(gameid: str):
    if gameid in _life_pieces:
        return _life_pieces[gameid]
    return None

def GetFormatStage(game_id: str, stage: int) -> str:
    if game_id == "th08":
        stages = {
            0: '1',
            1: '2',
            2: '3',
            3: '4A',
            4: '4B',
            5: '5',
            6: '6A',
            7: '6B',
            8: '7',
        }
        return stages[stage]
    elif game_id in ['th06', 'th07']:
        return str(stage+1)
    else:
        return str(stage)
