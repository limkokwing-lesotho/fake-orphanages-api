import datetime


def increment():
    return datetime.date.today().day + datetime.datetime.now().hour


all_houses = [
    {
        'id': '01',
        'name': "Lehakoe",
        'location': "Maseru Central",
        'image': "https://www.habitatforhumanity.org.uk/wp-content/uploads/2017/10/housing-poverty-lesotho-africa.jpg",
    },
    {
        'id': '02',
        'name': "House of Hope",
        'location': "Hills View",
        'image': "https://riseint.org/wp-content/uploads/2017/05/Lesotho-1-1.jpg",
    },
    {
        'id': '03',
        'name': "Liphakoe",
        'location': "Maseru Central",
        'image': "https://live.staticflickr.com/5020/5484238615_45d912a83b_b.jpg",
    },
    {
        'id': '04',
        'name': "'Ma Bana",
        'location': "Leribe",
        'image': "https://www.habitat.org/sites/default/files/2016-12/lesotho-orphans_0.jpg",
    },
    {
        'id': '05',
        'name': "Selikoe",
        'location': "Mohale's Hoek",
        'image': "https://www.humanium.org/en/wp-content/uploads/2020/08/shutterstock_1118238941-1-1024x683.jpg",
    },
    {
        'id': '06',
        'name': "Lejoe Letlama",
        'location': "Ha Mabote",
        'image': "https://everyoneschild.net/wp-content/uploads/2020/06/XrpIbQafQ0CXtTQJPO5QBQ_thumb_c53e.jpg",
    },
]

house1 = {
    'id': "01",
    'name': "Lehakoe",
    'location': "Maseru Central",
    'image': "https://www.habitatforhumanity.org.uk/wp-content/uploads/2017/10/housing-poverty-lesotho-africa.jpg",
    'donated': 1920 + increment() * 2,
    'target': 12000
}

house2 = {
    'id': "02",
    'name': "House of Hope",
    'location': "Hills View",
    'image': "https://riseint.org/wp-content/uploads/2017/05/Lesotho-1-1.jpg",
    'donated': 1000 + increment() * 32,
    'target': 13000
}

house3 = {
    'id': "03",
    'name': "Liphakoe",
    'location': "Maseru Central",
    'image': "https://live.staticflickr.com/5020/5484238615_45d912a83b_b.jpg",
    'donated': 920 + increment() * 2,
    'target': 1500
}

house4 = {
    'id': "04",
    'name': "'Ma Bana",
    'location': "Leribe",
    'image': "https://www.habitat.org/sites/default/files/2016-12/lesotho-orphans_0.jpg",
    'donated': 800 + increment() * 3,
    'target': 950
}

house5 = {
    'id': "05",
    'name': "Selikoe",
    'location': "Mohale's Hoek",
    'image': "https://www.humanium.org/en/wp-content/uploads/2020/08/shutterstock_1118238941-1-1024x683.jpg",
    'donated': increment() * 5,
    'target': 5000
}

house6 = {
    'id': "06",
    'name': "Lejoe Letlama",
    'location': "Ha Mabote",
    'image': "https://everyoneschild.net/wp-content/uploads/2020/06/XrpIbQafQ0CXtTQJPO5QBQ_thumb_c53e.jpg",
    'donated': 920 + increment() * 5,
    'target': 1200
}
