import argparse
import glob
import os
import pickle
import random

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from SVM.pyimagesearch.rgbhistogram import RGBHistogram

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-f", "--females", required=True, help="number of images of females.(Max 5407)"
)
ap.add_argument(
    "-m", "--males", required=True, help="number of images of males.(Max 4372)"
)
args = vars(ap.parse_args())

path = "../data/images"
imagePaths = sorted(glob.glob(path + "/*.jpg"))

# Sort out the data based on gender
# number of images of males: 4372
# number of images of females: 5407
males = []
females = []
for imagePath in imagePaths:
    if imagePath.split("_")[1] == "0":
        males.append(imagePath)
    if imagePath.split("_")[1] == "1":
        females.append(imagePath)

# Select random images from the sorted data. Number will be taken from the user.
random_females = random.sample(females, int(args["females"]))
random_males = random.sample(males, int(args["males"]))

imagePaths = np.concatenate((random_males, random_females))

desc = RGBHistogram([8, 8, 8])

data = []
target = []
for imagePath in imagePaths:
    # load the image
    image = cv2.imread(imagePath)
    # describe the image

    features = desc.describe(image)

    data.append(features.flatten())
    target.append(imagePath.split("_")[1])

targetNames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)

SVM_model = pickle.load(open("SVM/SVM_model.pkl", "rb"))
RM_model = pickle.load(open("RandomForest/RandomForest_model.pkl", "rb"))

models = [SVM_model, RM_model]

females = []
males = []
for i in models:
    score_1 = precision_score(target, i.predict(data), pos_label=1)
    females.append(score_1)
    score_0 = precision_score(target, i.predict(data), pos_label=0)
    males.append(score_0)

ind = np.arange(len(males))  # the x locations for the groups
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, males, width, label="Men")
rects2 = ax.bar(ind + width / 2, females, width, label="Women")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Scores")
ax.set_title("Precision scores by classifier and gender")
ax.set_xticks(ind)
ax.set_xticklabels(("SVM", "RandomForest"))
ax.legend()
plt.show()
plt.savefig("../plots/plot.png")
