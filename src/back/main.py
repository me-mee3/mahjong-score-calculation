from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig

calculator = HandCalculator()

tiles = TilesConverter.string_to_136_array(man='22444', pin='333444', sou='444')
win_tile = TilesConverter.string_to_136_array(sou='4')[0]

result = calculator.estimate_hand_value(tiles, win_tile, config=HandConfig(is_tsumo=True))

print(result.han, result.fu)
print(result.cost['main'])
print(result.yaku)
for fu_item in result.fu_details:
    print(fu_item)