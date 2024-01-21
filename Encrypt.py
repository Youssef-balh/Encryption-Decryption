from posixpath import splitext
from ecies import encrypt
from PIL import Image
from qrcode import make as makeQR

pubhex = "Your public key"


def GenQRcode_And_watermark(data_string, img_path):
    qr_data = data_string
    qr = makeQR(qr_data)
    qr = qr.resize((512, 512))  

    im = Image.open(img_path)
    w, h = im.size
    imd = im.convert("RGBA").load() 
    watermarked_img = Image.new("RGBA", (w, h))

    for i in range(w):
        for j in range(h):
            d = imd[i, j]
            qr_pixel = qr.getpixel((i % 512, j % 512))
            watermarked_img.putpixel((i, j), tuple(d[:-1]) + ((d[-1] | 1) if qr_pixel else (d[-1] & ~1),))

    root, ext = splitext(img_path)
    watermarked_img.save('watermarked.png')

    qr.save(root + '_qrcode.png')

    with open(f"{'watermarked.png'}", "rb") as img:
        img_bytes = img.read()
    return img_bytes

def saveIntoTxt(endrypted_data):
    with open('encrypted.bin',"wb") as encryptTxt:
        encryptTxt.write(encrypted_data)


if __name__ == '__main__':
    img_name =  "captured.png"
    data = "Hello i m YoussefBlh"
    img_bytes = GenQRcode_And_watermark(data, img_name)
    encrypted_data = encrypt(pubhex, img_bytes)
    saveIntoTxt(encrypted_data)
    

