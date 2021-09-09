import qrcode
qr = qrcode.QRCode(
#parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix)
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, #parameter controls the error correction used for the QR Code
    box_size=10, #parameter controls how many pixels each “box” of the QR code is.
    border=4, #parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs)
)
qr.add_data('https://www.google.com') #message
qr.make(fit=True) #parameter when making the code to determine this automatically.

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode1.jpg", "JPEG")