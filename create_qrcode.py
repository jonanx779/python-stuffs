# Code for creating QR codes using pyqrcode
# Jonathan Salazar Santos

import pyqrcode
import png
from pyqrcode import QRCode

# String which represent the QR code
s = "jonathansalazar.com"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg  file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png("JonathanSalazarSantos.png", scale = 6)