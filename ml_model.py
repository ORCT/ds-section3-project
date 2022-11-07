import pandas as pd
from sklearn.linear_model import Lasso
import pickle

df = pd.read_csv('./main_df_fin.csv')
df.drop(['Match_Id'], axis=1, inplace=True)

X = df.iloc[:,5:]
y = df['Time']

lasso = Lasso(alpha=0.01)
lasso.fit(X,y)

# X_test = [[500,500,500,500,500]]
# print(lasso.predict(X_test))

with open('model.pkl', 'wb') as pickle_file:
    pickle.dump(lasso, pickle_file)