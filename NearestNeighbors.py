from sklearn.neighbors import NearestNeighbors
import numpy as np
import time
inicio = time.time()
A = []
# Importar el dataset
dataset = pd.read_csv('test100.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test1000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test10000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test100000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test1000000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test20000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test200000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test350000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test500.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test5000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test500000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='kd_tree').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
A.append(time_finit)
print(fin-inicio)




inicio = time.time()
B = []
# Importar el dataset
dataset = pd.read_csv('test100.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test1000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test10000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test100000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test1000000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test20000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test200000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test350000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test500.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test5000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)

# Importar el dataset
dataset = pd.read_csv('test500000.csv')
punto = dataset.iloc[:, [1,2,3]].values

nbrs = NearestNeighbors(n_neighbors=3, algorithm='brute').fit(punto)
distances, indices = nbrs.kneighbors(punto)

fin = time.time()
time_finit = fin-inicio
B.append(time_finit)
print(fin-inicio)