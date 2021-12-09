
# Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


header = st.container()
dataset = st.container()
visuals = st.container()

with header:
	st.title('Lung cancer logistics')

	st.header('Introduction')

	st.caption('Lung Cancer is a condition that affects the lungs and the entire chest cavity.Lung cancer is when abnormal cells divide in an uncontrolled way to form a tumour in the lung.The main symptoms are a cough, breathlessness and weight loss. The treatment you need depends on what type you have as well as your general health. Treatments include surgery, chemotherapy and radiotherapy.')




with dataset:

 	st.title('Project overview and data.')
st.caption('The objective of our study is to assess the duration of stay that treatment procedures take to help hospitals  channel their resources and patients to plan accordingly.')
st.caption('It will also assess the outcome of the cancer patients after discharge from the hospital following various treatment procedures.')
# Loading the dataset
st.header('A preview of the dataset.')
url='/home/francis/Desktop/lung_cancer_project/Lung-Cancer-/Clean dataset.csv'
#url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url,index_col=0)
df_poland =  df.copy()
preview=df_poland.head()
st.table(preview)
#
#

# objects= [cols for cols in df_poland if df_poland[cols].dtypes=='O']

#st.bar_chart(df[['Date of surgery','Total hospital stay']])


with visuals:
	st.header('Checking the trend of postoperative stay for each surgery between 2019 and 2020')
# time series plot for trend of post operative stays between 2019 and 2020 
figure=plt.figure(figsize=(10,8))
sns.lineplot(x=df_poland['Date of surgery'], y=df_poland['Postoperative hospital stay'], hue=df_poland['Type of surgery'])
plt.title("Trend of surgeries between 2019 and 2020",fontsize=15)
plt.show()
st.pyplot(figure)

# Bar plot to check  the frequency of total hospital days
with visuals:
	st.header('Checking the most frequent hospital stay time in days.')
fig, ax = plt.subplots()
ax.hist(df['Total hospital stay'], bins=50)

st.plotly_chart(fig)



# plotting to see the trend of people who stayed long in the hospital and whether they were alive or dead at the end

st.header("Checking the distribution of Total hospital stays vs outcome.")
fig = px.scatter(
    data_frame=df, x="Total hospital stay", y="Outcome at discharge",
)
st.plotly_chart(fig)




# plotting to see the type of surgery that makes people stay for long in hospital

st.header('Comparing the types of surgery and the duration it takes')
fig = px.scatter(
	data_frame=df, x="Postoperative hospital stay", y="Type of surgery",
)
st.plotly_chart(fig)

# checking the type of operations that had the most survivers vs deaths
