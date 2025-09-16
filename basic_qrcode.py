import segno
from PIL import Image

cv_link = "https://t.ly/HGs6Y"

my_qr = segno.make(cv_link, error="h")
my_qr.save(
    "my_qrcode.png", 
    scale = 8,
    border = 6,
    data_dark = (203, 176, 255),
    dark = (255, 119, 183),
    light = (17, 2, 46)
)

qr_image = Image.open("my_qrcode.png").convert("RGBA")
logo = Image.open("logo/TS.png").convert("RGBA")

qr_w, qr_h = qr_image.size
logo_size = int(qr_w * 0.25)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
qr_image.paste(logo, pos, mask=logo)

qr_image.save("qr_logo.png")