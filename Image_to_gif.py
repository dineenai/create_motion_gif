from PIL import Image
import glob
from shutil import copyfile
 
# Create the frames
frames = []


# images = "/home/ainedineen/foundcog/bids/derivatives/middle_volumes/_subject_id_IRC27/_run_1_session_1_task_name_pictures/_referencetype_robust/*.png"
# images = "/home/ainedineen/motion-robust-mri/bids/deriv_truncated_adult_pilot/middle_volumes/_subject_id_001/_acquisition_MbAxial_session_1_task_name_PCHstill/*.png"
# images = "/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHstill_middle_vols/*.png"
# source = "/home/ainedineen/motion-robust-mri/bids/deriv_truncated_adult_pilot/middle_volumes/_subject_id_001/_acquisition_MbAxial_session_1_task_name_PCHstill/*.png"
# dest = "/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHstill_middle_vols"
# copyfile(source, dest)
# im = Image.open(path.join(reports_dir, img_dest_dir, slice))
# resized_img = im.resize((512, 288))
# resized_img.save(path.join(reports_dir, img_dest_dir, slice))

# images = "/home/ainedineen/motion-robust-mri/create_gifs/sub-001_MBAx_PCHstill_middle_vols/*.png"
# sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold_mid_vols_mcf
# sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold_mid_vols_raw
# sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_mcf
# sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_raw


# sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold_mid_vols_raw

# PENDING!
# sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold_mid_vols_raw
# sub-001_ses-1_task-PCHstill_acq-MbAxial_dir-AP_bold_mid_vols_mcf
# sub-001_ses-1_task-PCHstill_acq-MbAxial_dir-AP_bold_mid_vols_raw

images = "/home/ainedineen/motion-robust-mri/create_gifs/sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold_mid_vols_raw/*.png"




# imgs = glob.glob("*.png")
imgs = glob.glob(images)
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
# Save into a GIF file that loops forever
frames[0].save('sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold_mid_vols_raw_small.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)