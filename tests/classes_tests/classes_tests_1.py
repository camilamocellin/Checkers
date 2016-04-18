import sys
sys.path.insert(1,'/home/luiz/Projects/Checkers/scripts/classes')
import game_board, piece, position, track

tab = game_board.Board()
print(tab)
print(tab[1][1])
print (tab[2][1])

def draw_tab(tab):
    string = ""
    for line in tab:
        for column in tab[0]:
            string += column.get_draw() + " "
        string += "\n"
    return string

print (draw_tab(tab))