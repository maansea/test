#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import pickle
def app():
    option_visitor_type = st.sidebar.selectbox(
     'Is he a repeating customer?',
    ('Returning_Visitor', 'New_Visitor', 'Others'))
    option_weekend = st.sidebar.selectbox(
     'Did he purchase on weekend',
    ('Yes', 'No'))
    
if st.sidebar.button('Predict Propensity of the Customer to make a purchase'):
        lookup_dict={"Yes":1,"No":0}
        dict = {'option_visitor_type':[lookup_dict[option_basket]],
            'option_weekend':[lookup_dict[option_promo]]
            }
        prediction_df = pd.DataFrame(dict)
        st.write("Customer details for Propensity prediction")
        st.write(prediction_df)
        with open("propensity_model.pkl", 'rb') as pfile:  
            propensity_model_loaded=pickle.load(pfile)
        y_predicted=propensity_model_loaded.predict(prediction_df)
        if (y_predicted[0]==1): 
            st.write("The customer will order from the website. Probabality of ordering:")
        else:
            st.write("The customer will not order from the website. Probabality of ordering:")
        st.write(propensity_model_loaded.predict_proba(prediction_df))


# In[ ]:




