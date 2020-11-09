import image_services as IS

# IS.download_file("urls0.txt")


str1 = IS.create_hash("images/coati.jpg")
str2 = IS.create_hash("images/coati_sd.jpg")


if IS.tweetedbefore(str1):
    print("TRUE")
