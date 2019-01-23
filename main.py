import cv2
import sys
import sklearn
import sklearn.cluster
import numpy
import json


def image_path():
    return 'sample.jpg'


def loadLocal(rawData):
    return cv2.imread(image_path())


def loadBinary(rawData):
    return cv2.imdecode(rawData, cv2.IMREAD_COLOR)


load = loadBinary


def toHsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def runHsvCluster(image_data):
    img = toHsv(image_data)
    img_array = numpy.reshape(img, (img.shape[0] * img.shape[1], 3))
    kmeans = sklearn.cluster.KMeans(n_clusters=5)
    kmeans.fit(img_array)
    return kmeans


def cluster(req):
    kv = runHsvCluster(load(req.gget_data()))
    return json.dumps(kv.cluster_centers_)

