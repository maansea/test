#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import training
import predict


# In[7]:


#Title of the Application
st.title("Customer Propensity to Purchase")


#Choice of page
page_choices={"Know more about the training data":training,
              "Predict the Propensity of Purchase":predict}


#Create radio button for the page choice
page_selection = st.radio("Go to", list(page_choices.keys()))


#Choosing the page based on the user selection from radio button
page = page_choices[page_selection]


#Display the page
with st.spinner(f'Loading {page_selection} ...'):
    page.app()


# In[ ]:





# In[ ]:




