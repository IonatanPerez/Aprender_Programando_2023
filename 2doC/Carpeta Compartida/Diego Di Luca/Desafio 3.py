#%%
import pandas as pd   #Importo la libreria Pandas
import gdown         #Importo la libreria gdown(en el caso de un drive)
google_drive_URL = 'https://drive.google.com/file/d/1SnzP5aANk2QB5eok3owepxQQwHSG0nRh/view' #Enlace del CSV
gdown.download(google_drive_URL, 'archivo.csv', quiet=False) #Descargo el CSV
df = pd.read_csv('archivo.csv')   #Le pido a python que lea el CSV
print(df.head(5)) #Le pido a python que me muestre las priemras 5 filas del CSV