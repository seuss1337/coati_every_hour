from imutils import paths
from PIL import Image
import imagehash
import requests
import os
import re

# downloads every image on the file, 1 url per line. Also checks counter.txt
# for image naming purposes
def download_file(file):
    rows = open(file)
    total = 0
    with open("counter.txt") as f:
        total = int(f.readline())
    for url in rows:
        # workouround to fixing error downloading certain url's
        url1 = url.strip()
        fix = "??"
        url2 = str(url) + str(fix)
        try:
            response = requests.get(url1, timeout=10)
            print(url2)
            filen = os.path.sep.join(["images1", "{}.jpg".format(str(total).zfill(8))])
            if len(response.content) > 1000:
                open(filen, "xb").write(response.content)
        except:
            print("Error, skipping")
        total += 1
    os.remove("counter.txt")
    open("counter.txt", "xt").write(str(total))


# returns average hash of image
def create_hash(image):
    return str(imagehash.average_hash(Image.open(image)))


# checks if hash is in list of images tweeded before
def tweetedbefore(hash):
    rows = open("tweetedhash.txt", "rt")
    for line in rows:
        if hash == line.strip():
            return True
        else:
            return False
