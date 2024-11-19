planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 149.597870, 'Mars': 227.94}

# string.format() example
for index, planet_name in enumerate(planets.keys(), start=1):
    # print(index, planet_name, planets[planet_name])
    print("{:2d} {:<10s} {:06.2f} Gm".format(index, planet_name, planets[planet_name]))

# literal string interpolation
# 'f' string

for index, planet_name in enumerate(planets.keys(), start=1):
    # print(index, planet_name, planets[planet_name])
    print(f"{index:2d} { planet_name:<10s} {planets[planet_name]:06.2f} Gm")
