import sqlite3
import pandas as pd

def make_db(df):
    conn = sqlite3.connect('./kartrider.db')
    df.to_sql('match_data', conn)

if __name__ == '__main__':
    df = pd.read_csv('./main_df_fin.csv')
    make_db(df)