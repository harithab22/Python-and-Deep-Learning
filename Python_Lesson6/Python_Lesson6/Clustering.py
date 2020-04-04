import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")


dataset = pd.read_csv('CC.csv')

print(dataset.dtypes)

"""
cor = dataset.corr()
# Printing the correlation with the target feature "quality"
print(cor['TENURE'].sort_values(ascending=False)[:6],'\n')
"""

# splitting the features and class
x = dataset.iloc[:,[2, -5,-6]]
y = dataset.iloc[:,-1]
print(x.shape, y.shape)

# see how many samples we have of each species
print(dataset["TENURE"].value_counts())

## Printing the count of Null values
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

## Replacing null values with mean values
x = x.select_dtypes(include=[np.number]).interpolate().dropna()

## Verifying Null values after replacing it with the mean value
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# Scatter plotting all the features
combine_dataset = dataset.iloc[:,[-1, 2, -5,-6]]
g = sns.pairplot(combine_dataset, hue="TENURE")
# sns.FacetGrid(dataset, hue="TENURE", size=4).map(plt.scatter, "CREDIT_LIMIT", "PURCHASES_TRX").add_legend()
# sns.FacetGrid(dataset, hue="TENURE", size=4).map(plt.scatter, "BALANCE_FREQUENCY", "PAYMENTS").add_legend()
# sns.FacetGrid(dataset, hue="TENURE", size=4).map(plt.scatter, "CREDIT_LIMIT", "BALANCE_FREQUENCY").add_legend()
# do same for petals
# sns.FacetGrid(dataset, hue="TENURE", size=4).map(plt.scatter, "PetalLengthCm", "PetalWidthCm").add_legend()
plt.show()

# Standard scaling the features
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)


# Building the k-means algorithm
from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print("Silhoutte Score: " + str(score))

# ##elbow method to know the number of clusters
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()