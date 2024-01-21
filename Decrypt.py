from posixpath import splitext
from ecies import decrypt
from PIL import Image
from pyzbar.pyzbar import decode


privhex = "Your private key"


#Remove watermarks ,get hidden qr code and extract data  
def qr_code_to_real_data(img_path):
    im = Image.open(img_path)
    s = w, h = im.size
    imd = im.load()
    oim = Image.new('1', s)
    oimd = oim.load()
    for i in range(w):
        for j in range(h):
            d = imd[i, j]
            oimd[i, j] = 255 * (d[-1] & 1)
    root, ext = splitext(img_path)
    fname = 'deco' + ext
    oim.save(fname)
    decoded_objects = decode(Image.open(fname))
    data = [obj.data.decode("utf-8") for obj in decoded_objects][0]
    return data 
    
    
def openTxtFile():
    with open("encrypted.bin","rb") as encrypted_data:
        return encrypted_data.read()

def saveImg(img_data):
    with open('decrypted.png',"wb") as decrypted:
        decrypted.write(img_data)    

if __name__ == '__main__':
    encrypted_img = openTxtFile()
    decrypted_img = decrypt(privhex,encrypted_img)
    saveImg(decrypted_img)
    data = qr_code_to_real_data("decrypted.png")
    print(data)
