
# /home/ainedineen/motion-robust-mri/create_gifs
# /home/ainedineen/motion-robust-mri/bids/sub-001/ses-1/func
# sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold.nii.gz
# sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold.nii.gz
# /home/ainedineen/motion-robust-mri/bids/sub-001/ses-1/func


import os
import numpy as np

# from nibabel.testing import data_path
# example_file = os.path.join(data_path, 'example4d.nii.gz')

# 49 - 68
# example_file = os.path.join(data_path, '/home/users/dineenai/bids/01AD/ses-1/func/sub-01AD_ses-1_acq-infant_MB_Sag_int_still_dir-AP_task-audio_PCH_bold.nii')
example_file = "/home/ainedineen/motion-robust-mri/bids/sub-001/ses-1/func/sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold.nii.gz"


#  load the file to create a nibabel image object:
import nibabel as nib
import matplotlib.pyplot as plt

epi_img_data = nib.load(example_file)
print(epi_img_data.shape)


data = epi_img_data.get_fdata()
print(data.shape)
i = 68
# out_file = os.path.abspath(f"sag_slice32_vol{str(i)}.png")
# print(f"out_file: {out_file}, type: {type(out_file)}")
# plt.imsave(out_file, np.rot90(epi_img_data[32,:,:,i]), cmap='gray');

plt.imsave('sag_slice32_vol68.png', np.rot90(epi_img_data[32,:,:,i]), cmap='gray');