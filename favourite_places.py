favourite_places = {                                                          #bandarban, cox's bazar, ratargul
    'samiul': {
        'favourite_place': 'ratargul',
        'favourite_number': '4',
    },
    'antora': {
        'favourite_place': "bandarban",
        'favourite_number': '3',
    },
    'mithila': {
        'favourite_place': "cox's_bazar",
        'favourite_number': '4',
    },
}
for each_person, person_info in favourite_places.items():                  #this for loop is for the main dictionary where each person is the key and person_info holds the value
    print("\n"+each_person.title()+"'s favourite place and number is: ")   #here we are printing the keys of the main dictionary
    for info in person_info.values():                                      #when you are using nest of dictionary in dictionary always remember that the keyword values gonna use in the inside loop as it is gonna use for iterate among values
        print("\t\t\t\t\t\t\t\t\t\t"+info.title()+".")                     #in this inside loop we need only values then used values not items
