import csv 
import matplotlib.pyplot as plt

f=open("pjesme.csv")
sadrzaj= csv.DictReader(f)

broj_pjesma={}

for pjesma in sadrzaj:
    zanr=pjesma["Genre"]
    if zanr in broj_pjesma:
        broj_pjesma[zanr]+=1
    else:
        broj_pjesma[zanr]=1

f.close()
print(broj_pjesma)

plt.figure(figuresize=(10,6))
plt.bar(broj_pjesma.keys(),broj_pjesma.values(),color="red")
plt.xlabel("Zanr")
plt.ylabel("broj pjesama")
plt.title("broj pjesama po zanru")
plt.xticks(rotation=90)
plt.show()
