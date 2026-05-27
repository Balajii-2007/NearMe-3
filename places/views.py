from django.shortcuts import render


# Data for 5 locations around a house in Mysore
PLACES = {
    'mysore-palace': {
        'name': 'Mysore Palace',
        'slug': 'mysore-palace',
        'category': 'Heritage',
        'distance': '1.2 km',
        'description': (
            'Mysore Palace, also known as Amba Vilas Palace, is one of the most magnificent royal palaces '
            'in India and the most visited monument in the country after the Taj Mahal. Located approximately '
            '1.2 kilometres from our house, this grand palace was built in the Indo-Saracenic style and '
            'completed in 1912 under the reign of Krishnaraja Wadiyar IV. The palace was designed by the '
            'British architect Henry Irwin and blends Hindu, Muslim, Rajput, and Gothic architectural styles '
            'beautifully. The interiors are breathtakingly ornate with stained glass ceilings, carved wooden '
            'doors, mosaic floors, and a magnificent Durbar Hall. On Sundays and public holidays the entire '
            'palace is illuminated with nearly 100,000 light bulbs, creating an awe-inspiring spectacle. '
            'During the Dasara festival in October, the palace hosts grand processions and cultural events '
            'drawing millions of tourists from across the world every year.'
        ),
        'icon': '🏰',
        'color': '#d4a017',
    },
    'chamundi-hills': {
        'name': 'Chamundi Hills',
        'slug': 'chamundi-hills',
        'category': 'Religious',
        'distance': '3.0 km',
        'description': (
            'Chamundi Hills is the most sacred and iconic natural landmark of Mysore, rising about 1,065 metres '
            'above sea level and located approximately 3.0 kilometres from our house. Atop this hill stands '
            'the revered Chamundeshwari Temple, dedicated to Goddess Chamundeshwari, the presiding deity of '
            'the Mysore royal family and the city itself. The temple is a magnificent example of Dravidian '
            'architecture with a towering 40-metre gopuram. A popular route to the top involves climbing '
            '1,000 steps, and along the way visitors pass a massive monolithic statue of Nandi the bull, '
            'carved out of a single rock in 1659 CE. The view of the entire Mysore city from the hilltop '
            'is absolutely stunning, especially at sunrise and sunset. The hills are surrounded by dense '
            'forest and are home to diverse flora and wildlife. Visiting Chamundi Hills is considered an '
            'essential spiritual and scenic experience for every resident of Mysore.'
        ),
        'icon': '⛰️',
        'color': '#c0392b',
    },
    'devaraja-market': {
        'name': 'Devaraja Market',
        'slug': 'devaraja-market',
        'category': 'Shopping',
        'distance': '0.8 km',
        'description': (
            'Devaraja Market is the oldest and most vibrant traditional market in Mysore, located just '
            '0.8 kilometres from our house. This bustling market was established during the reign of '
            'Tipu Sultan and has been serving the people of Mysore for over two centuries. The market '
            'is an explosion of colours, aromas, and sounds. It is particularly famous for its flower '
            'stalls overflowing with jasmine, marigold, and rose garlands used for temple offerings and '
            'daily puja. You can also find a wide variety of fresh fruits, vegetables, spices, incense '
            'sticks, traditional Mysore silk sarees, sandalwood products, and the world-famous Mysore pak '
            'sweet here. The market is spread across several lanes and is always busy from early morning '
            'to late evening. It is a wonderful place to soak in the authentic culture and everyday life '
            'of Mysore. The architecture of the market building itself, with its old-style pillars and '
            'arches, adds a historic charm to the shopping experience.'
        ),
        'icon': '🌼',
        'color': '#e67e22',
    },
    'ksrtc-hospital': {
        'name': 'JSS Hospital',
        'slug': 'ksrtc-hospital',
        'category': 'Healthcare',
        'distance': '1.0 km',
        'description': (
            'JSS Hospital is one of the most reputed and well-equipped private hospitals in Mysore, '
            'situated approximately 1.0 kilometre from our house. It is part of the JSS Academy of '
            'Higher Education and Research, a premier deemed university. The hospital is a multi-speciality '
            'tertiary care centre with over 1,000 beds and state-of-the-art medical infrastructure. '
            'It offers comprehensive healthcare services across all major specialities including cardiology, '
            'neurology, oncology, orthopaedics, nephrology, gastroenterology, and organ transplantation. '
            'The hospital is also a major teaching hospital attached to JSS Medical College and trains '
            'hundreds of medical students and residents every year. The emergency and trauma care unit '
            'operates round the clock. The hospital is well known for its compassionate staff, modern '
            'diagnostic facilities, and quality patient care. It serves patients not just from Mysore '
            'but from the entire region of southern Karnataka and neighbouring states as well.'
        ),
        'icon': '🏥',
        'color': '#1abc9c',
    },
    'brindavan-gardens': {
        'name': 'Brindavan Gardens',
        'slug': 'brindavan-gardens',
        'category': 'Recreation',
        'distance': '2.0 km',
        'description': (
            'Brindavan Gardens is one of the most famous and beautifully maintained garden complexes '
            'in all of India, located about 2.0 kilometres from our house near the Krishnaraja Sagar '
            'Dam on the Kaveri River. These stunning terraced gardens were developed in 1932 and spread '
            'across nearly 60 acres of lush greenery. The gardens are laid out in a formal Mughal style '
            'with symmetrical pathways, fountains, flower beds, and well-trimmed hedges. The centrepiece '
            'is the spectacular musical fountain show held every evening where jets of water dance in '
            'perfect synchronisation to classical Carnatic music and Bollywood songs, all illuminated '
            'by colourful lights. Thousands of visitors flock here every weekend and holiday. The backdrop '
            'of the massive Krishnaraja Sagar reservoir makes the setting even more picturesque. The gardens '
            'are surrounded by a wide variety of trees, flowering plants, and even aquatic gardens. '
            'A visit to Brindavan Gardens at dusk is a truly magical and unforgettable experience.'
        ),
        'icon': '🌿',
        'color': '#27ae60',
    },
}


def home(request):
    """Main page with Google Maps imagemap."""
    places_list = list(PLACES.values())
    # Public image of Mysore (falls back to local static file if you prefer)
    mysore_image_url = 'https://upload.wikimedia.org/wikipedia/commons/6/66/Mysore_Palace.jpg'
    return render(request, 'places/home.html', {
        'places': places_list,
        'mysore_image_url': mysore_image_url,
    })


def place_detail(request, slug):
    """Detail page for each location."""
    place = PLACES.get(slug)
    if not place:
        from django.http import Http404
        raise Http404("Place not found")
    return render(request, 'places/place_detail.html', {'place': place})
