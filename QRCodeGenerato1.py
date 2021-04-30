# pip install qrcode

import qrcode

print("\nThis is a QR Code Generator")
print("============================\n")

string = input("Type anything: ")

image = qrcode.make(string)
image.save("C:/Users/User/Pictures/Saved Pictures/qrcode.jpg")

