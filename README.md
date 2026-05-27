# Ex 03 – Imagemap Project
**Mysore, Karnataka Neighbourhood Map**

## Project Structure
```
imagemap_project/
├── manage.py
├── requirements.txt
├── README.md
├── imagemap_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── places/
    ├── views.py
    ├── urls.py
    ├── static/places/images/
    │   └── neighbourhood_map.png   ← PUT YOUR MAP SCREENSHOT HERE
    └── templates/places/
        ├── home.html
        └── place_detail.html
```

## Setup & Run

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000

## Adding Your Google Maps Screenshot

1. Open Google Maps → navigate to your house area in Mysore
2. Screenshot the area at **800 × 500 px**
3. Save as `places/static/places/images/neighbourhood_map.png`
4. Go to **http://image-map.net** → upload the image
5. Draw circles over each of the 5 locations
6. Copy the generated `<area>` tags
7. Open `places/templates/places/home.html`
8. Replace the `<area>` tags inside `<map name="mysoreMap">` with your generated ones
9. Also adjust the hotspot overlay `left:` and `top:` percentages to match

## 5 Locations Covered (Mysore)

| # | Place | Category | Distance |
|---|-------|----------|---------|
| 1 | Mysore Palace | Heritage | 1.2 km |
| 2 | Chamundi Hills | Religious | 3.0 km |
| 3 | Devaraja Market | Shopping | 0.8 km |
| 4 | JSS Hospital | Healthcare | 1.0 km |
| 5 | Brindavan Gardens | Recreation | 2.0 km |

## URLs

| URL | Page |
|-----|------|
| `/` | Home page with imagemap |
| `/place/mysore-palace/` | Mysore Palace detail |
| `/place/chamundi-hills/` | Chamundi Hills detail |
| `/place/devaraja-market/` | Devaraja Market detail |
| `/place/ksrtc-hospital/` | JSS Hospital detail |
| `/place/brindavan-gardens/` | Brindavan Gardens detail |
