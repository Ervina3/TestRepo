import matplotlib.pyplot as plt
#line chart
'''
x=[0,1,2,3,4]
y=[0,2,4,6,8]

plt.figure(figsize=(5,3))
plt.plot(x,y, label="2x",color='r', linewidth=2, linestyle='-',marker='*', markersize=5 )
plt.title('prva funkcija',fontdict={'fontname':'Arial','fontsize':15})

x2=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
y1=[elem ** 2 for elem in x2[:6]]
y2=[elem ** 2 for elem in x2[6:]]

plt.plot(x2[:6], y1, color='b' , label='x^2')
plt.plot(x2[6:] ,y2 , linestyle='--')
plt.xlabel('X osa')
plt.ylabel('Y osa')

plt.legend()
plt.savefig('funkcija.png')
plt.show()
'''
#bar chart
'''
labels=['A', 'B', 'C']
values=[1, 2 ,6]
bars= plt.bar(labels,values)
bars[0].set_hatch('/')
bars[1].set_hatch('o')
plt.savefig('barchart.png') 
'''
'''
stock_prices=[10, 12, 15, 18, 20, 22, 25]
dates=['Jan 1', 'Jan 2' , 'Jan 3', 'Jan 4', 'Jan 5', 'Jan 6', 'Jan 7']
plt.plot(dates, stock_prices)
plt.xlabel('Datum')
plt.ylabel('CIjena akcija')
plt.title('Kreitanje akcija')
plt.savefig('akcije.png')
'''



