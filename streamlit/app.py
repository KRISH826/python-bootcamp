import streamlit as st
import pandas as pd
import numpy as np

# title
st.title("My First App")
# st.markdown("This is my first app")
st.write("This is my first app")

# example of data frame
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
st.write("Here This Data Table")
st.write(df)


data_chart = pd.DataFrame(
    np.random.randn(50, 3),columns=['a', 'b', 'c']
)
st.line_chart(data_chart)

