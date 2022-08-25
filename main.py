import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")

movie_list = [movie.getText() for movie in movie_titles][::-1]
print(movie_list)

with open("movies.txt", 'w') as file:
    for i in range(len(movie_list)):
        file.write(f"{movie_list[i]}\n")