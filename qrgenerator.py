import qrcode

def generate_qr_code(user_url):
    """Generates and displays a QR code given a URL"""
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )
    
    qr.add_data(user_url)  # Add URL data to the QR code
    qr.make(fit=True)      # Fit QR code to the data provided

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()                     # Display the QR code
    img.save("qr_code.png")        # Save QR code image as file

if __name__ == "__main__":
    # Prompt user to input URL
    user_url = input("Enter the URL to generate a QR code: ")
    generate_qr_code(user_url)     # Call the function with the input URL
# End of script - Use https://www.bioxsystems.com/ as the link for QR code generation