import gmaps

gmaps.configure(api_key='AIzaSyBvJ4s8ets2vpwWXV74F5b9JpD0QbehCDg')
plantation_sites = [{'name':'SAF Lines, Katulbod', 'area':'Sector 9, Bhilai, Chhattisgarh', 'location': (21.195806, 81.308889)},
                    {'name':'Street no. 23, near Mamta garden', 'area':'Sector 10, Bhilai, Chhattisgarh', 'location':(21.179836, 81.327990)},
                    {'name':'Civic Center Area', 'area':'Sector 5, Bhilai, Chhattisgarh', 'location':(21.181597, 81.338361)},
                    {'name':'Maroda Sector', 'area':'Bhilai, Chhattisgarh', 'location':(21.162621, 81.359463)}
                   ]

plant_locations = [plant['location'] for plant in plantation_sites]

info_box_template = """
<dl>
<dd> <b>{name} </b></dd>
<dd> {area} </dd>
<dd> <button onclick="myFun"> Plant Here </button>
<script>

    
</dd>

</dl>
"""

plant_info = [info_box_template.format(**plant) for plant in plantation_sites]
marker_layer = gmaps.marker_layer(plant_locations, info_box_content=plant_info)
city = (21.1938, 81.3509)
fig = gmaps.figure(center=city, zoom_level=12)
fig.add_layer(marker_layer)
fig