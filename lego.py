import pandas as pd

lego_sets = pd.read_csv("D:\Projects\Python Files\Lego Dataset Analysis\lego_sets.csv")
theme = pd.read_csv("D:\Projects\Python Files\Lego Dataset Analysis\parent_themes.csv")

theme.rename(columns = {'name':'parent_theme'}, inplace = True) 
merged = pd.merge(lego_sets, theme, on = 'parent_theme')

merged[merged['set_num'].isnull()].shape
licensed = merged[merged['is_licensed']]
licensed = licensed.dropna(subset = ['set_num'])
star_wars = licensed[licensed['parent_theme']=='Star Wars']

the_force = (star_wars.shape[0]/licensed.shape[0])*100
answer = round(the_force, 2)
print(answer)

licensed=licensed.sort_values('year')
licensed['count'] = 1

summed_df = licensed.groupby(['year', 'parent_theme']).sum().reset_index()

min_popularity = summed_df.sort_values('count', ascending=False).drop_duplicates(['year'])

min_popularity.sort_values('year', inplace = True)
min_popularity.head()