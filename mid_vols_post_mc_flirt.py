# Get middle volumes from 
import numpy as np
import nibabel as nib
from nibabel import load
import matplotlib.pyplot as plt
import os
from os import path

# NB do not chose sagital acquisitions
# func = '/home/ainedineen/motion-robust-mri/bids/workingdir_truncated_adult_pilot/001/deriv/preproc/bold_preproc/_subject_id_001/_acquisition_MbSagit_session_1_task_name_PMstill/mcflirt/sub-001_ses-1_task-PMstill_acq-MbSagit_dir-AP_bold_mcf.nii'


# # MOTION
# func = "/home/ainedineen/motion-robust-mri/bids/workingdir_truncated_adult_pilot/001/deriv/preproc/bold_preproc/_subject_id_001/_acquisition_SbAxial_session_1_task_name_HHmotion/mcflirt/sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold_mcf.nii"
# outdir = 'sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold_mid_vols_mcf'

# STILL
# func = "/home/ainedineen/motion-robust-mri/bids/workingdir_truncated_adult_pilot/001/deriv/preproc/bold_preproc/_subject_id_001/_acquisition_SbAxial_session_1_task_name_HHstill/mcflirt/sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mcf.nii"
# outdir = 'sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_mcf'


# func = '/home/ainedineen/motion-robust-mri/bids/sub-001/ses-1/func/sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold.nii.gz'
# outdir = 'sub-001_ses-1_task-HHmotion_acq-SbAxial_dir-AP_bold_mid_vols_raw'
# func = '/home/ainedineen/motion-robust-mri/bids/sub-001/ses-1/func/sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold.nii.gz'
# outdir = 'sub-001_ses-1_task-HHstill_acq-SbAxial_dir-AP_bold_mid_vols_raw'

# func = nib.load(path)


# func = '/home/ainedineen/motion-robust-mri/bids/sub-001/ses-1/func/sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold.nii.gz'
# outdir = 'sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold_mid_vols_raw'
func = '/home/ainedineen/motion-robust-mri/bids/sub-001/ses-1/func/sub-001_ses-1_task-PCHstill_acq-MbAxial_dir-AP_bold.nii.gz'
outdir = 'sub-001_ses-1_task-PCHstill_acq-MbAxial_dir-AP_bold_mid_vols_raw'


# # STILL
# func = "/home/ainedineen/motion-robust-mri/bids/workingdir_truncated_adult_pilot/001/deriv/preproc/bold_preproc/_subject_id_001/_acquisition_MbAxial_session_1_task_name_PCHstill/mcflirt/sub-001_ses-1_task-PCHstill_acq-MbAxial_dir-AP_bold_mcf.nii"
# outdir = 'sub-001_ses-1_task-PCHstill_acq-MbAxial_dir-AP_bold_mid_vols_mcf'

# MOTION
# func = "/home/ainedineen/motion-robust-mri/bids/workingdir_truncated_adult_pilot/001/deriv/preproc/bold_preproc/_subject_id_001/_acquisition_MbAxial_session_1_task_name_PCHmotion/mcflirt/sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold_mcf.nii"
# outdir = 'sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold_mid_vols_mcf'




# sub-001_ses-1_task-PCHmotion_acq-MbAxial_dir-AP_bold.nii.gz
# sub-001_ses-1_task-PCHstill_acq-MbAxial_dir-AP_bold.nii.gz
search_range=20



funcfile = func
if isinstance(func, list):
    funcfile = func[0]

# load functional time series
epi_img = nib.load(funcfile)
epi_img_data = epi_img.get_fdata()

outfiles = []

x = int(int(epi_img_data.shape[3]) / 2) - 1

half_range = int(search_range/2)

# For both reference types, dump slices for search range
for i in range(x - half_range, x + half_range):
    # add outfiles
    out_file = os.path.abspath(f"{outdir}/sag_slice32_vol{i}.png")
    print(f"out_file: {out_file}, type: {type(out_file)}")
    # fix outfile with directory!!!!!
    plt.imsave(out_file, np.rot90(epi_img_data[32,:,:,i]), cmap='gray');
    outfiles.append(out_file)

    # out_path = path.join(outdir,out_file)

    # print(f"out_file: {out_path}, type: {type(out_file)}")
    # # fix outfile with directory!!!!!
    # plt.imsave(out_path, np.rot90(epi_img_data[32,:,:,i]), cmap='gray');
    # outfiles.append(out_path)


    print(f" n of volumes in time series: {epi_img_data.shape[3]}")

    # Pairwise comparison of the 20 middle volumes of the time series in the frequency domain using sum of squares

    # Middle volume of the timeseries
    dist_squared = np.empty((search_range,search_range))

    counter = 0
    counter_i = 0

    for i in range(x - half_range, x + half_range):
        counter_j = 0                
        for j in range(x - half_range, x + half_range ):
    
            vol_1 = epi_img_data[:,:,:,i]
            vol_2 = epi_img_data[:,:,:,j]

            # Compute the 3-dimensional discrete Fourier Transform. Shift the zero-frequency component to the center of the spectrum.
            # Take absolute value of each complex number. Square the difference of the elements of the volumes
            # Sum all elements of the array of squared differences.
            # log was added to make numbers more managable
            one_dist_squared = np.sum(np.square(np.log(np.abs(np.fft.fftshift(np.fft.fftn(vol_1)))) - np.log(np.abs(np.fft.fftshift(np.fft.fftn(vol_2))))))

            dist_squared[counter_i, counter_j] = one_dist_squared
    
            counter += 1
            counter_j += 1

        counter_i += 1

    # find the average distance from each of the volumes to each of the other volumes
    mean_dist = np.zeros(search_range)
    for i in range(search_range):
        mean_dist[i] = np.mean(dist_squared[i])

    # Return the minimum of the average distances ignoring any NaNs
    min = np.nanmin(mean_dist)

    print(' Minimum element of Numpy Array: ', min)

    # Get the indices of minimum elements in numpy array
    result = np.where(mean_dist == min)

    print(f" Returned tuple of indicies of volumes with min distance from all other volumes: {result}\n n of min vols (1 desired): {len(result)}\n Index of minimum element (assuming just 1): {result[0]}\n Middle vol: {x}")

    reference = x - half_range + result[0]
    reference = int(reference[0])

print(f" vol of choice: volume {reference}")


print(outfiles)

# return reference, outfiles