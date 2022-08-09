import os
from PIL import Image
from os import path

# PATH = "/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHstill_middle_vols"
# Copy_to_path="/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHstill_middle_vols"

# for filename in os.listdir(PATH):
#     img = Image.open(os.path.join(PATH, filename)) # images are color images

#     print(img)
#     # img = img.resize((224,224), Image.ANTIALIAS)
#     resized_img = img.resize((512, 288))
#     img.save(Copy_to_path+filename+'.png') 



# im = Image.open(path.join('/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHstill_middle_vols', 'sag_slice32_vol214.png'))

# im = Image.open('/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHstill_middle_vols/*.png')


# # resized_img = im.resize((512, 288))
# resized_img = im.resize((512, 352))
# resized_img.save()



# PATH = '/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHmotion_middle_vols'

# for filename in os.listdir(PATH):
#     im = Image.open(os.path.join(PATH, filename)) # images are color imasges
#     print(im.size) #(64, 44)
#     resized_img = im.resize((256, 176))
#     resized_img.save(filename)



# sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold_mid_vols_mcf
# sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold_mid_vols_raw
# sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_mcf
# sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_raw
in_path = '/home/ainedineen/motion-robust-mri/create_gifs/sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_raw'
out_path = '/home/ainedineen/motion-robust-mri/create_gifs/sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_raw_LARGE'
for filename in os.listdir(in_path):
    im = Image.open(os.path.join(in_path, filename)) # images are color imasges
    print(im.size) #(64, 44)
    resized_img = im.resize((256, 176))
    # output = 
    resized_img.save(f'{out_path}/{filename}')