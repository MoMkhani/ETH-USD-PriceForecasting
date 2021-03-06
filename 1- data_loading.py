# -*- coding: utf-8 -*-
"""Data Loading.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A2Uw-sUxi6iu-OmeodPQaW5vRTfpMQwS

#**1 Data Loading**

##**1.1 Loading Libraries**
"""

import pandas as pd
import numpy as np
import math
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import *

from sklearn.metrics import  mean_absolute_error, r2_score 
from sklearn.preprocessing import MinMaxScaler

import statsmodels.api as sm

# Models
import xgboost
from tensorflow.keras.layers import LSTM, Activation, Dense, Dropout, Conv1D, MaxPooling1D, Flatten, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import MSE
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.activations import relu

plt.style.use('seaborn-darkgrid')

"""##**1.2 Loading Dataset**"""

# Load dataset from github
url = 'https://raw.githubusercontent.com/MoMkhani/ETH-USD-PriceForecasting/main/Data/Binance_ETHUSDT_1h.csv'
df = pd.read_csv(url)
# Last five rows
df.head()