import qrcode
import image
qr=qrcode.QRCode(
    version=15, #15 means the version of the qrcode high the number bigger the code image and complicate picture
    box_size=10, #
    border=5
)
data="https://images.ctfassets.net/i3tkg7dt3kro/IlUCPwwkYQwcASb0gqXuW/63c5ab191e4f53cab04b5335f6ec7410/short-friendship-quotes.png"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="White")
img.save("test.png")