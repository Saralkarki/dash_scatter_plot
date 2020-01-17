import pandas as pd
df = pd.read_csv('data/earthquake.csv')
df['text'] = df['Epicenter'] + ',' + df['Magnitude'].astype(str)+ ' ' + 'Richter'
site_lat = df.Lat
site_lon = df.Long


# separate the categories of earthquake
scale = []
for magnitude in df.Magnitude:
    if magnitude >= 3.0 and magnitude <=3.9:
        scale.append("Limited Damage")
    elif magnitude >=4.0 and magnitude <=4.9:
        scale.append("Minor Damage")
    elif magnitude >=5.0 and magnitude <=5.9:
        scale.append("Slight Damage")
    elif magnitude >=6.0 and magnitude <=6.9:
        scale.append("Severe Damage")
    elif magnitude >=7.0 and magnitude <=7.9:
        scale.append("Serious Damage")
    else:
        scale.append("Great Damage")

df['damage'] = scale

df['text'] = df['Epicenter'] + ',' + df['Magnitude'].astype(str)+ ' ' + 'Richter'

df_1 = df[df['damage'] == 'Slight Damage']
df_2 = df[df['damage'] == 'Minor Damage']
df_3 = df[df['damage'] == 'Limited Damage']
df_4 = df[df['damage'] == 'Severe Damage']
df_5 = df[df['damage'] == 'Serious Damage']
