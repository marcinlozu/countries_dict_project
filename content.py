#functions:
#print every city in countries
def every_city(countries):
	for country, city in countries.items():
		for city2 in countries[country]:
			print(city2)
#
def countries_to_visit(countries, my_countries, emi_countries):
	countries_to_visit = []
	for country in countries:
		if (country not in my_countries) and (country not in emi_countries):
			countries_to_visit.append(country)
	return countries_to_visit
#
def cities_to_visit(countries, my_countries, emi_countries):
	cities = {}
	for country, city in countries.items():
		if (country not in my_countries.keys()) and (country not in emi_countries.keys()):
			cities[country] = city
		elif (country in my_countries.keys()) and (country not in emi_countries.keys()):
			for value in countries[country]:
				if value not in my_countries[country]:
					if country not in cities:
						cities[country] = [value]
					else:
						#cities[country] = [cities[country], value]
						cities[country].append(value)
		elif (country not in my_countries.keys()) and (country in emi_countries.keys()):
			for value in countries[country]:
				if value not in emi_countries[country]:
					if country not in cities:
						cities[country] = [value]
					else:
						#cities[country] = [cities[country], value]
						cities[country].append(value)
		else:
			for value in countries[country]:
				if (value not in my_countries[country]) and (value not in emi_countries[country]):
					if country not in cities:
						cities[country] = [value]
					else:
						#cities[country] = [cities[country], value]
						cities[country].append(value)
	return cities
#
def visited_countries(countries, my_countries, emi_countries):
	visited_places = []
	for key in countries:
		if (key in my_countries) and (key in emi_countries):
			visited_places.append(key)
	return visited_places


