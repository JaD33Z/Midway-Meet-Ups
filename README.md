# Midway-Meet-Ups
Search for places between two points in a selected area to meet up.

Enter two locations into the form, your location and whom you are going to meet with.
Then Meet Ups will show a map with those two points marked out. You can search and choose any 
location between that distance by entering the name of the town or city and what type of place 
(restaurant, pub, park, mall, library, bicycle trail,...etc.) you are searching for to meet at, 
and Meet Ups will produce a map image with all the searched category's locations marked in the area.
Hover with the mouse and name and full address will pop up on the map, with clickable link to get more info,
pictures, directions, etc. Based on passing latitude and longitude coordinates, Geopy library communicates with
Nominatim API to extract info from Open Street Map. Folium libray produces the HTML map images with js.Leaflet. 
Built with Python and Flask. 
