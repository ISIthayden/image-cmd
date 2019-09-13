# image-cmd scans web pages for images and displays them in a terminal
# web scraper command line tool with image viewer, time limited
# tool is called from the command line and does this:
#- get some list of image urls from the internet
#- picks a random image from list
#- displays that image to the terminal using shitty color terminal graphics

import os
import random
import subprocess

print("Please enter a website to obtain images from:\n")
url = input('')

subprocess.call(['/usr/bin/image-scraper','-s images','-m 10',url])

filePath = '/home/tony/image-cmd/ images/' + (random.choice(os.listdir('/home/tony/image-cmd/ images')))

subprocess.call(['/usr/bin/viu', filePath])
