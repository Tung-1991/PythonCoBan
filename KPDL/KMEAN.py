import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

data=pd.read_csv('Example.csv')
print(data)

plt.scatter(data['Satisfaction'],data['Loyalty'])
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()

dulieu = data.copy()
k = KMeans(2)
k.fit(dulieu)

phancum=dulieu.copy()
phancum['cluster_pred']=k.fit_predict(dulieu)

plt.scatter(phancum['Satisfaction'],phancum['Loyalty'],c = phancum['cluster_pred'],cmap = 'rainbow')
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()

thuoctinh=[]
for i in range(1,30):
    k=KMeans(i)
    k.fit(dulieu)
    thuoctinh.append(k.inertia_)
print(thuoctinh)

plt.plot(range(1,30),thuoctinh)
plt.xlabel('Cụm')
plt.ylabel('thuộc tính')
plt.show()

kn = KMeans(4)
kn.fit(dulieu)
phancumm=data.copy()
phancumm['cluster_pred']=kn.fit_predict(dulieu)
print(phancumm)

plt.scatter(phancumm['Satisfaction'],phancumm['Loyalty'],c = phancumm['cluster_pred'],cmap = 'rainbow')
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()


