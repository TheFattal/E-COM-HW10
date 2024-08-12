countries = [
    {'name': 'Israel', 'population': 9.3, 'birth': 1948},
    {'name': 'United States', 'population': 331.9, 'birth': 1776},
    {'name': 'Japan', 'population': 125.8, 'birth': 660},
    {'name': 'Australia', 'population': 25.7, 'birth': 1901},
    {'name': 'Canada', 'population': 38.0, 'birth': 1867}
]

large_population_countries = list(filter(lambda country: country['population'] > 30, countries))
print(large_population_countries)

post_1800_countries = list(filter(lambda country: country['birth'] > 1800, countries))
print(post_1800_countries)

country_names = list(map(lambda country: country['name'], countries))
print(country_names)

country_birth_years = list(map(lambda country: country['birth'], countries))
print(country_birth_years)

sorted_by_birth = sorted(countries, key=lambda country: country['birth'])
print(sorted_by_birth)

sorted_by_population = sorted(countries, key=lambda country: country['population'])
print(sorted_by_population)
