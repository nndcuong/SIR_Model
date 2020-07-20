import numpy as np
import scipy.stats as st
import seaborn as sns
from matplotlib import pyplot as plt
import math
import pylab
import csv
from sampling import metropolis_hastings
from sampling import circle
from sampling import pgauss
from regionize_data import regionize
# def read_csv(file_name):
#     with open(file_name) as csv_file:
#         l = []
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if(line_count == 1):
#                 l = list(map(int,row[4:]))
#             elif(line_count >1):
#                 int_row = list(map(int,row[4:]))
#                 for i in range(len(int_row)):
#                     l[i] += int_row[i]
#             line_count +=1
#     return l
# #to test!!
# file_i ='data/time_series_covid19_confirmed_global.csv'
# file_r = 'data/time_series_covid19_deaths_global.csv'


s,i,r = regionize()
x = [i+j for (i,j) in zip(i,r)]
while x[0] == 0:
    x.pop(0)
samples = metropolis_hastings(circle,len(x))
beta = samples[:,0]
gamma = samples[:,1]
E_R0 = 0
for i in range(len(beta)):
    pi = 1.
    for val in x:
        pi *= math.exp(beta[i]*math.log(gamma[i]) - math.log(math.gamma(beta[i])) + (beta[i]-1)*math.log(val) - gamma[i]*val)
    E_R0 += pi *beta[i]/gamma[i]
print(E_R0)