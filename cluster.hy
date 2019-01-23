(import cv2)
(import sys)
(import sklearn)
(import sklearn.cluster)
(import numpy)
(import json)

(defn image-path [] "sample.jpg")
(defn loadLocal [rawData] (cv2.imread (image-path)))
(defn loadBinary [rawData] (cv2.imdecode rawData cv2.IMREAD_COLOR))

(setv load loadBinary)

(defn toHsv [img]
  (cv2.cvtColor img cv2.COLOR_BGR2HSV))

(defn runHsvCluster [image-data]
  (setv img (toHsv image-data))
  (setv img-array (numpy.reshape img (, (* (. img.shape [0]) (. img.shape [1])) 3)))
  (setv kmeans (sklearn.cluster.KMeans :n_clusters 5))
  (kmeans.fit img-array)
  kmeans)

(defn cluster [req] 
  (setv kv (runHsvCluster (load (req.gget_data))))
  (json.dumps kv.cluster_centers_)
)
