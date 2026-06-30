import streamlit as st
import pandas as pd
import numpy as np
import sklearn.datasets as load_iris
import sklearn.svm as svm
import sklearn.metrics as metrics
import sklearn.ensemble as RandomForestClassifier


@st.cache
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names
    

df,target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1] , df)


