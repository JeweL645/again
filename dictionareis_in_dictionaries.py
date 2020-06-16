engineers = {
    'user1': {
        'first_name': 'elias',
        'last_name': 'islam',
        'username': 'elias_islam',
        'email': 'eliasislam645@gmail.com',
        'fav_language': 'python',
    },
    'user2': {
        'first_name': 'nadia',
        'last_name': 'chowdhury',
        'username': 'n_chowdhury',
        'email': 'chowdhurymam1@hotmail.com',
        'fav_language': 'javascript',
    },
    'user3': {
        'first_name': 'mohiuzzaman',
        'last_name': 'bornav',
        'username': 'm_bornav',
        'email': 'mzbornav@yahoo.com',
        'fav_language': 'c',
    },
}

for username, user_info in engineers.items():  #this for loop is for the main dictionary
    print("\n"+username)                       #this print() statement actually working for to print the key of the first dictionary
    for user, val in user_info.items():        #this for loop is basically to loop over the value dictionary
        print(user.title()+":"+val.title())    #here this print statement is working for concate the key value pair of the value dictionary
