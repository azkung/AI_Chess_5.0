import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
import math
from model import Net



def run_test(modelPath, xPath, yPath):
    test_x = np.load(xPath)
    test_y = np.load(yPath)
    print(test_x.shape)
    print(test_y.shape)

    tensor_x = torch.Tensor(test_x)
    tensor_y = torch.Tensor(test_y)

    testSet = TensorDataset(tensor_x, tensor_y)
    testLoader = DataLoader(testSet, batch_size=1, shuffle=True)

    net = Net()
    net.load_state_dict(torch.load(modelPath))

    total = 0
    count = 0
    with torch.no_grad():
        for data in testLoader:
            X, y = data
            output = net(X)
            diff = abs(output[0][0]- y[0])
            total += diff
            count += 1

    print("Average difference: ", total/count)
    
# run_test("models/1665154011re", "numpy/basic_test_x.npy", "numpy/basic_test_y.npy")