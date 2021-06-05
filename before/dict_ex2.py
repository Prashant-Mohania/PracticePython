# first method


user = {}
Name, Age, fav_movies, fav_songs = input(
    "enter your Name, Age , fav_movies , fav_songs:- ").split(",")
user['Name'] = Name
user['Age'] = Age
user['Fav_Movies'] = fav_movies
user['Fav_Songs'] = fav_songs
for i in user:
    print(f"{i} :- {user[i]}")

# second method


user = {}
Name, Age, fav_movies, fav_songs = input(
    "enter your Name, Age , fav_movies , fav_songs:- ").split(",")
user['Name'] = Name
user['Age'] = Age
user['Fav_Movies'] = fav_movies
user['Fav_Songs'] = fav_songs
for key, value in user.items():
    print(f"{key} :- {value}")


# third method

# Prashant,18,coco and avengers,yaari and khaab
user = {}
Name = input("enter your name:- ")
Age = input("enter your age:- ")
fav_movies = input("enter your fav movies:- ").split(",")
fav_songs = input("enter your fav songs:- ").split(",")
user['Name'] = Name
user['Age'] = Age
user['Fav_Movies'] = fav_movies
user['Fav_Songs'] = fav_songs
for key, value in user.items():
    print(f"{key} :- {value}")
