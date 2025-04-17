import qrcode 
def generate_qr_code(data, filename): 
# Create a QR code instance 
qr = qrcode.QRCode( 
version=1, 
error_correction=qrcode.constants.ERROR_CORRECT_L, 
box_size=10, 
border=4, 
) 
# Add data to the QR code 
qr.add_data(data) 
qr.make(fit=True) 
# Create an image from the QR code 
img = qr.make_image(fill_color="black", back_color="white") 
# Save the image 
img.save(filename) 
if __name__ == "__main__": 
# Example data and filename 
data = "https://www.nafeestech.blog" 
filename = "Nafees.png" 
# Generate and save the QR code 
generate_qr_code(data, filename) 
print(f"QR code generated and saved as {filename}")
