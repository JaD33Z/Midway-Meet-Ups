from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import folium
from geopy.geocoders import Nominatim
from forms import LocationForm, MidwayForm
import requests
from dotenv import load_dotenv
from os import environ

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
Bootstrap(app)

geolocator = Nominatim(user_agent="meet_app_here")
NOMINATIM_ENDPOINT = "https://nominatim.openstreetmap.org"


@app.route('/', methods=["GET", "POST"])
def home():
    form = LocationForm()
    if form.validate_on_submit():
        start_point = form.start_point.data
        end_point = form.end_point.data
        your_location = geolocator.geocode(start_point)
        their_location = geolocator.geocode(end_point)
        start_cords = (your_location.latitude, your_location.longitude)
        end_cords = (their_location.latitude, their_location.longitude)
        folium_map = folium.Map(location=start_cords, zoom_start=14)
        folium.Marker(start_cords).add_to(folium_map)
        folium.Marker(end_cords, icon=folium.Icon(color="red")).add_to(folium_map)
        return folium_map._repr_html_()
    return render_template('index.html', form=form)



@app.route('/midway', methods=["GET", "POST"])
def midway():
    form = MidwayForm()
    if form.validate_on_submit():
        town_name = form.town_name.data
        state_name = form.state_name.data
        place_category = form.place_category.data
        search_query = f"/search.php?q={town_name}+{state_name}+{place_category}&format=jsonv2"
        request_url = f"{NOMINATIM_ENDPOINT}{search_query}"
        response = requests.get(request_url)
        request_response = response.json()
        meet_point = geolocator.geocode(town_name + state_name)
        folium_map = folium.Map(location=meet_point, zoom_start=18)

        results = [(i['lat'], i['lon'], i['display_name']) for i in request_response]
        for (k,v,n) in results:
            folium.Marker((k,v), popup=f"<a href=https://boulter.com/gps/#{k}%2C%{v}>{n}!</a>",
                          tooltip=(n)).add_to(folium_map)

        return folium_map._repr_html_()
    return render_template('midway.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
