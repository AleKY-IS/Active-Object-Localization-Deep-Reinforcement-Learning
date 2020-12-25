# -*- coding: utf-8 -*-
from IPython.display import clear_output
from utils.agent import *
from utils.dataset import *
from utils.models import *


import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple
from itertools import count
from PIL import Image
import torch.optim as optim
import cv2 as cv
import sys
from torch.autograd import Variable
import traceback
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#!pip3 install torch==1.5.1 torchvision==0.6.1 -f https://download.pytorch.org/whl/cu92/torch_stable.html

batch_size = 32
PATH="./datasets/"



train_loader2012, val_loader2012 = read_voc_dataset(download=LOAD, year='2012')
train_loader2007, val_loader2007 = read_voc_dataset(download=LOAD, year='2007')


classes = ['cat', 'bird', 'motorbike', 'diningtable', 'train', 'tvmonitor', 'bus', 'horse', 'car', 'pottedplant', 'person', 'chair', 'boat', 'bottle', 'bicycle', 'dog', 'aeroplane', 'cow', 'sheep', 'sofa']

agents_per_class = {}
datasets_per_class = sort_class_extract([val_loader2007, val_loader2012])
index = 10
image, [oxmin, oxmax, oymin, oymax] = extract(index, datasets_per_class['cat'])
agent = Agent('cat', alpha=0.02, num_episodes=25, load=True)
agent.predict_image(image)