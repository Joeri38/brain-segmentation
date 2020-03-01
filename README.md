# Brain segmentation

This repository contains the training and test data to create a convolutional neural network that segments MRI images of the brain into white matter, grey matter and cerebrospinal fluid (CSF). Details of the network can be found at: 

https://joeri38.github.io/brainSegmentation-website/

The data consists of 60 3D images of brain MRI scans as a training set and 14 MRI scans as a test set. The images are accompanied by ground truth, consisting of the segmentation into white matter, grey matter and cerebrospinal fluid (CSF). The data is stored as numpy arrays. In the map 'anatomischeScans', the data is also available as NifTi .nii files. 

