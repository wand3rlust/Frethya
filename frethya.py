import piexif
import base64

# Function to write EXIF data
def encode(file_path, message):
    try:
        
        # Retrieve EXIF data in Dictionary format
        exif_data = piexif.load(file_path)
        
        # Check if image contains EXIF data
        if "Exif" not in exif_data.keys():
            exif_data["Exif"] = {}
        
        # Encode message in base64  string
        encoded_message = base64.b64encode(message.encode("utf-8")).decode("utf-8")
        
        # Put base64 string in "UserComment" EXIF tag
        exif_data["Exif"][piexif.ExifIFD.UserComment] = encoded_message.encode("utf-8")
        
        # Insert modified EXIF data into image
        piexif.insert(piexif.dump(exif_data), file_path)
        
        print("Secret message written to the image.")
    except Exception as e:
        print(f"Error: {e}")


# Function to read EXIF data
def decode(file_path):
    try:
        
        # Retrieve EXIF data in Dictionary format
        exif_data = piexif.load(file_path)
        
        # Check if image contains EXIF data
        if "Exif" in exif_data.keys():
            
            # Check if "UserComment" tag in present
            if piexif.ExifIFD.UserComment in exif_data["Exif"].keys():
                
                # Read value in "UserComment" EXIF tag
                secret_message = exif_data["Exif"][piexif.ExifIFD.UserComment].decode("utf-8")
                
                # Decode base64 string
                decoded_message = base64.b64decode(secret_message).decode("utf-8")
                print(f"Secret Message: {decoded_message}")
            else:
                print("No secret message found.")
        else:
            print("No EXIF data found in the image.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\033[1;31m")
    print("\n▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄")
    print(" ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌")
    print(" ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌")
    print(" ▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌")
    print(" ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌")
    print(" ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
    print(" ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌")
    print(" ▐░▌          ▐░▌     ▐░▌  ▐░▌               ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌")
    print(" ▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌")
    print(" ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌")
    print("  ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀       ▀       ▀         ▀ ")
    print("\033[0;0m")
    print("\033[1;32m")
    print("\n                                      Author: Abhijeet Kumar")
    print("                                   Github: github.com/wand3rlust")
    print("\033[0;0m")
    print("\033[1;34m")
    print("\n1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        file_path = input("Enter the file path: ")
        message = input("Enter the secret message: ")
        encode(file_path, message)
    elif choice == "2":
        file_path = input("Enter the file path: ")
        decode(file_path)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
