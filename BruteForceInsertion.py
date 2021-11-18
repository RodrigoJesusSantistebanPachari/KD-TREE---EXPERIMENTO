import numpy as np
import pandas as pd
import time
#######################################
inicio = time.time()
dataset = pd.read_csv('test100.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test500.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test1000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test5000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test10000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test20000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test100000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test200000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test350000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test500000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################
#######################################
inicio = time.time()
dataset = pd.read_csv('test1000000.csv')
punto = dataset.iloc[:, 1].values

root = build(punto)

fin = time.time()
print(fin - inicio)
#######################################