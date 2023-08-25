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
df_anime_filtrado = df_anime_filtrado.dropna(subset=['rating'])
# %%
df_user_rating_anime = pd.merge(left=df_rating, right=df_anime_filtrado, on='anime_id',how='left')
columns=['user_id','anime_id','rating_x','name']
df_user_rating_anime = df_user_rating_anime[columns]
#%%
df_user_rating_anime.rename(columns={"rating_x": "user_rating"},inplace=True)
# %%
df_user_rating_anime = df_user_rating_anime.dropna(subset=['name'])
#%%
df_anime_filtrado.to_csv("./data/general_rating.csv")
df_user_rating_anime.to_csv("./data/user_rating.csv")
# %%
df_anime_filtrado
#%%
df_user_rating_anime