import content

#countries to visit
countries = {'France': ['Paris', 'Dieppe', 'Toulouse', 'Marsilie'], 'Greece': ['Athens', 'Crete', 'Thessaloniki'], 'Germany': ['Bayreuth', 'Nurnberg', 'Berlin'], 'USA': ['Chicago', 'NY', 'LA'], 'Spain': ['Madryt', 'Sevilla', 'Toledo'], 'Portugal': ['Porto', 'Lisboa', 'Faro'], 'India': ['Mumbai', 'New Delphi'] }
#countries that I have visited
my_countries = {'France': ['Paris', 'Dieppe', 'Toulouse'],'Greece': ['Athens', 'Crete', 'Thessaloniki'], 'Portugal': ['Porto', 'Lisboa'], 'Germany': ['Bayreuth']}
#countries Emi has visited
emi_countries = {'France': ['Dieppe', 'Toulouse'],'Greece': ['Athens', 'Crete', 'Thessaloniki'], 'Portugal': ['Porto', 'Lisboa'], 'India': ['Mumbai'] }

#countries that we have never been to (together)
print('Countries that we have never been to:')
print(content.countries_to_visit(countries, my_countries, emi_countries))
#cities that we have never been to (together)
print('Cities that we have never been to:')
print(content.cities_to_visit(countries, my_countries, emi_countries))
#countries that we have been together
print('Countries that we have been to:')
print(content.visited_countries(countries, my_countries, emi_countries))
#cities that we have been together
print('Cities that we have been to:')

