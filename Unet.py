import numpy as np

from keras.models import load_model

Unet = load_model('Unet.h5')
Unet.summary()

#Load the data

#Loading the data

import os

def get_data(Test_or_Train, img_type, n):
    imgs = []
    name = {'T1' : 'sub-{}_T1w.npy', 
            'grey' : 'c1sub-{}_T1w.npy', 
            'white' : 'c2sub-{}_T1w.npy',
            'csf' : 'c3sub-{}_T1w.npy'}
        
    for i in range(n):
        i += 1
        
        if Test_or_Train == 'Test':
            i += 60
        
        if i < 10:
            numb = '0' + str(i)
        else:
            numb = str(i)
        
        if img_type == 'T1':
            subfolder = 'imgs'
            filename = os.path.join(Test_or_Train,subfolder,name[img_type].format(numb))
        else: 
            subfolder = 'masks'
            filename = os.path.join(Test_or_Train,subfolder,img_type,name[img_type].format(numb))
            
        print('Loading {}'.format(name[img_type].format(numb)))
        
        img = np.load(filename)
        
        #Normalize the images to values in [0,1]
        imgNorm = img / img.max()
        imgNorm = np.expand_dims(imgNorm, axis = 3) #To add the channel dimension (of length 1)
        imgs.append(imgNorm[0:16,:,:])
        
    print('\n Loaded {} {} images of type {}'.format(n, Test_or_Train, img_type))
    print('-'*30)
    return imgs

x_train = get_data('Train', 'T1', 1)
y_train = get_data('Train', 'grey', 1)

#De lijn code die alles crasht
print('-'*30)
print('Fitting model...')
print('-'*30)

Unet.fit([x_train], [y_train], batch_size=1, epochs=2, verbose=1, shuffle=True) #validation_split=0.10

print('-'*30)
print('Training finished')
print('-'*30)
