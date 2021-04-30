import qrcode

string = input("Type anything: ")

qr = qrcode.QRCode(version=1, box_size=20, border= 10)
qr.add_data(string)
qr.make(fit=True)

image = qr.make_image(fill_color = 'green', back_color = 'black')
image.save('C:/Users/User/Pictures/Saved Pictures/qrcode2.jpg')
