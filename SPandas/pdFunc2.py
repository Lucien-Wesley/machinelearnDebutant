print()
print()
print("Resultat")

import pandas as pd

data = {'nom': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'âge': [25, 28, 21, 32, 30],
        'ville': ['Paris', 'Londres', 'New York', 'Londres', 'Paris']}

df = pd.DataFrame(data)

print(df)




print()
print()
print("Resultat")



#Pour accéder aux données d'une colonne particulière, vous pouvez utiliser la syntaxe suivante :
df['nom']

index = 2

#Pour accéder aux données d'une rangée particulière, vous pouvez utiliser la syntaxe suivante :
df.loc[index]


#Pour accéder aux données d'une cellule particulière, vous pouvez utiliser la syntaxe suivante :
df.at[index, "ville"]

print()
print()
print("Resultat")


import pandas as pd

data = {'nom': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'âge': [25, 28, 21, 32, 30],
        'ville': ['Paris', 'Londres', 'New York', 'Londres', 'Paris']}

df = pd.DataFrame(data)

total_age = df['âge'].sum()

print(total_age)

print()
print()
print("Resultat")


import pandas as pd

df = pd.read_csv("monfichier.csv")
print(df.head())


#L'option ``head()`` permet d'afficher les premières lignes du dataframe pour vérifier si le fichier a été chargé avec succès.











