import io
import base64
import PIL.Image as Image
import numpy as np
import chess
import chess.svg
import cairosvg

fen = "r1bqkb2/pppp1ppp/2n2n2/4p2r/2B1P3/3P1N2/PPP2PPP/RNBQ1RK1 w Qkq - 0 1"
board = chess.Board(fen)
chess.STARTING_BOARD_FEN=fen

boardsvg = chess.svg.board(flipped=True,
                           #lastmove = chess.Move.from_uci('c7c5'),
                           coordinates=False,
                           board = board,
                           size=350,
                           colors={"square light": "#eeedd5", "square dark": "#7c945d", })

in_mem_file = io.BytesIO()
cairosvg.svg2png(bytestring=boardsvg, write_to=in_mem_file)
image= Image.open(io.BytesIO(in_mem_file.getvalue()))
image.show()
b64image = base64.b64encode(in_mem_file.getvalue())
print(b64image)


