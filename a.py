import json_lines
import json
import numpy as np
import matplotlib.pyplot as plt
import os


#importing the json
data = '/Users/iknott/Desktop/Kaggle/stanford-covid-vaccine/test.json'
list_obj = []
with open(data) as f:
    for jsonObj in f:
        dict = json.loads(jsonObj)
        list_obj.append(dict)
print(list_obj[1])

#importing the np array
path = "Users/iknott/Desktop/Kaggle/stanford-covid-vaccine/bpps/"
data_np = np.load(path + "path id_00073f8be.npy")
plt.plot(data[0])
plt.show()
