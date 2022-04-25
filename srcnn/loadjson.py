from ctypes import sizeof
import json
with open("/home/tongtong/python_project/anomalydetector/samples_128_train.json", 'r+') as fin:
    a = json.load(fin)

print(len(a[1][1]))