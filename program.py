import fen2pil
import io
import base64
import PIL.Image as Image
import numpy as np



from fen2pil import draw

fen = "r1bqkb2/pppp1ppp/2n2n2/4p2r/2B1P3/3P1N2/PPP2PPP/RNBQ1RK1 w Qkq - 0 1"

pil_image = draw.transform_fen_pil(
        fen=fen,
        board_size=480,
        light_color=(255, 253, 208),
        dark_color=(76, 153, 0)
    )
buffered = io.BytesIO()
pil_image.save(buffered, format="PNG")
b64image = base64.b64encode(buffered.getvalue())

img = np.array(Image.open(io.BytesIO(base64.b64decode(b64image))))
pil_image.show()
print(img.shape)

