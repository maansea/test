#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st
import pandas as pd
#import altair as alt
import matplotlib.pyplot as plt


st.set_option('deprecation.showPyplotGlobalUse', False)


def app():
    #Header
    st.write("Training data used")


    #Reading the data
    df=pd.read_csv("online_shoppers_intention.csv")


    #display the data as a table
    st.write(df.head(30))


    #header
    st.write("Distribution of Repeated Customer (Dependent variable)")


    #bar plot
    temp=df["VisitorType"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(["Returning_Visitor","New_Visitor"],temp,color ='maroon',width = 0.4)
    plt.xlabel("Order status")
    plt.ylabel("No. of customers")
    st.pyplot()


# In[ ]:





# In[ ]:





# In[ ]:




