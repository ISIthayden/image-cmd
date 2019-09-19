# image-cmd scans web pages for images and displays them in a terminal
# web scraper command line tool with image viewer, time limited
# tool is called from the command line and does this:
#- get some list of image urls from the internet
#- picks a random image from list
#- displays that image to the terminal using shitty color terminal graphics

import os
import sys
import shutil
import random
import subprocess

# request url to scrape from user and assign it to a varible
url = input("Please enter a website to obtain images from:\n")

# call image-scraper and pass it the url, saving images in a new directory
subprocess.call(['/usr/bin/image-scraper','-s images','-m 10',url])

# randomly select a file within the images directory and assign its path to a variable
filePath = '/home/tony/image-cmd/ images/' + (random.choice(os.listdir('/home/tony/image-cmd/ images')))

# draw the image to the command line, using viu, passing it the path of the selected image
subprocess.call(['/usr/bin/viu', filePath])

shutil.rmtree(shutil.rmtree("images", ignore_errors=True, onerror=None))
