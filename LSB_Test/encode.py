from stegano import lsb

# Read the secret message
with open("message.txt", "r", encoding="utf-8") as file:
    secret_message = file.read()

# Hide the message
secret_image = lsb.hide("test.png", secret_message)

# Save the new image
secret_image.save("stegoTest.png")

print("Stego image created successfully!")