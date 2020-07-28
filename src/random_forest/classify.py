from __future__ import print_function
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import argparse
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required = True,
	help = "path to the training image dataset")
args = vars(ap.parse_args())

# grab the image
imagePaths = sorted(glob.glob(args["images"] + "/*.jpg"))

# initialize the list of data and class label targets
data = []
target = []

# initialize the image descriptor

# loop over the image
for imagePath in imagePaths:
    # load the image
    image = cv2.imread(imagePath)
    # describe the image
    # update the list of data and targets
    mean = (104, 117, 123)
    features = cv2.dnn.blobFromImage(image, 1.0, (227,227), mean, swapRB=False)

    data.append(features.flatten())
    target.append(imagePath.split("_")[1])


# grab the unique target names and encode the labels
targetNames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)


# construct the training and testing splits
(trainData, testData, trainTarget, testTarget) = train_test_split(data, target,
	test_size = 0.3, random_state = 42)

# train the classifier
model = RandomForestClassifier(n_estimators = 25, random_state = 84)
model.fit(trainData, trainTarget)


# evaluate the classifier
print(classification_report(testTarget, model.predict(testData),
	target_names = targetNames))

# loop over a sample of the images
for i in np.random.choice(np.arange(0, len(imagePaths)), 10):
    # grab the image
    imagePath = imagePaths[i]

    # load the image
    image = cv2.imread(imagePath)

    # describe the image
    # features = desc.describe(image)
    mean = (104, 117, 123)
    features = cv2.dnn.blobFromImage(image, 1.0, (227,227), mean, swapRB=False)


    gender = le.inverse_transform(model.predict([features.flatten()]))[0]
    print(imagePath)
    print("I think person on this photo is {}".format(gender.upper()))
    cv2.imshow("image", image)
    cv2.waitKey(0)
