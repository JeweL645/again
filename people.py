person1 = {
    'name': 'faria',
    'age': '25',
    'hobby': 'dancing',
    'profession': 'teacher',
}
person2 = {
    'name': 'nadia',
    'age': '24',
    'hobby': 'singing',
    'profession': 'singer',
}
person3 = {
    'name': 'elias',
    'age': '25',
    'hobby': 'drawing',
    'profession': 'programmer',
}
peoples = [person1,person2,person3]

for people in peoples:
    print("Name: "+people['name'].title())
    print("Age: "+people['age'])
    print("Hobby: "+people['hobby'].title())
    print("Profession "+people['profession'].title())
    print()