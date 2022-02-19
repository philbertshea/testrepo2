import cv2
import os

for subcat in range(10):
        for filename in os.listdir(os.path.join("gtsrb", str(subcat))):
            with open(os.path.join("gtsrb", str(subcat), filename)) as f:
                print(f"File {filename} in sub-category {subcat} has been read.")
