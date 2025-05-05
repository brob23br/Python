import qrcode

url = "https://1drv.ms/b/c/b9b1d2e362f939e0/EUsO8z7BEq9CpzEs7ZKEiZgBdINzU4Td9PSl2FDQWNwewQ?e=lLGavZ"

qr = qrcode.make(url)

qr.save("resume_qr 5-5-25.png")
