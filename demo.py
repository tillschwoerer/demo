import pandas as pd
import streamlit as st
import warnings
import altair as alt
warnings.filterwarnings('ignore')


@st.cache()
def prepare_data():
    df = pd.read_csv('used_cars.csv')
    sample = df.sample(n=2000, random_state=1)
    return sample


sample = prepare_data()


st.header('*Used Cars Streamlit App*')

st.markdown("""
This is my first streamlit app. I just 

- try
- out
- what is possible
- `some code`
""")

vehicle_types = sample.vehicleType.unique()

color_var = st.radio('Select Color Variable',
                     options=['vehicleType', 'brand'], horizontal=True)

vehicle_choices = st.multiselect(
    'Select multiple vehicle types', options=vehicle_types, default=vehicle_types)

vehicle_choices_altair = alt.selection_multi(
    fields=['vehicleType'], bind='legend')


fig = alt.Chart(
    sample[sample.vehicleType.isin(vehicle_choices)]
).mark_circle().encode(
    x=alt.X('age'),
    y=alt.Y('price'),
    color=alt.Color(color_var)
).add_selection(vehicle_choices_altair).transform_filter(vehicle_choices_altair)


st.altair_chart(fig)
