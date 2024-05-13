# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7ON_jduNxOVODkcmYqhKv5-2rWD5vg8
"""

import pandas as pd
df10=pd.read_csv('my_data.csv')
df10

X = df10.drop(['price'],axis='columns')
y=df10.price

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=10)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)
model.score(X_test,y_test)

# Predict y values using the trained model
y_pred = model.predict(X)



import streamlit as st
import pandas as pd

# Function to preprocess user input and make predictions
def predict_price(location, total_sqft, bath, bhk):
    # Create a dataframe with the input features
    input_data = pd.DataFrame({
        'total_sqft': [total_sqft],
        'bath': [bath],
        'bhk': [bhk],
        location: [1]
    })
    # Use the trained model to make predictions
    predicted_price = model.predict(input_data)
    return predicted_price[0]

if __name__ == '__main__':
    st.title('Property Price Predictor')

    # Input fields
    location = st.text_input('Location', 'Enter location here...')
    total_sqft = st.number_input('Total Square Feet', value=1000)
    bath = st.number_input('Number of Bathrooms', value=2)
    bhk = st.number_input('Number of Bedrooms (BHK)', value=2)

    # Predict button
    if st.button('Predict Price'):
        # Call the predict_price function
        predicted_price = predict_price(location, total_sqft, bath, bhk)
        st.success(f'Predicted Price: {predicted_price}')
