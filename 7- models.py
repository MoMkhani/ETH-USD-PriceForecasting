# -*- coding: utf-8 -*-
"""Models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A2Uw-sUxi6iu-OmeodPQaW5vRTfpMQwS

# **8. Models**

## **8.1 XGBOOST**
"""

# Instantiate an xgboost regressor object
xgb_model = xgboost.XGBRegressor()
# Fit the training date
xgb_model.fit(np.squeeze(X_train), np.squeeze(y_train))

# Evaluate the results
evaluate_model(xgb_model, model_name="XGBoost", test_data=np.squeeze(X_test), target_data=np.squeeze(y_test))

"""## **8.2 LSTM**"""

# Instantiate sequential model
LSTM_Model = Sequential()

# Define lstm model
LSTM_Model.add(LSTM(units=96,
                    return_sequences=True,
                    input_shape=(X_train.shape[1], 1)))
LSTM_Model.add(Dropout(0.2))
LSTM_Model.add(LSTM(units=96, 
                    return_sequences=True))
LSTM_Model.add(Dropout(0.2))
LSTM_Model.add(LSTM(units=96, 
                    return_sequences=True))
LSTM_Model.add(Dropout(0.2))
LSTM_Model.add(LSTM(units=96))
LSTM_Model.add(Dropout(0.2))
LSTM_Model.add(Dense(units=1))

# Config the model
LSTM_Model.compile(loss=MSE, optimizer=Adam())

# Fit the model
LSTM_Model.fit(X_train,y_train,batch_size=32,epochs=10,verbose=1,validation_split=0.05)

# Evaluate the model and plot the results
evaluate_model(LSTM_Model, "LSTM")

"""## **8.3 CNN**"""

# Instantiate sequential model
CNN_model=Sequential()

# Define cnn model
CNN_model.add(Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=X_train[0].shape))
CNN_model.add(MaxPooling1D(3))
CNN_model.add(Dropout(0.1))
CNN_model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
CNN_model.add(MaxPooling1D(3))
CNN_model.add(Dropout(0.1))
CNN_model.add(Flatten())
CNN_model.add(Dense(32, activation='relu'))
CNN_model.add(Dense(1, activation='relu'))

# Config the model
CNN_model.compile(optimizer='adam', loss='mse')

# Fit the model
CNN_model.fit(X_train, y_train, epochs=20, validation_split=0.1)

# Evaluate the model and plot the results
evaluate_model(CNN_model, "CNN")

# Save models
# LSTM_Model.save('LSTM.h5')
# CNN_model.save('CNN.h5')