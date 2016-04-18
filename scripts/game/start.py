import sys
sys.path.insert(1,'/home/luiz/Projects/Checkers/scripts/classes')
import game_board, piece, position, track, player

def set_pieces(tab):
    player1 = player.Player(1)
    player2 = player.Player(2)
    for item in range(0, 8):
        for i in range(0, 8):
            if not ((item + i) % 2 == 0):
                if item < 3: a_player = player1
                elif item > 4: a_player = player2
                else: a_player = False
                if a_player:
                    a_piece = piece.Piece(tab[item][i], a_player)
                    tab[item][i].occupation = a_piece
                    a_player.pieces.append(a_piece)

