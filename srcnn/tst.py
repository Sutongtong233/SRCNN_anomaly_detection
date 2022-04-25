import pickle
with open('/home/tongtong/python_project/anomalydetector/snapshot/srcnn_retry5_128.bin', 'rb') as f:
    # f.seek(0)
    print(f)
    a = pickle.load(f)
print(a)