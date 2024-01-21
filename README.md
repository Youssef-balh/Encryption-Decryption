# QR Code Watermarking with ECC Encryption/Decryption

This Python script is designed for data encryption and decryption using Elliptic Curve Cryptography (ECC). The unique feature of this tool is the integration of QR code watermarking. Prior to encryption, the data is converted into a QR code, which is then embedded as a watermark onto an image. During the decryption process, the encrypted image is decrypted, watermarks are removed, and data is extracted from the QR code.

## Required libraries :
  Required Python libraries (install using `pip install -r requirements.txt`):
  - [`pycryptodome`]: Cryptographic library for ECC encryption.
  - [`opencv-python`]: OpenCV library for image processing.
  - [`qrcode`]: QR code generation.
  - [`pil`]: Image processing library.
  - [`ecies`]: ECC (Elliptic Curve Cryptography) encryption.
  - [`posixpath`]: Provides functions for manipulating paths based on the POSIX standard.

  
### Encryption

```bash
python encrypt.py 
```
### Decryption
```bash
python decrypt.py
```
![deco](https://github.com/Youssef-balh/Encryption-Decryption/assets/113738047/6bf97706-4747-4f87-91a3-53906caaa346) | ![deco](https://github.com/Youssef-balh/Encryption-Decryption/assets/113738047/73349d13-b4a6-4990-b2e5-a79f1a249aba)




