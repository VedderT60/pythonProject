import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a=np.arange(12).reshape((4,3))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1)) #odnosimy sie wartościami do wierszy w axisie
#
# print(a.cumsum(axis=1))
#
# b=np.array([20,30,40,50])
# c=np.arange(4)
#
# d=c+b
# print(d)
# print(np.sqrt(c))
# e=np.sqrt(c)
# f=d+e
# print(f)

# a=np.array([[2,5,1],[5,7,1]])
# b=np.array([[2,3],[4,5],[7,1]])
# c=np.dot(a,b) #mnozenie maciezy z zachowaniem majcy
# print(c)
# d=a.dot(b)
# print(d)
#
# e=np.arange(3)
# f=np.arange(3)
# print(np.dot(e,f)) #mnozenie wszystkich elementow razem zgodnie z zasadami mnozenia
# g=np.arange(3)
# h=np.arange([[0],[1],[2]])
# print(g.dot(h))

# a=np.arange(6).reshape((3,2)) #towrzenie plaskiej tablicy i dostep mamy do kazdego z el. oddzielnie
# print(a) #liczba kolumn razy liczba wierszy musi sie rownac ilosci elementow w tablicy wyjsciowej
# # for b in a.flat:
# #     print(b)
# c=a.reshape((2,3)) #mozna zmieniac wymiary macierzy
# print(c)
# b=c.ravel() #splaszczona macierz
# print(b)
# d=c.T #transpozycja - zamiana wierszy i kolumn
# print(d)

# s=pd.Series([1,3,4,'a',3.5]) #dodaje etykiete do obiektu
# print(s)
# s2 = pd.Series([10,12,14,8], index=['a','b','c','d'])
# print(s2)

#tworzenie tabelki danych jako slownik z indexami auto nadajacymi sie
# data={'Kraj':['Belgia','Indie','Polska'],'Stolica':['Bruksela','New Delhi','Warszawa'],'Populacja':[1118123,123123123,3241343]}
# df=pd.DataFrame(data)
#print(df)
# print(s['a']) #wyswietlanie wartosci danego indeksu
# print(s.a)
#
# print(df[0,1])
# print(df['Kraj']) #wyswietla tak cala kolumne
# print(df.iloc([0],[0])) # podajemy dokladny indeks elementu ktorego chcemy wyciagnac
# print(df.loc([0],['Kraj'])) #indeks wiersza i nazwe kolumny
# print(df.at[0,'Kraj'])
# print(df.sample(2))#losowe wyciaganie wierszy
#print(df.sample(10), replace=True)
# daty=pd.date_range('20220507', periods=5) #seria dat w danym formacie rrrrmmdd
# print(daty)
# df2=pd.DataFrame(np.random.randn(5,4),index=daty, columns=list('ABCD')) #ramka danych jako indeksy na daty i powyzej nazwy kolumn
# print(df2)

df3 = pd.read_csv('dane.csv', header=0, sep=';', decimal=".")
print(df3)
# df3.to_csv('dane2.csv',index=False)
#openpyxl - biblioteka do xlsx
xlsx = pd.ExcelFile('data/ludnosc.xlsx')
df=pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('ludnosc.xlsx', sheet_name='dane')

# new = df.drop([3])
# print(new)
# df.drop([3], inplace=True)
# print(df)
# df["Kontynent"] = ["Europa", 'Azja', 'Ameryka Południowa', 'Europa']
# print(df)
# df.sort_values(by='Kraj', inplace=True)
# print(df)
#
# grupa = df.groupby(by='Kontynent')
# print(grupa.get_group('Europa'))
# grupa = df.groupby(by='Kontynent').agg({'Populacja': ['sum']})
# print(grupa)
#
# # grupa.plot(kind='bar', xlabel='Kontynenty',
# #            ylabel='Populacja w mld', rot=0,
# #            title='Populacja na kontynentach')
# wykres = grupa.plot.bar()
# wykres.set.xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.set_title('Populacja na kontynentach')
# plt.savefig('plot2.png')
# plt.show()

# grupa = df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(8, 8),
#            colors=['red', 'green'])
# plt.legend(loc='upper left')
# plt.show()

seria = pd.Series(np.random.randn(1000))
seria = seria.cumsum()

seria.plot()
plt.show()