# Nesting list and dictionaries

"""

{
    Key: Value
    Key: [List]
    Key:[Dict]

    }
"""

# Nesting

capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

travel_log = {
    'France': {'cities_visited':['Paris', 'Lille', 'Dijon'], 'total_visits': 12}, #Nesting a list inside a dictionary which is itself nested in a dictionary  
    'Germany': ['Berlin', 'Hamburg', 'Stuttgard']
}

# Nesting a dictionary in a list
travel_log = [
    {
    'country':'France',
    'cities_visited':['Paris', 'Lille', 'Dijon'], 
    'total_visits': 12
    },  

    {
    'country':'Germany',
    'cities_visited':['Berlin', 'Hamburg', 'Stuttgard'],
    'total_visits': 5
    }

]


