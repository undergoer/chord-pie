from pycirclize import Circos
import numpy as np

import pandas as pd

file = 'Inventory Data Export 11 July 2025.xlsx'
sheet = "Bilateral MRAs"

df = pd.read_excel(file, sheet_name=sheet)
print(len(df))

# Initialize Circos sections
sectors = {'Australia': 69, 'Brunei Darussalam': 1, 'Canada': 40, 'Papua New Guinea': 1, 'Hong Kong, China': 56,
           'Russia': 5, 'Singapore': 8, 'Japan': 6,
           'China': 14, 'Malaysia': 3, 'New Zealand': 15, 'Korea': 3, 'Indonesia': 3}

external = {'Australia': 38, 'Brunei Darussalam': 0, 'Canada': 26, 'China': 0, 'Hong Kong, China': 27, 'Indonesia': 1,
            'Japan': 0, 'Korea': 1, 'Malaysia': 0, 'New Zealand': 3, 'Papua New Guinea': 0, 'Russia': 5, 'Singapore': 3}


# trade_colors
tc = {
    'Accountants': '#ccebc5',
    'Architects': '#decbe4',
    'Actuaries': '#dbe297',
    # 'Dental Practitioners': '#d9dddc',
    'Surveyors': '#d9dddc',
    'Engineers': '#fbb4ae',
    #    'Nurses and Midwives': '#90a0a5',
    #    'Veterinarians': '#bebdb8',
    'Other': '#fffacd'
    # 'Veterinarians': '#ffffcc'
}

tc0 = {
    'Accountants': 'green',
    'Architects': 'red',
    'Actuaries': 'purple',
    # 'Dental Practitionerss': '#d9dddc',
    'Surveyors': 'orange', # '#d9dddc',  # (.8, .9216, .7725)
    'Engineers': 'pink',
    #    'Nurses and Midwives': '#90a0a5',
    #    'Veterinarians': '#bebdb8',
    # 'Other': 'purple'
    # 'Veterinarians': '#ffffcc'
}

# darker pastels
tc1 = {'Engineers': (0.9850980392156864, 0.44117647058823545, 0.39647058823529424),
       'Accountants': (0.6200000000000003, 0.8509803921568627, 0.5678431372549021),
       'Architects': (0.38156862745098064, 0.560392156862745, 0.8062745098039217),
       'Surveyors': (1.0, 0.7243137254901959, 0.344313725490196),
       'Actuaries': (0.7466666666666666, 0.7988235294117647, 0.22509803921568627),
       # 'All regulated professions': (0.9180392156862746, 0.6050980392156863, 0.7988235294117647),
       # 'Dental Practitioners': (0.724313725490196, 0.724313725490196, 0.724313725490196),
       'Other professions': (1.0, 0.9627450980392156, 0.6125490196078429)}

# country colours
cl = {'Australia': 'green', 'Brunei Darussalam': 'pink', 'Canada': 'blue', 'Papua New Guinea': 'brown',
      'Hong Kong, China': 'orange', 'Russia': 'purple', 'Singapore': 'yellow', 'Japan': 'gray',
      'China': 'red', 'Malaysia': 'tomato', 'New Zealand': 'plum', 'Korea': 'olive', 'Indonesia': 'crimson'}


circos = Circos(sectors, space=3)


# get colours for professions
def my_colour(cc):
    if cc in tc1:
        return tc1[cc]
    else:
        # return "gray"
        return 1.0, 0.9627450980392156, 0.6125490196078429  # "#fffacd"


# respace these labels
cc = ["Singapore", "New Zealand", "Indonesia"]

for sector in circos.sectors:
    # Plot country name
    if sector.name in cc:
        sector.text(f"{sector.name}", r=80.5, size=11)
    else:
        sector.text(f"{sector.name}", r=77.5, size=11)
    # Create x positions and outer pie
    x = np.arange(sector.start, sector.end) + 0.5
    i = 0
    if sector.name in external:
        i = external[sector.name]
    y = [1 if k < i else 0 for k in range(len(x))]
    # Plot bars
    track2 = sector.add_track((67.5, 72.5), r_pad_ratio=0.1)
    track2.axis()
    track2.bar(x, y, color=cl[sector.name])
    y = [1] * len(x)
    track3 = sector.add_track((72.5, 75), r_pad_ratio=0.1)
    track3.axis()
    track3.bar(x, y, color=cl[sector.name])

# Plot links
circos.link(('Australia', 38, 39), ('Indonesia', 1, 2), color=my_colour('Accountants'))
circos.link(('Canada', 26, 27), ('Hong Kong, China', 27, 28), color=my_colour('Accountants'))
circos.link(('Australia', 39, 40), ('Hong Kong, China', 28, 29), color=my_colour('Accountants'))
circos.link(('Australia', 40, 41), ('Singapore', 3, 4), color=my_colour('Accountants'))
circos.link(('Australia', 41, 42), ('Canada', 27, 28), color=my_colour('Accountants'))
circos.link(('Australia', 42, 43), ('Papua New Guinea', 0, 1), color=my_colour('Accountants'))
circos.link(('Australia', 43, 44), ('New Zealand', 3, 4), color=my_colour('Actuaries'))
circos.link(('Australia', 44, 45), ('Canada', 28, 29), color=my_colour('Actuaries'))
circos.link(('Australia', 45, 46), ('Japan', 0, 1), color=my_colour('Actuaries'))
circos.link(('Japan', 1, 2), ('New Zealand', 4, 5), color=my_colour('Architects'))
circos.link(('Hong Kong, China', 29, 30), ('New Zealand', 5, 6), color=my_colour('Architects'))
circos.link(('Australia', 46, 47), ('Hong Kong, China', 30, 31), color=my_colour('Architects'))
circos.link(('Australia', 47, 48), ('Japan', 2, 3), color=my_colour('Architects'))
circos.link(('Australia', 48, 49), ('Hong Kong, China', 31, 32), color=my_colour('Builders and Construction Managers'))
circos.link(('Australia', 49, 50), ('New Zealand', 6, 7), color=my_colour('Builders and Construction Managers'))
circos.link(('Australia', 50, 51), ('Canada', 29, 30), color=my_colour('Dental Practitioners'))
circos.link(('Canada', 30, 31), ('New Zealand', 7, 8), color=my_colour('Dental Practitioners'))
circos.link(('Australia', 51, 52), ('New Zealand', 8, 9), color=my_colour('Dietitians'))
circos.link(('Australia', 52, 53), ('Canada', 31, 32), color=my_colour('Dietitians'))
circos.link(('Australia', 53, 54), ('Indonesia', 2, 3), color=my_colour('Engineers'))
circos.link(('Canada', 32, 33), ('Hong Kong, China', 32, 33), color=my_colour('Engineers'))
circos.link(('Australia', 54, 55), ('Hong Kong, China',33, 34), color=my_colour('Engineers'))
circos.link(('Australia', 55, 56), ('Singapore', 4, 5), color=my_colour('Engineers'))
circos.link(('China', 0, 10), ('Hong Kong, China', 34, 44), color=my_colour('Engineers'))
circos.link(('Australia', 56, 57), ('Canada', 33, 34), color=my_colour('Engineers'))
circos.link(('Australia', 57, 58), ('Japan', 3, 4), color=my_colour('Engineers'))
circos.link(('Hong Kong, China', 44, 45), ('New Zealand', 9, 10), color=my_colour('Engineers'))
circos.link(('Australia', 58, 60), ('Korea', 1, 3), color=my_colour('Engineers'))
circos.link(('Australia', 60, 61), ('Malaysia', 0, 1), color=my_colour('Engineers'))
circos.link(('Australia', 61, 62), ('New Zealand', 10, 11), color=my_colour('Medical Practitioners'))
circos.link(('China', 10, 11), ('Hong Kong, China', 45, 46), color=my_colour('Real Estate Agents'))
circos.link(('Australia', 62, 63), ('New Zealand', 11, 12), color=my_colour('Social Workers'))
circos.link(('Canada', 34, 35), ('Singapore', 5, 6), color=my_colour('Surveyors'))
circos.link(('Canada',35, 36), ('Japan', 4, 5), color=my_colour('Surveyors'))
circos.link(('Canada', 36, 37), ('Hong Kong, China', 46, 47), color=my_colour('Surveyors'))
circos.link(('Australia', 63, 65), ('Hong Kong, China', 47, 49), color=my_colour('Surveyors'))
circos.link(('Australia', 65, 66), ('Singapore', 6, 7), color=my_colour('Surveyors'))
circos.link(('Canada', 37, 38), ('New Zealand', 12, 13), color=my_colour('Surveyors'))
circos.link(('Australia', 66, 67), ('Canada', 38, 39), color=my_colour('Surveyors'))
circos.link(('Hong Kong, China', 49, 51), ('New Zealand', 13, 15), color=my_colour('Surveyors'))
circos.link(('Hong Kong, China', 51, 52), ('Singapore', 7, 8), color=my_colour('Surveyors'))
circos.link(('Canada', 39, 40), ('Malaysia', 1, 2), color=my_colour('Surveyors'))
circos.link(('Australia', 67, 68), ('Malaysia', 2, 3), color=my_colour('Surveyors'))
circos.link(('Hong Kong, China', 52, 53), ('Japan', 5, 6), color=my_colour('Surveyors'))
circos.link(('Australia', 68, 69), ('Brunei Darussalam', 0, 1), color=my_colour('Surveyors'))
circos.link(('China', 11, 14), ('Hong Kong, China', 53, 56), color=my_colour('Surveyors'))

circos.savefig("example01.png")
