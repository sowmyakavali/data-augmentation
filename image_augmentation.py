from PIL import Image
from PIL import ImageEnhance
import os
import torch
from torchvision import transforms


 
directory="./data/"
directory2="./resized/"
directory3="./rotated/"
directory4="./transposed/"
directory5="./enhanced_images/"
directory6="./image_colored/" 
directory7="./image_contrasted/" 
directory8="./image_sharped/"
#size=(640,556)


 
#-----------to craete a new folder----------------
def create_folder_if_not_exists(path):

    if(not os.path.exists(path)):
        try:
            os.mkdir(path)
            print("Created folder {}".format(path))
        except FileExistsError:
            print("The folder already exists")
            raise
            pass
        pass
    else:
        print("The folder {} already exists ".format(path))
#--------------to remove a folder---------------------
def remove_folder(path):
    if(os.path.exists(path)):
        # Delete all contents of a directory using shutil.rmtree() and  handle exceptions
        try:

            shutil.rmtree(path,ignore_errors=False)
            print("Folder {} is entirely removed ".format(path))
        except:
            print('Error while deleting directory')
            pass
        pass
    else:
        print("the folder {} does not exist. So, could not remove it.".format(path))

#for i in list_of_directories:
#	remove_folder(path)

#for i in list_of_directories:
#	create_folder_if_not_exists(path)
create_folder_if_not_exists(directory2)
create_folder_if_not_exists(directory3)
create_folder_if_not_exists(directory4)
create_folder_if_not_exists(directory5)
create_folder_if_not_exists(directory6)
create_folder_if_not_exists(directory7)
create_folder_if_not_exists(directory8)

size=(300,300)

#------------------To resize the images----------------------------

def rescale_images(directory, size):
	count=0
	for img in os.listdir(directory):       
		if(img.endswith(".jpg")):  		
			im = Image.open(directory+img)          
			image_size=im.size
			#if(cmp(size,image_size)!=0):			
			if( (size>image_size) - (size<image_size) !=0):
				im_resized = im.resize(size, Image.ANTIALIAS)
				im_resized.save(directory2+img)
				count=count+1


'''def resize_images(directory):
	count=0
	for img in os.listdir(directory):       
		if(img.endswith(".jpg")):  		
			im = Image.open(directory+img)          
			basewidth = 300
			wpercent = (basewidth / float(im.size[0]))
			hsize = int((float(im.size[1]) * float(wpercent)))
			im_resized = im.resize((basewidth, hsize), Image.ANTIALIAS)
			im_resized.save(directory2+img) '''

#-----------------------image rotation----------------------------
def image_rotation(directory):
           for img in os.listdir(directory):
                   if (img.endswith(".jpg")):
                        im1  = Image.open(directory+img)
                        # Rotate it by 45 degrees
                        im2  = im1.rotate(45)
                        im2.save(directory3+img)
                        # Rotate it by 90 degrees
                        im3  = im1.transpose(Image.ROTATE_180)
                        im3.save(directory4+img)

#---------------------image color enhancement------------------------------           
def image_enhance(directory):
	for img in os.listdir(directory):
		if (img.endswith(".jpg")):
			image  = Image.open(directory+img)
			enh_bri = ImageEnhance.Brightness(image)
			brightness = 1.5
			image_brightened = enh_bri.enhance(brightness)
			image_brightened.save(directory5+img)

			enh_col = ImageEnhance.Color(image)
			color = 1.5
			image_colored = enh_col.enhance(color)
			image_colored.save(directory6+img)
			
			enh_con = ImageEnhance.Contrast(image)
			contrast = 1.5
			image_contrasted = enh_con.enhance(contrast)
			image_contrasted.save(directory7+img)
			

			enh_sha = ImageEnhance.Sharpness(image)
			sharpness = 3.0
			image_sharped = enh_sha.enhance(sharpness)
			image_sharped.save(directory8+img)
			

def affine_transform(directory):
	for img in os.llistdir(directory):
		if(img.endswith(".jpg")):
			loader_transform = transforms.RandomAffine(0, translate=(0.4, 0.5))
			

rescale_images(directory, size)
#resize_images(directory)
image_rotation(directory)
image_enhance(directory)
