import pandas as pd
games = pd.read_csv('games.csv')
print(games.head())
print(games.info())
print(games['playingtime'].mean())
print(games['total_comments'].max())
print(games[games['id']==1500]['name'])
print(games[games['id']==1500]['yearpublished'])
print(games[games['total_comments']==games['total_comments'].max()])
print(games[games['total_comments']==games['total_comments'].min()])
print(games.groupby('type')['minage'].mean())
print(games['id'].nunique())
print(games['type'].value_counts())
print(games[['playingtime','total_comments']].corr())

# seaborn usage

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_color_codes('deep')
games = pd.read_csv('games.csv')
print(games.info())
games.dropna(inplace=True)

sns.distplot(games['average_rating'])
plt.show()

sns.jointplot(x='minage', y='average_rating',data=games)
plt.show()

sns.pairplot(games[['playingtime', 'minage', 'average_rating']])
plt.show()

sns.stripplot(x='type', y='playingtime', jitter=True, data= games)
plt.show()

sns.regplot(x='playingtime', y='average_rating', data=games[games['playingtime']<500])
plt.show()
