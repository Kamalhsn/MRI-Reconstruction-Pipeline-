# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:28:38 2020

@author: Kamal
"""

def checkNoise(preset):
# Function to check whether noise data has been processed
# ************************************************************************
# Version 0.1                                                  24.01.2020
# Narendra              narendrakumar dot anupoju at st dot ovgu dot de
# Kamal                 kamalhasan    dot battu   at st dot ovgu dot de
# ************************************************************************
    if preset.usePreset and strcmp(preset.file, 'noise'):
        isNoise = 'true'
        poolobj = gcp ('nocreate')
        if not isempty(poolobj):
            print('| ')
            delete(gcp('nocreate'))
        print('===============================================================\n')
        print('| Reconstruction finished at %s\n', datestr(datetime('now')))
        print('===============================================================\n')
    else:
        isNoise = 'false'
    return isNoise

        
    