import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="viz demo")
#property_type	sector	bedRoom	bathroom	balcony	agePossession	built_up_area
# servant room	store room	furnishing_type	luxury_category	floor_category
with open('df2.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline2.pkl','rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs')

# property_type
property_type = st.selectbox('Property type',['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

# bedRoom
bedrooms = st.selectbox('Number of Bedrooms',sorted(df['bedRoom'].unique().tolist()))

# bathroom
bathroom = st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist()))

# balcony
balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

# agePossession
property_age = st.selectbox('Age of Property',sorted(df['agePossession'].unique().tolist()))

# built_up_area
built_up_area = float(st.number_input('Built-up Area'))

# servant room
servant_room = st.selectbox('Servant room',['0.0','1.0'])

# store room
store_room = st.selectbox('Store room',['0.0','1.0'])

# furnishing_type
furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

# luxury_category
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))

# floor_category
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room,
             furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)

    # predict
    # st.text(np.expm1(pipeline.predict(one_df)))
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The price of the property is between {} Cr and {} Cr".format(round(low,2),round(high,2)))
