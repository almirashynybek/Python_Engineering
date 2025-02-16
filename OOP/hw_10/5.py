# Задание 3: Коллекция фильмов

class MovieCollection:
    def __init__(self):
        self.__movies = []

    def add_movie(self, item):
        self.__movies.append(item)

    def __len__(self):
        print("Количество фильмов: ", end = '')
        return len(self.__movies)
    
    def __getitem__(self, index):
        return self.__movies[index]
    
    def __setitem__(self, index, value):
        self.__movies[index] = value
    
    def __contains__(self, item):
        return item in self.__movies
    
    def __str__(self):
        return (
            f"Коллекция фильмов: "
            f"{', '.join(self.__movies) if self.__movies else 'пуста'}")
    

movies = MovieCollection()
movies.add_movie("Inception")
movies.add_movie("The Matrix")

print(len(movies))
print(movies[0])

movies[1] = "Interstellar"
print("Inception" in movies)
print(movies)

