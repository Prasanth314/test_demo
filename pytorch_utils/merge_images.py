from PIL import Image
def merge_images(img1,img2,dest_folder):
  img_01 = Image.open(img1)
  img_02 = Image.open(img2)
  # img_03 = Image.open("digit-number-img-2.jpg")
  # img_04 = Image.open("digit-number-img-3.jpg")

  img_01_size = img_01.size
  img_02_size = img_02.size
  # img_03_size = img_02.size
  # img_02_size = img_02.size

  print('img 1 size: ', img_01_size)
  print('img 2 size: ', img_02_size)
  # print('img 3 size: ', img_03_size)
  # print('img 4 size: ', img_03_size)

  new_im = Image.new('RGB', (2*img_01_size[0],2*img_01_size[1]), (250,250,250))

  new_im.paste(img_01, (0,0))
  new_im.paste(img_02, (img_01_size[0],0))
  # new_im.paste(img_03, (0,img_01_size[1]))
  # new_im.paste(img_04, (img_01_size[0],img_01_size[1]))
  img1=img1.split('/')[-1]
  new_im.save(dest_folder+img1, "PNG")
  new_im.show()

  
import os
folder1_path = '/content/cur/A/'
folder2_path = '/content/cur/B/'
for img1 in os.listdir(folder1_path):
  if(img1.startswith("real")):
    img2=img1.replace("real","fake")
    if(os.path.exists(folder2_path+img2)):
      merge_images(folder1_path+img1,folder2_path+img2,'/content/')
