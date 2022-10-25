from odoo import fields, models, api, _
from odoo.exceptions import UserError
import chess
import chess.svg
import cairosvg
import io
import base64
import PIL.Image as Image


class SlideSlide(models.Model):
    _inherit = "slide.slide"

    fen = fields.Char('FEN')

    @api.onchange('fen')
    def _onchange_fen(self):
        if self.fen:
            board = chess.Board(self.fen)
            chess.STARTING_BOARD_FEN=self.fen

            boardsvg = chess.svg.board(flipped=True,
                                    #lastmove = chess.Move.from_uci('c7c5'),
                                    coordinates=False,
                                    board = board,
                                    size=1050,
                                    colors={"square light": "#eeedd5", "square dark": "#7c945d", })

            in_mem_file = io.BytesIO()
            cairosvg.svg2png(bytestring=boardsvg, write_to=in_mem_file)
            image= Image.open(io.BytesIO(in_mem_file.getvalue()))
            #image.show()
            b64image = base64.b64encode(in_mem_file.getvalue())
            #print(b64image)
            self.name='Chess'
            self.slide_type='infographic'
            self.is_preview=True
            self.image_1920=b64image

