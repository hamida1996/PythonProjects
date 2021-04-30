import pyzbar.pyzbar from decode
from PIL import Image

img = Image.open('C:/Users/User/Pictures/Saved Pictures/qrcode.jpg')

print(decode(img))
