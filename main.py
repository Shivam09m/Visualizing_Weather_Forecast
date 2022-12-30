import streamlit as st
import plotly.express as px
from backend import get_data

# Add Title, text input, slider, select box, sub-header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of Forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/Sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        temperatures = [x-273 for x in temperatures]
        dates = [dict["dt_txt"] for dict in filtered_data]

        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_conditions]
        st.image(image_path, width=115)
