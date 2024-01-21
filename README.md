# QR Code Watermarking with ECC Encryption/Decryption

This Python script is designed for data encryption and decryption using Elliptic Curve Cryptography (ECC). The unique feature of this tool is the integration of QR code watermarking. Prior to encryption, the data is converted into a QR code, which is then embedded as a watermark onto an image. During the decryption process, the encrypted image is decrypted, watermarks are removed, and data is extracted from the QR code.

## Required libraries :
  Required Python libraries (install using `pip install -r requirements.txt`):
  - [`pycryptodome`]: Cryptographic library for ECC encryption.
  - [`opencv-python`]: OpenCV library for image processing.
  - [`qrcode`]: QR code generation.
  - [`pil`]: Image processing library.
  - [`ecies`]: ECC (Elliptic Curve Cryptography) encryption.

  
### Encryption

```bash
python encrypt.py 
