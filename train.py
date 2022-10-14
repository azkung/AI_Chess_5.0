import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
import time
from model import Net


def run_train(modelPath, xPath, yPath, epochs, prevModelPath = None):
    train_x = np.load(xPath)
    train_y = np.load(yPath)
    print(train_x.shape)
    print(train_y.shape)

    tensor_x = torch.Tensor(train_x)
    tensor_y = torch.Tensor(train_y)

    trainSet = TensorDataset(tensor_x, tensor_y)
    trainLoader = DataLoader(trainSet, batch_size=10, shuffle=True)

    net = Net()

    if(prevModelPath != None):
        net.load_state_dict(torch.load(prevModelPath))

    optimizer = optim.Adam(net.parameters(), lr =0.0001)

    criterion = nn.BCELoss()

    for epoch in range(epochs):
        for idx, data in enumerate(trainLoader):
            X, y = data
            net.zero_grad()
            output = net(X)
            loss = criterion(output, y.unsqueeze(1))
            loss.backward()
            optimizer.step()
        print("Epoch: ", epoch + 1, "| Latest Loss: ", loss)
        # total = 0

        # with torch.no_grad():
        #     for data in trainLoader:
        #         X, y = data

        #         output = net(X)
        #         diff = abs(output[0][0]- y[0])
        #         total += diff

        # print("Epoch: ", epoch + 1, "| Average difference: ", total/len(train_y))

    torch.save(net.state_dict(), modelPath)