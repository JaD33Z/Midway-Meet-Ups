# Midway-Meet-Ups
Search for places between two points in a selected area to meet up.

This project uses an API along with several libraries that interact with web services that facilitate geolocation functionality. Geopy library communicates with Nominatim API to extract info from Open Street Map. Folium library produces the HTML map images with js.Leaflet. 
Built with Python and Flask.

</br>


 Geopy library is a python client for several popular geolocation web services. Geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources. These services each have a class within geopy.geocoders.  Geocoders each define a geocode method, for resolving a location from a string, and may define the latitude and longitude coordinates to an address. It also abstracts the services of, in the case of this app, the Nominatin API.  
 
   
 Nominatim API indexes named or numbered features, and subsets of categories like, hotels, restaurants, parks, etc. within the Open Street Map dataset. It's a tool to search Open Street Map data to generate the name and address of OpenStreetMap points.
 
 OpenStreetMap is a free, editable map of the whole world that is being built by volunteers largely from scratch and released with an open-content license. It gives you free access to map images and all their underlying map data.
 
 The Folium Library is for visualizing geospatial data. It's a python wrapper to communicate with Leaflet.js
 
 Leaflet is an open source JavaScript library used to build web mapping applications. It renders map elements to html and css and displays interactive map images.

</br>

## App functionality
 The entered text of location submitted by form is passed to geocode which resolves the named address to it's coordinates, which will be used by folium to display the Leaflet map image of the span between both locations. You choose a town midway and the type of places you want to check out, and once submitted, a query string is constructed with location parameters and sent to Nominatim's endpoint to request the data from Open Street Map. The OSM response data is converted to json format to be parsed through and passed to Folium to be displayed on the Leaflet interactive map page containing location markers with their corresponding info. The location markers are labeled with name, address and clickable links to redirect you along with the location data to Map Quest for further information and directions to meet point.
 

</br>

Enter two locations into the form, your location and the location of whom you are going to meet with.
Then Meet Ups will produce an interactive map image with those two points marked out.

</br>

![first-page-form](https://user-images.githubusercontent.com/74392848/133685546-85f47fca-f94a-4384-b8a0-f0afbec06e58.png)

</br>




</br>

![first-map-view](https://user-images.githubusercontent.com/74392848/133685702-3d97690c-c0b4-4513-9d73-266bd64b8b18.png)

</br>

You can search and choose any 
location between that distance by entering the name of the town or city and what type of place 
(restaurant, pub, park, mall, library, bicycle trail,etc.) you are searching for to meet up at. 
Submit and Meet Ups will produce another interactive map image with all the searched category's results located in the chosen area.


</br>

![better-midway-form](https://user-images.githubusercontent.com/74392848/133685828-4b3047d2-ec6a-4687-8783-410516d0549b.png)

</br>

Hover with mouse over the map markers for names and full addresses to pop up on the map, with clickable links to get more info, pictures, directions, etc.

</br>

![better-midway-map-view](https://user-images.githubusercontent.com/74392848/133685906-77fa2e8e-c33b-470e-ac48-212d37a75f1d.png)

</br>

By clicking link on leaflet map image you will be taken to boulter.com geocaching GPS Coordinate Converter, where your chosen location's data page will be present with several options.
You can just click the Map Quest link under your locations map image and you'll be provided with directions and details from your start location to meet up destination. 


</br>

![map-quest-directions](https://user-images.githubusercontent.com/74392848/133685939-508d87a3-07ea-461f-9766-d04ef0bcce4a.png)

</br>



