import pandas as pd
import sqlite3

con = sqlite3.connect("be.sqlite")
df = pd.read_sql_query("SELECT latitude, longitude FROM wifi_zone WHERE (latitude BETWEEN 50.000000 AND 51.000000) AND (longitude BETWEEN 4.00000 AND 5.000000)", con)


with open('wifi_data.txt', 'w') as f:
    for ind in df.index:
        f.write(str(df['latitude'][ind]) + " " + str(df['longitude'][ind]))
        f.write('\n')


#for label, content in df.items():
    #print(f'label: {label}')
#    print()

#with open('data.txt', 'w') as f:
#    for row in df.:
#        x = x_center + (random() - 0.5)/10
#        y = y_center + (random() - 0.5)/10
#        f.write(str(x) + " " + str(y))
#        f.write('\n')
