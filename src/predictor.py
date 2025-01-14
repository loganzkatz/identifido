import numpy as np
from keras.models import load_model
import sys
import json
from PIL import Image

def predict(img_path):
    with open('/Users/lzkatz/Desktop/Galvanize/Capstone/Identifido/aux_files/breed_dict.json') as bd:
        classes = json.load(bd)
    model_dir = '/Users/lzkatz/Desktop/Galvanize/Capstone/Identifido/model/deep_nodense/temp_model.hdf5'

    model = load_model(model_dir)
    
    img = Image.open(img_path)
    img = img.resize((model.input_shape[3], model.input_shape[2]))
    img = np.asarray(img, dtype='float32')
    img /= 255.
    img = np.transpose(img, (2,0,1))
    img = np.array([img])

    class_pred = model.predict(img)
    class_pred = class_pred.flatten()
    sort_pred = np.argsort(class_pred)[:-6:-1]

    breed_pred = []
    for i in sort_pred:
        breed_pred.append((classes[str(i)], class_pred[i]))
    
    return breed_pred

if __name__ == '__main__':
    pic_dir = '/Users/lzkatz/Desktop/Galvanize/Capstone/Identifido/data/test/'
    pic = sys.argv[1]
    pic_path = pic_dir + pic
    results = predict(pic_path)
    print results
