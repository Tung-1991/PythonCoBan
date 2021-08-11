import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

data=pd.read_csv('chuanhoa.csv')
thuoctinh=[]

for i in range(1,514):
    kn=KMeans(i)
    kn.fit(data)
    thuoctinh.append(kn.inertia_)
print(thuoctinh)

plt.plot(range(1,514),thuoctinh)
plt.xlabel('Cụm')
plt.ylabel('thuộc tính')
plt.show()

kn = KMeans(10)
kn.fit(data)
data['Cụm']=kn.fit_predict(data)
print(data)

plt.scatter(data['month'],data['area'],data['Cụm'],cmap = 'rainbow')
plt.xlabel('month')
plt.ylabel('area')
plt.show()

print(kn.cluster_centers_)

def tinh (n):
    l = []
    for i in data['Cụm']:
        l.append(i)
    print("instance",l.count(n))
    t = (l.count(n) / 514) * 100
    return t
for i in range(0,10):
    print(tinh(i))
