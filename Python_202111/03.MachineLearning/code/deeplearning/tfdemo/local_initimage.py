#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'demo'))
	print(os.getcwd())
except:
	pass

#%%
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Required magic to display matplotlib plots in notebooks
get_ipython().run_line_magic('matplotlib', 'inline')

# This is where we extracted the images
imgdir = 'dataset'

# Set up a figure of an appropriate size
fig = plt.figure(figsize=(12, 16))

# loop through the subfolders
dir_num = 0
for root, folders, filenames in os.walk(imgdir):
    for folder in folders:
        # Load the first image file using the PIL library
        file = os.listdir(os.path.join(root,folder))[0]
        imgFile = os.path.join(root,folder, file)
        img = Image.open(imgFile)
        # Add the image to the figure (which will have 4 columns and enough rows to show a file from each folder)
        a=fig.add_subplot(4,np.ceil(len(folders)/4),dir_num + 1)
        imgplot = plt.imshow(img)
        # Add a caption with the foilder name
        a.set_title(folder)
        dir_num = dir_num + 1


#%%
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Helper function to resize image
def resize_image(img, size): 
    from PIL import Image, ImageOps 
    
    # resize the image so the longest dimension matches our target size
    img.thumbnail(size, Image.ANTIALIAS)
    
    # Create a new square white background image
    newimg = Image.new("RGB", size, (255, 255, 255))
    
    # Paste the resized image into the center of the square background
    if np.array(img).shape[2] == 4:
        # If the source is in RGBA format, use a mask to eliminate the transparency
        newimg.paste(img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)), mask=img.split()[3])
        print(size[0])
        print(size[1])
        print(img.size[0])
        print(img.size[1])
        print(img.split()[3])
        
    else:
        newimg.paste(img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
        print(size[0])
        print(size[1])
        print(img.size[0])
        print(img.size[1])
        
        #print(img.split()[3])
  
    # return the resized image
    return newimg


# Create resized copies of all of the source images
size = (128,128)

indir = 'dataset'
outdir = 'resized_dataset'

# Create the output folder if it doesn't already exist
if os.path.exists(outdir):
    shutil.rmtree(outdir)

# Loop through each subfolder in the input dir
for root, dirs, filenames in os.walk(indir):
    for d in dirs:
        print('processing folder ' + d)
        # Create a matching subfolder in the output dir
        saveFolder = os.path.join(outdir,d)
        if not os.path.exists(saveFolder):
            os.makedirs(saveFolder)
        # Loop through the files in the subfolder
        files = os.listdir(os.path.join(root,d))
        for f in files:
            # Open the file
            imgFile = os.path.join(root,d, f)
            print("reading " + imgFile)
            img = Image.open(imgFile)
            # Create a resized version and save it
            proc_img = resize_image(img, size)
            saveAs = os.path.join(saveFolder, 'resized_' + f)
            print("writing " + saveAs)
            proc_img.save(saveAs)
            #break
            


#%%
# Create a new figure
fig = plt.figure(figsize=(10, 40))

# loop through the subfolders in the input directory
img_num = 1
for root, folders, filenames in os.walk(indir):
    for folder in folders:
        # Get the first image in the subfolder and add it to a plot that has two columns and row for each folder
        file = os.listdir(os.path.join(root,folder))[0]
        imgFile1 = os.path.join(indir,folder, file)
        img1 = Image.open(imgFile1)
        a=fig.add_subplot(len(folders), 2, img_num)
        imgplot = plt.imshow(img1)
        a.set_title(folder)
        # The next image is the resized counterpart - load and plot it
        img_num = img_num + 1
        imgFile2 = os.path.join(outdir,folder, 'resized_' + file)
        img2 = Image.open(imgFile2)
        b=fig.add_subplot(len(folders), 2, img_num)
        imgplot = plt.imshow(img2)
        b.set_title('resized ' + folder)
        img_num = img_num + 1


#%%



