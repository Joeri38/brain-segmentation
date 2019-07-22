import numpy as np
import nibabel as nib
import os

#Specify how many images to save in train and how many to save in test

n = int(input('Images to save in train: '))
m = int(input('Images to save in test: '))
print('Saving {} images in train and {} images in test'.format(n,m))

#Takes a filename and copies it from startDir to endDir
def save_imgarray(name, startDir, endDir):
    filename = os.path.join(startDir, name + '.nii')
    img = nib.load(filename)
    imgArr = img.get_fdata()
    savename = os.path.join(endDir, name + '.npy')
    np.save(savename, imgArr)

Start = 'anatomischeScans'
tissue = {'grey' : 1, 'white' : 2, 'csf' : 3}

#This function saves the files to either test or train folder
#These two folders have an identical structure
#Number is the number of images to be saved and add is the img
#number from which you start counting
def main(Test_or_Train, number, add):

    greyEnd = os.path.join(Test_or_Train, 'masks', 'grey')
    whiteEnd = os.path.join(Test_or_Train, 'masks', 'white')
    csfEnd = os.path.join(Test_or_Train, 'masks', 'csf')
    imgEnd = os.path.join(Test_or_Train, 'imgs')

    for i in range(number):
        i += add + 1
        if i < 10:
            numb = '0' + str(i)
        else:
            numb = str(i)
            
        print('Saving image number {} in {}'.format(numb, Test_or_Train))
        
        greyName = 'c{0}sub-{1}_T1w'.format(tissue['grey'], numb)
        save_imgarray(greyName, Start, greyEnd)

        whiteName = 'c{0}sub-{1}_T1w'.format(tissue['white'], numb)
        save_imgarray(whiteName, Start, whiteEnd)

        csfName = 'c{0}sub-{1}_T1w'.format(tissue['csf'], numb)
        save_imgarray(csfName, Start, csfEnd)

        imgName = 'sub-{}_T1w'.format(numb)
        save_imgarray(imgName, Start, imgEnd)

main('Train', n, 0)
main('Test', m, n)

print("All images are saved")



    





    
