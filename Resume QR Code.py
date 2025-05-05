import qrcode

url = "https://"
qr = qrcode.make(url)
qr.save("resume_qr 5-5-25.png")
