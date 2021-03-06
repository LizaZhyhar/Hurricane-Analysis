# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas',  'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
                   
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# 1
def damages_USD(list_of_damages):
  damages_list = []
  for record in list_of_damages:
    if record == 'Damages not recorded':
      damages_list.append(record)
    elif record[-1] == 'B':
      record = str(float(record[:-1]) * 1000000000)
      damages_list.append(record)
    elif record[-1] == 'M':
      record = str(float(record[:-1]) * 1000000)
      damages_list.append(record)
  return damages_list

updated_damages_list = damages_USD(damages)
print(updated_damages_list)
print('--------------------------------')

# 2 
def dictionary_of_hurricanes(names, months, years, max_sustained_winds, areas_affected, deaths):
  hurricanes = {}
  for hurricane in range(len(names)):
    hurricanes.update({names[hurricane]: {'Name': names[hurricane], 'Month': months[hurricane], 'Year': years[hurricane], 'Max Sustained Wind': max_sustained_winds[hurricane], 'Areas Affected': areas_affected[hurricane], 'Damage': updated_damages_list[hurricane], 'Deaths': deaths[hurricane]}})
  return hurricanes

hurricane_dictionary = dictionary_of_hurricanes(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricane_dictionary)
print('--------------------------------')

# 3
def hurricance_organized_by_year(hurricane_dictionary):
  list_of_years = []
  hurricanes_organized_by_year = {}
  hurricanes_in_year = []
  for key, value in hurricane_dictionary.items():
    if value['Year'] not in list_of_years:
      list_of_years.append(value['Year']) 
  for year in list_of_years:
    for key, value in hurricane_dictionary.items():
      if value['Year'] == year:
        hurricanes_in_year.append({'Name': value['Name'], 'Month': value['Month'], 'Year':value['Year'], 'Max Sustained Wind':value['Max Sustained Wind'], 'Areas Affected':value['Areas Affected'], 'Damage': value['Damage'], 'Deaths':value['Deaths']})
        hurricanes_organized_by_year.update({value["Year"]: hurricanes_in_year})
    hurricanes_in_year = []
  return hurricanes_organized_by_year

hurricance_organized_by_year_result =   hurricance_organized_by_year(hurricane_dictionary)
print(hurricance_organized_by_year_result)
print('--------------------------------')
  
# 4
def area_count(areas_affected):
  new_areas_affected = []
  number_of_hurricanes_in_areas = {}
  for record in areas_affected:
    for area in record:
      new_areas_affected.append(area)
  for area in new_areas_affected:
    count = new_areas_affected.count(area)
    number_of_hurricanes_in_areas.update({area:count})
  return number_of_hurricanes_in_areas

count_hurricane_in_every_area = area_count(areas_affected)
print(count_hurricane_in_every_area)
print('--------------------------------')

# 5 
def the_most_hurricanes_area(number_of_hurricanes_in_areas):
  max_number_of_hurricanes = 1
  for key, value in number_of_hurricanes_in_areas.items():
    if value > max_number_of_hurricanes:
      max_number_of_hurricanes = value
      max_number_of_hurricanes_area = key
  result = ('The most affected by hurricanes area is {}. This area was hit for {} times.'.format(max_number_of_hurricanes_area, max_number_of_hurricanes))
  return result

the_most_hurricanes_area_result = the_most_hurricanes_area(count_hurricane_in_every_area)
print(the_most_hurricanes_area_result)
print('--------------------------------')

# 6
def the_greatest_number_of_deaths(deaths_number):
  max_deaths = max(deaths_number)
  max_deaths_index = deaths_number.index(max_deaths)
  max_deaths_result = '{} is  the hurricane that caused the greatest number of deaths. As a result of the hurricane {} people died'.format(names[max_deaths_index], max_deaths)
  return max_deaths_result

the_greatest_number_of_deaths_result = the_greatest_number_of_deaths(deaths)
print(the_greatest_number_of_deaths_result)
print('--------------------------------')

# 7
def mortality_rating(deaths_number, mortality_scale, hurricane_names, hurricane_dictionary):
  hurricane_mortality_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for hur_mort in range(len(deaths_number)):
    if deaths_number[hur_mort] == mortality_scale[0]:
      hurricane_name = hurricane_names[hur_mort]
      hurricane_mortality_rating[0].append(hurricane_dictionary[hurricane_name])
    elif deaths_number[hur_mort] > mortality_scale[0] and deaths_number[hur_mort] <= mortality_scale[1]:
      hurricane_name = hurricane_names[hur_mort]
      hurricane_mortality_rating[1].append(hurricane_dictionary[hurricane_name])
    elif deaths_number[hur_mort] > mortality_scale[1] and deaths_number[hur_mort] <= mortality_scale[2]:
      hurricane_name = hurricane_names[hur_mort]
      hurricane_mortality_rating[2].append(hurricane_dictionary[hurricane_name])
    elif deaths_number[hur_mort] > mortality_scale[2] and deaths_number[hur_mort] <= mortality_scale[3]:
     hurricane_name = hurricane_names[hur_mort]
     hurricane_mortality_rating[3].append(hurricane_dictionary[hurricane_name])
    elif deaths_number[hur_mort] > mortality_scale[3] and deaths_number[hur_mort] <= mortality_scale[4]:
      hurricane_name = hurricane_names[hur_mort]
      hurricane_mortality_rating[4].append(hurricane_dictionary[hurricane_name])
    elif deaths_number[hur_mort] > mortality_scale[4]:
     hurricane_name = hurricane_names[hur_mort]
     hurricane_mortality_rating[5].append(hurricane_dictionary[hurricane_name])
  return hurricane_mortality_rating

mortality_rating_result = mortality_rating(deaths, mortality_scale, names, hurricane_dictionary)
print(mortality_rating_result)
print('--------------------------------')

# 8
def the_greatest_damage(damages_list):
  max_damage = 0
  for damage in damages_list:
    if damage != 'Damages not recorded' and float(damage) > max_damage:
      max_damage = float(damage)
  max_damage_index = damages_list.index(str(max_damage))
  max_damage_result = names[max_damage_index] + ' is the hurricane that caused the greatest damage. As a result of the hurricane the damage reached ' + str(max_damage) +' dollars.'
  return max_damage_result

the_greatest_damage_result = the_greatest_damage(updated_damages_list)
print(the_greatest_damage_result)
print('--------------------------------')

# 9
def damage_rating(damages, names, damage_scale, hurricane_dictionary):
  hurricane_damage_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for damage in damages:
    if damage != 'Damages not recorded':
      if float(damage) == damage_scale[0]:
        damage_name = names[damages.index(damage)]
        hurricane_damage_rating[0].append(hurricane_dictionary[damage_name])
      elif float(damage) > damage_scale[0] and float(damage) <= damage_scale[1]:
        damage_name = names[damages.index(damage)]
        hurricane_damage_rating[1].append(hurricane_dictionary[damage_name])
      elif float(damage) > damage_scale[1] and float(damage) <= damage_scale[2]:
        damage_name = names[damages.index(damage)]
        hurricane_damage_rating[2].append(hurricane_dictionary[damage_name])
      elif float(damage) > damage_scale[2] and float(damage) <= damage_scale[3]:
        damage_name = names[damages.index(damage)]
        hurricane_damage_rating[3].append(hurricane_dictionary[damage_name])
      elif float(damage) > damage_scale[3] and float(damage) <= damage_scale[4]:
        damage_name = names[damages.index(damage)]
        hurricane_damage_rating[4].append(hurricane_dictionary[damage_name])
      elif float(damage) > damage_scale[4]:
        damage_name = names[damages.index(damage)]
        hurricane_damage_rating[5].append(hurricane_dictionary[damage_name])
  return hurricane_damage_rating

damage_rating_result = damage_rating(updated_damages_list, names, damage_scale, hurricane_dictionary)
print(damage_rating_result)
