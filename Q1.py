israel_dict: dict = {
    "name": "israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": {"Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"},
    "currency": "ILS",
    "area_Kilometer": 22145,
    "gdp_billion": 450

}

# a:
print(f"The capital is: {israel_dict.get('capital')}")

# b:
print("\nAll the keys are:")
for key in israel_dict.keys():
    print(key)

# c:
uppercase_keys = [key.upper() for key in israel_dict]
print("\nKeys in uppercase are:")
print(uppercase_keys)

# d:
print("\nAll the values are:")
for value in israel_dict.values():
    print(value)

# e:
values_len_list = [len(value) for value in israel_dict]
print(f"\nValues len list is:\n{values_len_list}")

# f:
print("\nAll the items are:")
for item in israel_dict.items():
    print(item)

# g:
dict_copy = israel_dict.copy()

# h:
israel_dict.clear()

# i:
new_dict = dict.fromkeys(israel_dict.keys(), None)
print(new_dict)

# j:
del israel_dict['currency']

# k:
area_km_pop = israel_dict.pop('area_Kilometer')

# l:
israel_dict.update({'Soccer ': 'sport_national'})
israel_dict.update({'population_millions': 9.4})
