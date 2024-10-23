import pyqrcode
import pypng

def qr_code():
    q = pyqrcode.create(input("Enter the text: "))
    q.png('generated_qr_code.png', scale=6)
    print("QR Code Generated")

qr_code()