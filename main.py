import cv2
import sys
import sklearn
import sklearn.cluster
import numpy


def image_path():
    return 'sample.jpg'


def loadLocal(rawData):
    return cv2.imread(image_path())


load = loadLocal


def toHsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def runHsvCluster(image_data):
    img = toHsv(image_data)
    img_array = numpy.reshape(img, (img.shape[0] * img.shape[1], 3))
    kmeans = sklearn.cluster.KMeans(n_clusters=5)
    kmeans.fit(img_array)
    return kmeans


def cluster(req):
    return req.get_data()


kv = runHsvCluster(load('placeholder'))
print(kv.cluster_centers_)

