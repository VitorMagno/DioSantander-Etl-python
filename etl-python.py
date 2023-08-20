#%%
import pandas as pd
import numpy as np
# %%
df_animes = pd.read_csv("./data/anime.csv")
df_rating = pd.read_csv("./data/rating.csv")
# %%
columns=['anime_id','name','rating', 'members']
filtro_filme = df_animes['episodes']!='1'
df_anime_filtrado = df_animes[filtro_filme]
df_anime_filtrado = df_anime_filtrado[columns]
# %%
df_rating
# %%
df_anime_filtrado.sort_values(by='members', ascending=False).head(10)
# %%
df_anime_filtrado.sort_values(by='rating', ascending=False).head(10)
# %%
df_rating_anime = pd.merge(left=df_rating, right=df_anime_filtrado, on='anime_id',how='left')
columns=['user_id','anime_id','rating_x','name']
df_rating_anime = df_rating_anime[columns]
# %%
df_rating_anime