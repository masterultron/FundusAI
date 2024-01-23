from fastai.vision import *
from fastai.imports import *
from fastai.learner import *
from fastai.vision.all import *

import numpy as np
import matplotlib.image as mpimg
import os
import time
from PIL import Image

import pathlib
import random


basedir = os.path.dirname(__file__)

# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

# For linux deployment
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

# path = Path('.')
path = os.getcwd()

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

#------Create/Define all functions

def get_x(r): 
    return image_path/r['train_image_name']

def get_y(r): 
    return r['class']

def get_features(r): return image_path/r['image']

def get_output(r): return r['quality']

def loadBinaryModel():
    binaryModel = load_learner(f"{path}/diagnosis/AI_Models/Binary_Prediction_Model.pkl")
    return binaryModel

def loadMultiModel():
    multiModel = load_learner(f"{path}/diagnosis/AI_Models/Severity_Prediction_Model.pkl")
    return multiModel

def loadQualityModel():
    qualityModel = load_learner(f"{path}/diagnosis/AI_Models/Quality_Assessment.pkl")
    return qualityModel

binaryModel = loadBinaryModel()
multiModel = loadMultiModel()
qualityModel = loadQualityModel()


# Dummy functions
def isHighQualityImage(imageName):

    img = PILImage.create(imageName)

    pred, pred_idx, prob = qualityModel.predict(img)

    # Extract the probability value directly without formatting
    pred_prob_value = prob[pred_idx].item() * 100

    # Format the value as a string for printing or further use
    pred_prob_string = f"{pred_prob_value:.0f}%"

    print("Quality Stats: ", pred, pred_prob_string)
    
    # Display the prediction
    if pred == '0' or pred == '1':
        # TO-DO: Add prediction threshold (>=70%)
        return True

    elif pred == '2':
        return False


def isRetinopathyPresent(image):
    img = PILImage.create(image)

    pred, pred_idx, prob = binaryModel.predict(img)

    # Extract the probability value directly without formatting
    pred_prob_value = prob[pred_idx].item() * 100

    # Format the value as a string for printing or further use
    pred_prob_string = f"{pred_prob_value:.0f}%"

    print("Retinopathy Stats: ", pred, pred_prob_string)

    # pred = pred
    # pred_prob = pred_prob

    print("Binary Pred:", int(pred))
    
    # Display the prediction
    if int(pred) == 1:
        pred_output = True

        if prob[pred_idx]*100 <= 85.0:
            rec_action = 'Please visit an Opthalmologist to confirm your Daignosis'
        else:
            rec_action = 'Please visit an Opthalmologist for prompt treatment.'

        return pred_output, rec_action

    else:
        # pred_output = 'Absence of Diabetic Retinopathy'
        pred_output = False

        if prob[pred_idx]*100 <= 85.0:
            rec_action = 'Please visit an Opthalmologist to confirm your Daignosis'
        else:
            rec_action = 'Please be sure to go for Diagnosis once a year.'
        
        return pred_output, rec_action
    


def severityLevel(image):
    # results = {
    #     'benign': 'No cause for concern',
    #     'moderate': 'Consult you doctor regularly and adopt a new meal plan.',
    #     'Non-proliferative Diabetic Retinopathy': 'Please see your doctor as soon as possible, and take another test in 6 months'
    # }

    # options = []
    # for [key, value] in results.items():
    #     options.append([key, value])

    # return random.choice(options)
    
    img = PILImage.create(image)

    pred, pred_idx, prob = multiModel.predict(img)

    # Extract the probability value directly without formatting
    pred_prob_value = prob[pred_idx].item() * 100

    # Format the value as a string for printing or further use
    pred_prob_string = f"{pred_prob_value:.0f}%"

    print("Severity Stats: ", pred, pred_prob_string)

    return [pred, isRetinopathyPresent(image)[1]]