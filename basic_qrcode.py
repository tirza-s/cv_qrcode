import segno
from PIL import Image

cv_link = "https://t.ly/jUNcb"

# Generate QR code with custom colors and error correcttion level set to high = h
my_qr = segno.make(cv_link, error="h")
my_qr.save(
    "my_qrcode.png", 
    scale = 8, #Controls resolution (bigger scale = larger image)
    border = 6, # thickness of the border arround the qr 
    data_dark = (203, 176, 255), # Color for data modules (inner pixels)
    dark = (255, 119, 183),# Color for outer finder patterns
    light = (17, 2, 46)    # Background color
)

# Open the generated QR code and my logo image
qr_image = Image.open("my_qrcode.png").convert("RGBA")
logo = Image.open("logo/tirza-s logo.png").convert("RGBA")

# Resize logo to 25% of the QR code width
qr_w, qr_h = qr_image.size
logo_size = int(qr_w * 0.25)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Position offsets for the logo
# offset_x: negative = shift left, positive = shift right
# offset_y: negative = shift up,   positive = shift down
offeset_x = 0 # keep center horizontally 
offeset_y = 10 # move 10px lower 

# Calculate the top-left corner where the logo will be pasted
pos = ((qr_w - logo_size) // 2 + offeset_x,
        (qr_h - logo_size) // 2 - offeset_x)

#Paste the logo on top of the QR code
qr_image.paste(logo, pos, mask=logo)

# Save final QR code with embedded logo
qr_image.save("qr_logo.png", scale=8)