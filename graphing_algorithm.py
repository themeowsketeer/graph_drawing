import matplotlib.pyplot as plt
import numpy as np

x = [10,50,100,200,500,1000] #given set of n value
y = [3.2,9.4,21.8,21.8,51.8,92.4] #average executed time of Insertion Sort
z = [93,19,49.2,57.4,132.4,245.4] #average executed time of Quick Sort
t = [6.4,5.4,12.8,26,71,129.4] #average executed time of Merge Sort

plt.figure(figsize=(50, 10)) #set out size of the figure

plt.scatter(x, y) ; plt.scatter(x, z) ; plt.scatter(x, t) #mapping out all points of all 3 data sets

#for i in range(0,len(x)):
#    plt.annotate("n={0}".format( x[i] ) , xy=( x[i] , z[i] )) #Insertion Sort
#
#    plt.annotate("n={0}|t={1}".format( x[i] , z[i] ) , xy=( x[i] , z[i] )) #Quick Sort
#    
#    plt.annotate("n={0}|t={1}".format( x[i] , t[i] ) , xy=( x[i] , t[i] )) #Merge Sort
#Used for naming each point on the graph with respective coordinations. Not practical due to overlapping and overlapped by each other

#plotting the points altogether
plt.plot(x, y, label='Insertion Sort') ; plt.plot(x, z, label='Quick Sort') ; plt.plot(x, t, label='Merge Sort') 

#labelling the x-axis and y-axis
plt.xlabel('n value') ; plt.ylabel('Average time executed (ms)')

#labelling the general graph
plt.title("Graph of executed time by 3 sorting algorithms")

#customizing the grid in corresponding to x-coordinate of x point. for y-grid the value will be divided into 26 spaces
plt.xticks(x, x) ; plt.yticks(np.arange(0,275,25), np.arange(0,275,25))

#showing legend for each plot of data set, the grid and the final graphing
plt.legend() ; plt.grid(True) ; plt.show()

# (x*list(map(mth.log, x)): revamp the value so that it can be used in the operators
# import matplotlib as mpl
# import numpy as np
# import math as mth