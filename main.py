import pandas as pd
import re
from numeric import year, runtime
from classification import genres,cast,director
from item import recommend


dat = pd.read_csv("dataset/refined_dataset.csv")
data = pd.DataFrame(dat)

print("Welcome....")
n = int(input(print("Choose the criteria on which you want your recommendations to be:\n1.Year\n2.Runtime\n3.Genre\n4.director\n5.cast\n6.Movie")))

if n == 1:
    p = int(input(print("Enter the years from which you want the movies to be")))
    x=int(input(print("how many recommendations do you want")))
    res = pd.merge(data, year(p), on='movieId')
    res = res.sort_values(by=['weighted score'], ascending=[False])
    print(res[["original_title", "year_x"]].head(x))

if n == 2:
    p = int(input(print("Enter the runtime of your movie in minutes")))
    x = int(input(print("How many recommendations do you want")))
    res = pd.merge(data, runtime(p), on='movieId')
    res = res.sort_values(by=['weighted score'], ascending=[False])

    print(res[["original_title", "runtime_x", "year_x"]].head(x))

if n == 3:
    p = str(input(print("Enter the genre from which you want the movies to be")))
    p=p.replace(" ", "")
    p=p.lower()
    p=p.capitalize()
    x = int(input(print("How many recommendations do you want")))
    gen = pd.DataFrame(genres(p))
    res = pd.merge(data, gen, on='movieId')
    res = res.sort_values(by=['weighted score'], ascending=[False])


    print(res[["original_title","genres_x", "year"]].head(x))

if n == 4:
    p = str(input(print("Enter the director from which you want the movies to be")))
    p = p.replace(" ", "")
    p = p.lower()

    x = int(input(print("How many recommendations do you want")))
    direc = pd.DataFrame(director(p))
    res = pd.merge(data,direc, on='movieId')
    res = res.sort_values(by=['weighted score'], ascending=[False])

    print(res[["original_title","director_x", "year"]].head(x))

if n == 5:
    p = str(input(print("Enter the cast from which you want the movies to be")))
    p=p.replace(" ","")
    p=p.lower()

    x = int(input(print("How many recommendations do you want")))
    cas = pd.DataFrame(cast(p))
    res = pd.merge(data,cas, on='movieId')
    res = res.sort_values(by=['weighted score'], ascending=[False])
    

    print(res[["original_title","cast_x", "year"]].head(x))

if n == 6:
    r_cols = ['user_id', 'movie_id', 'rating']
    rating = pd.read_csv('dataset/ratings.csv', names=r_cols)

    df = pd.read_csv('dataset/final.csv')
    df_title = df[["movie_id", "title"]]
    df_title.set_index('movie_id', inplace=True)

    ratings = pd.merge(df_title, rating, on="movie_id")
    df_p = ratings.pivot_table(index=['user_id'], columns=['movie_id'], values='rating').reset_index(drop=True)
    df_p.fillna(0, inplace=True)

    df_title['check'] = df_title["title"].str.lower().str.replace(" ", "")
    df_title["check"] = df_title['check'].map(lambda x: re.sub(r'\W+', '', x))

    inp = str(input("Enter Movie\n"))
    inp = inp.lower()
    inp = inp.replace(" ", "")
    movie = df_title[df_title['check'].str.contains(inp)]
    x = movie.values
    print("The following movies matched your search")
    print('########################################')
    for i in range(len(x)):
        print(str(i+1)+" "+str(x[i][0]))
    user=int(input("\nPlease select a movie by entering its index number\n"))
    movie_title = x[user-1][0]
    n = int(input("how many recommendations do you want??\n"))
    recommendations = recommend(movie_title, n)
    print(recommendations)
