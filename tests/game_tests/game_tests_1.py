import sys
sys.path.insert(1,'/home/luiz/Projects/Checkers/scripts/classes')
sys.path.insert(1,'/home/luiz/Projects/Checkers/scripts/game')
import game_board, piece, position, track, start

tab = game_board.Board()


def draw_tab(tab):
    string = ""
    for line in tab:
        for column in line:
            string += column.get_draw() + " "
        string += "\n"
    return string

start.set_pieces(tab)

print (draw_tab(tab))