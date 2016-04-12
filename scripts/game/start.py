import sys
sys.path.insert(1,'/home/luiz/Projects/Checkers/scripts/classes')
import game_board, piece, position, track

def set_pieces(tab):
    for item in range(0, 8):
        for i in range(0, 8):
            if (item + i) % 2 == 0:
                pass
            else:
                if item < 3:
                    player = "player1"
                elif item > 4: player = "player2"
                else: player = False
                if player: tab[item][i].occupation = piece.Piece(tab[item][i], player)

