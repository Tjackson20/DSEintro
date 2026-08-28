import folium
# name: Teliyah Jackson
# fun fact: I have 3 siblings that are still under the age of 10 and my favorite color is purple.
name = "Teliyah Jackson"
print(name)

hometown = "Nashville, TN"
undergrad_major = "Computer Science"
current_program = "Data Science and Engineering"
research_area = "Fusion Energy"
undergrad_school = "Lane College"

lane_latitude = 35.6145
lane_longitude = -88.8140
print("Lane college coordinates:")
lane_coordinates = {
    "latitude": lane_latitude,
    "longitude": lane_longitude
}

nashville_latitude = 36.16607
nashville_longitude = -86.7778

nashville_coordinates = {
    "latitude": nashville_latitude,
    "longitude": nashville_longitude
}

ornl_latitude = 35.9313
ornl_longitude = -84.3104

ornl_coordinates = {
    "latitude": ornl_latitude,
    "longitude": ornl_longitude
}

utk_latitude = 35.95174
utk_longitude = -83.93266
utk_coordinates = {
    "latitude": utk_latitude,
    "longitude": utk_longitude
}
journey_map = folium.Map(location=[35.9, -85.5], zoom_start=7)

folium.Marker(
    location=[nashville_latitude, nashville_longitude],
    popup="Nashville, TN"
).add_to(journey_map)

folium.Marker(
    location=[lane_latitude, lane_longitude],
    popup="Lane College"
).add_to(journey_map)

folium.Marker(
    location=[ornl_latitude, ornl_longitude],
    popup="Oak Ridge National Laboratory"
).add_to(journey_map)

folium.Marker(
    location=[utk_latitude, utk_longitude],
    popup="University of Tennessee"
).add_to(journey_map)

journey_route = {
    "Nashville, TN": nashville_coordinates,
    "Lane College": lane_coordinates,
    "Oak Ridge National Laboratory": ornl_coordinates,
    "University of Tennessee": utk_coordinates
}

route_coordinates = [
    [nashville_latitude, nashville_longitude],
    [lane_latitude, lane_longitude],
    [ornl_latitude, ornl_longitude],
    [utk_latitude, utk_longitude]
]
folium.PolyLine(
    route_coordinates,
    weight=4,
    opacity=0.8
).add_to(journey_map)

graduation_year = 2026
grad_school = "University of Tennessee"

print(f"My name is {name}. I am from {hometown} and I am currently pursuing a degree in {current_program}. My research area so far has been in {research_area}. I completed my undergraduate studies in {undergrad_major} at {undergrad_school} and I graduated in {graduation_year}. Now I am attending {grad_school} for my graduate studies.")
print("Listed below are the places I have been academically:")
academic_journey = ["Lane College", "Oak Ridge National Laboratory", "University of Tennessee"]

for place in academic_journey:
    print(f"- {place}")

journey_map.save("academic_journey_map.html")
journey_map.save("academic_journey_map.html")