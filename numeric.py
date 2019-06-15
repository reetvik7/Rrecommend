import pandas as pd


pd.options.mode.chained_assignment = None

data = pd.read_csv("dataset/refined_dataset.csv")

df = data[["movieId", "popularity", "year", 'runtime', "vote_average", "vote_count"]]
df = df.apply(pd.to_numeric)
df['weighted score']=0.7*df['vote_count']+0.3*df['vote_average']
df= df.sort_values(by=['weighted score'], ascending=[False])


def year(p):
    return df.loc[df['year'] >= p]


def runtime(p):
    return df.loc[df['runtime'] >= p]


if __name__ == "__main__":
  year()
  runtime()