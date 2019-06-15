import re
import pandas as pd



#df = pd.read_csv('year.csv')
#dff=df[df.year > 2002]
#dff.to_csv("final.csv")

pd.options.mode.chained_assignment = None


r_cols = ['user_id', 'movie_id', 'rating']
rating = pd.read_csv('dataset/ratings.csv', names=r_cols)

df= pd.read_csv('dataset/final.csv')
df_title = df[["movie_id","title"]]
df_title.set_index('movie_id', inplace = True)

ratings = pd.merge(df_title,rating,on="movie_id")
df_p = ratings.pivot_table(index=['user_id'], columns=['movie_id'], values='rating').reset_index(drop=True)
df_p.fillna(0, inplace=True)



def recommend(movie_title,n):
    print("For movie ({})".format(movie_title))
    print("- Top movies recommended are ")
    i = int(df_title.index[df_title['title'] == movie_title][0])
    target = df_p[i]
    similar_to_target = df_p.corrwith(target)
    corr_target = pd.DataFrame(similar_to_target, columns = ['Similarity'])
    corr_target.dropna(inplace = True)
    corr_target = corr_target.sort_values('Similarity', ascending = False)
    corr_target.index = corr_target.index.map(int)
    corr_target = corr_target.join(df_title)[['Similarity', 'title']]
    return corr_target[1:n+1].to_string(index=False)

'''inp=str(input("enter movie"))
inp=inp.lower()
inp=inp.replace(" ","")
movie= df_title[df_title['check'].str.contains(inp)]
x=movie.values
movie_title = x[0][0]
n=int(input("how many??"))
x = recommend(movie_title,n)
print(x)
'''
