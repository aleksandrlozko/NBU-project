import pandas as pd
import re
from way import rcsv2


df = pd.read_csv(rcsv2)

df.drop(df[(df.category == '1') | (df.category == '0')].index, inplace=True)


# i = 0
# for line in df.text:
#     match = re.search('[?]', line)
#     try:
#         match = re.search('[?]', line)
#         if (df.category[i] == 'Positive' or df.category[i] == 'Negative') and match != None :
#             df.drop(df.index[i])
#             print(line)
#     except:
#         None
#
#     i += 1


n = 99

positive = df[(df.category == 'Positive')].sample(frac=1).reset_index(drop=True)[:n]
negative = df[(df.category == 'Negative')].sample(frac=1).reset_index(drop=True)[:n]
hotline = df[(df.category == 'Hotline')].sample(frac=1).reset_index(drop=True)[:n]
hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:n]
offer = df[(df.category == 'Offer')].sample(frac=1).reset_index(drop=True)[:n]

siteandcoins = pd.read_csv('../data/coins.csv')[:n]

DF = pd.concat([positive, negative, hotline, hooligan, offer, siteandcoins])
DF.to_csv('../data/category.csv', index=False)
