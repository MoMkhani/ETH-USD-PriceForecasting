# -*- coding: utf-8 -*-
"""Feature Engineering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A2Uw-sUxi6iu-OmeodPQaW5vRTfpMQwS

# **6. Feature Engineering**
"""

# Create main set to train and validate
eth_main = eth.loc['2017-08-17':'2021-10-15']

# Create holdout set
eth_recent = eth.loc['2021-10-16':]

# Preparing dataset
split = int(eth_main.shape[0]*0.8)
df_train = eth_main[:split]
df_test = eth_main[split:]

# Write a function to generate desired dataset
def create_dataset(df, n, feature=-1):
   """Create proper dataset for supervised time series forcasting.

   Args:
   df: input dataframe
   n: number of values to consider in a window as features
   feature: chosen column (feature) to perform
   
   Return:
   x, y = returns x as features and y as target variable
   """
   x = []
   y = []

   for i in range(n, df.shape[0]):
     x.append(df[i-n:i, feature])
     y.append(df[i, feature])
   x = np.expand_dims(np.array(x), -1)
   y = np.expand_dims(np.array(y), -1)  
   return x, y

# Scale before modeling
scaler = MinMaxScaler(feature_range=(0,1))
dataset_train = scaler.fit_transform(df_train)

# Scale validation set
dataset_test = scaler.transform(df_test)

# Create train and test sets using our function
X_train, y_train = create_dataset(dataset_train,50,-1)
X_test, y_test = create_dataset(dataset_test,50,-1)

# Check if it worked!
X_train.shape