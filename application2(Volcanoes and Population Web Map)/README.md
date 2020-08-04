Application2 include 4 file: two database('Volcano.txt', 'World.json'), html file(map which can be opened in browser) and map1.py(code on python)


1) Creating basement layer of map(Great Political map with all country)    
       //end of fist layer

2) Reading database "Volcano.txt" and choosing 3 column from there(Latitude,Longitude and Elevation of the volcanoes)
   Creating 3 list with 3 column(Latitude,Longitude and Elevation of the volcanoes).
   Creating markers with help of function 'folium.CircleMarker' and enter parameters for our tastes(location, radius, popup, fill_color, color)
   Define function 'color_choice' for markers for divide volcanoes by height(Green, Orange and Red Markers)
       //end of second layer

3) Adding 'Geojson' polygon layer with help of "world.json"(need for divide basement layer map on countries)
   On map draw countries by population  on colors(Green, Orange and Red)
      //end of thrid layer

4) Creating two FeatureGroup for second and thrid layer(need for more comfortable operating on the map)
   Add 'LayerControl' function for divede map on layer
   
5) Save web map in "Map1.html".
