import pandas as pd

data = pd.read_csv("dataset/refined_dataset.csv")

df = data[["movieId", "genres", "cast", 'keywords', "director", "vote_average", "vote_count"]]
df['weighted score'] = 0.7 * df['vote_count'] + 0.3 * df['vote_average']
df = df.sort_values(by=['weighted score'], ascending=[False])
df = df.dropna()



def genres(p):
    return df[df['genres'].str.contains(p)]


def director(p):
    return df[df['director'].str.contains(p)]



def cast(p):
    return df[df['cast'].str.contains(p)]

if __name__ == "__main__":
  genres()
  director()
  cast()