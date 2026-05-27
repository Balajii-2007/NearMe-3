# Ex04 Places Around Me
# Date:08-10-2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using `<map>` tag name the map.

## STEP 4
Create clickable regions in the image using `<area>` tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```html
home.html

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Places Around My House - Mysore</title>
</head>
<body>
    <h1 align="center">Mysore</h1>
    <h3 align="center">Places Around My House</h3>
    <img src="{% static 'places/images/neighbourhood_map.png' %}" usemap="#mysoreMap" alt="Mysore map">

    <map name="mysoreMap">
        <area target="" alt="Mysore Palace" title="Mysore Palace" href="/place/mysore-palace/" coords="210,180,35" shape="circle">
        <area target="" alt="Chamundi Hills" title="Chamundi Hills" href="/place/chamundi-hills/" coords="610,130,35" shape="circle">
        <area target="" alt="Devaraja Market" title="Devaraja Market" href="/place/devaraja-market/" coords="400,255,38" shape="circle">
        <area target="" alt="JSS Hospital" title="JSS Hospital" href="/place/ksrtc-hospital/" coords="185,390,35" shape="circle">
        <area target="" alt="Brindavan Gardens" title="Brindavan Gardens" href="/place/brindavan-gardens/" coords="625,390,35" shape="circle">
    </map>
</body>
</html>

place_detail.html

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ place.name }}</title>
</head>
<body>
    <h2 align="center">{{ place.city }}</h2>
    <h3 align="center">{{ place.name }}</h3>
    <hr>
    <h4>{{ place.description }}</h4>
</body>
</html>
```

# OUTPUT
The home page displays a Google Maps-based imagemap with clickable regions for the listed places.

# RESULT
The program for implementing image maps using HTML is executed successfully.
