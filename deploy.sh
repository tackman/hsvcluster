#!/bin/sh
hy2py3 > main.py && \
gcloud functions deploy cluster --region asia-northeast1  --runtime python37 --trigger-http
