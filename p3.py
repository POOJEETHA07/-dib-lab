import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
plt.figure(figsize=(14,10))
plt.subplot(3,2,1)
plt.plot(x,y1,label='sin(x)',color='b')
plt.plot(x,y2,label='cos(x)',color='r',linestyle='--')
plt.title('Line Plot')
plt.legend()
plt.subplot(3,2,2)
plt.scatter(x,y1,color='g',label='sin(x)')
plt.scatter(x,y2,color='m',label='cos(x)')
plt.title('Scatter Plot')
plt.legend()
categories=['A','B','C','D']
values=[25,30,35,40]
plt.subplot(3,2,3)
plt.bar(categories,values,color='pink')
plt.title('Bar Plot')
data=np.random.normal(0,1,1000)
plt.subplot(3,2,4)
plt.hist(data,bins=30,color='orange',edgecolor='black')
plt.title('Histogram')
sizes=[15,30,45,10]
labels=['Apple','Orange','Banana','Mango']
plt.subplot(3,2,5)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'yellowgreen','lightcoral', 'lightskyblue'])
plt.title('Pie Chart')
plt.subplot(3,2,6)
data1=np.random.normal(0,1,100)
data2=np.random.normal(0,2,100)
plt.boxplot([data1,data2], tick_labels=['Group 1','Group 2'])
plt.title('Box Plot')
plt.tight_layout()
plt.show()