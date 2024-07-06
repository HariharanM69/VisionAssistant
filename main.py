import qrcode

# URL to be encoded in the QR code
url = "https://hm69visionassistant-test.streamlit.app/"

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img_path = "vision_assistant_qr_code.png"
img.save(img_path)

img_path