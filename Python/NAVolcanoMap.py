import folium, pandas

def color(elevation=0.0):
	if(elevation <= 1000):
		return 'green'
	elif(elevation > 1000 and elevation < 2000):
		return 'orange'
	else:
		return 'red'

volcData = pandas.read_csv("Volc.txt")
# print(volcData.columns)
# lat = volcData['LAT']
# lon = volcData['LON']

map = folium.Map(location=[37,-107.522775], zoom_start=3, 
				 tiles="Mapbox Bright")

featureGroup = folium.FeatureGroup(name="Volcanoes")

for lt,ln,loc,elv in zip(volcData['LAT'], volcData['LON'], 
					 volcData['LOCATION'], volcData['ELEV']):

	loc = loc.strip()
	info = loc + '\n' + str(elv)

	featureGroup.add_child(folium.Marker(location=[lt,ln], 
										 popup=str(info) + 'm',
										 #popup=folium.Popup(str(elv),parse_html=True))
										 icon=folium.Icon(color=color(elv))))

	# featureGroup.add_child(folium.CircleMarker(location=[lt,ln], 
	# 									 radius=6,
	# 									 popup=str(info),
	# 									 #fill_color='red',
	# 									 color='black',
	# 									 fill_opaccity=0.7))

	

map.add_child(featureGroup)

map.save("Map1.html")