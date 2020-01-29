# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:08:10 2020

@author: Kamal
"""
def applyDistortionCorrection(name, settings):
# Function to apply 3D distortion correction retrospectively using code of
# Uten Yarach.
#
# ************************************************************************
# Version 0.1                                                  24.01.2020
# Narendra              narendrakumar dot anupoju at st dot ovgu dot de
# Kamal                 kamalhasan    dot battu   at st dot ovgu dot de
# ************************************************************************
    if settings.options.post.distortionCorrection:
        if settings.options.output.refData:
            print('===============================================================\n')
            print('| Conducting distortion correction. Started at #s\n', datestr(datetime('now')))
            print('===============================================================\n')
        
            if settings.options.output.gzip:
                refName = [name.namePath '/' name.nameFile '_withRef.nii.gz']
            else:
                refName = [name.namePath '/' name.nameFile '_withRef.nii']
    
        # Read data and orientation
            [img, RAS]= mris_read_nii(refName)
        
        # apply DiCo to Image
            dicoimg = CorrectDistortion(img, RAS)
        
        # Write NIfTI file
            print('| Writing NIfTI file...\n')
            [not,not,ext]=fileparts(refName)
            if strcmp(ext, '.gz'):
                tmp=refName(1:end-3)
                HeaderInfo=spm_vol_nifti(tmp)
                HeaderInfo.fname = [tmp(1:end-4) '_DiCo.nii']
            else:
                HeaderInfo=spm_vol_nifti(refName)
                HeaderInfo.fname = [refName(1:end-4) '_DiCo.nii']

            HeaderInfo.private.dat.fname = HeaderInfo.fname
        
            spm_write_vol(HeaderInfo,dicoimg)
            if settings.options.output.gzip:
                gzip(HeaderInfo.fname)
                delete(HeaderInfo.fname)
                print('| Done.\n')
                print('===============================================================\n\n')
        else:
            print('===============================================================\n')
            print('| Conducting distortion correction. Started at #s\n', datestr(datetime('now')))
            print('===============================================================\n')
            print('| Currently the origin is set to the center of the image. Please use a reference image to conduct distortion correction.\n')
            print('===============================================================\n\n')
  