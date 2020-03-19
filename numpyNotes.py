import numpy as np
import matplotlib.pyplot as plt

'''
a = np.array([1,3,5,6,7]) #Creating a numpy array
print(np.array([[1,2],[3,4]], "complex")) #Creating   a 2-dim numpy array and changing the datatype

b = np.arange(1.1,13.1)
print(b/2)

print(np.arange(20, dtype= "complex")) #Creates a numpy array as a range of numbers

print(np.zeros((5,3), dtype=int)) #returns array filled w/ zeros; parameters are shape: no.of dimensions as well as size in each dimension; dtype

print(np.ones((5,3), dtype=int, order="F"))  #Order changes how data is stored in memory --> Column major or row major("F" for Fortran) --> Does not affect how output is displayed tho

print(np.empty((5,3), dtype=int)) #Returns an empty array w/ uninitialized cells

print(np.linspace(2, 3, num=7, retstep=True)) #linspace is similar to arange but start and stop are mandatory and other parametrs are opt.( num ~ # of entries in array , endpoint ~ if stop should be included, retstep ~ returns step size
print(np.linspace(2, 3, num=5, endpoint=False))
print(np.linspace(2, 3, num=5, retstep=True ))

#EYE: Returns a matrix RREF 
print(np.eye(3,3, dtype=int))
print("")
print(np.eye(3,4, 2, dtype=int))

array_name.size --> gives length of array 


myarray = np.arange(35)
myarray.shape = (7,5)
print(myarray)

#Both ways of indexing array work
print(myarray[5,2])
print(myarray[5][2])

#Boolean mask arrays: array_name = (a boolean statement)

myarray= np.arange(36)
boolean_array = 0 == (myarray % 5)

#array_name[boolean_array] -> returns array w/ entries where corresponding entries in boolean_array are true
subarray = myarray[boolean_array]
print(subarray)

print(subarray[subarray > 20])

#Normal arrays do not support above
array = {0, 5, 10, 15, 20, 25}
print(array[array > 15])


#"Combined masK" : Using numpy's logical operations ~ np.logical_...() ~ to produce arrays that satisfy conditions
myarray = np.arange(50)
boolean_array = 0 == (myarray % 7)

greaterthan_20 = myarray > 20 #Produces a boolean
print(greaterthan_20)

both_bool = np.logical_and(boolean_array, greaterthan_20)

#print(both_bool)
print(myarray[both_bool])

print(myarray[greaterthan_20])

#Some Additional Stuff

my_3D_array = np.arange(70)
my_3D_array.shape = (2, 7, 5)
print(my_3D_array)

print(my_3D_array.ndim)
print(my_3D_array.dtype)

#NOTE DIFFERENCE BELOW!!!!!
array = [0,5,10,15]
print(array * 2)
nparray = np.array([0,5,10,15])
print(nparray*2)

left_mat = np.arange(6).reshape(2,3)
right_mat = np.arange(15).reshape(3,5)
#np.inner(left_mat, right_mat) --> returns the inner product of two --> used for 1D arrays

#print(np.dot(left_mat, right_mat)) #Returns Dot product of two matrices --> dot product of 2D array is essentially matrix multiplication

array = np.arange(15).reshape(3,5)
print(array)
print(array.sum(axis=0))

#NUMPY STRUCTURED ARRAYS
person_data_def = [('name', 'S6'), ('height', 'f8'), ('weight', 'f8'), ('age', 'i8')]
#print([person_data_def])

people_array = np.zeros((4), dtype= person_data_def)

people_array[3] = ('Delta', 73, 205, 34)

people_array[0] = ('Alpha', 65, 112, 23)

print(people_array)
print()

ages = people_array[['height','age']] #still treated as a numpy array; if I want to print out more data types --> need more brackets (use 1 bracket to represent a tuple & other to represent array of tuples
print(ages)

#Also work with multidimensional arrays

people_big_array = np.zeros((4,3,2), dtype = person_data_def)

#RECORD ARRAYS
person_data_def = [('name', 'S6'), ('height', 'f8'), ('weight', 'f8'), ('age', 'i8')]

person_record_array = np.rec.array([('Delta', 73, 205, 34),('Alpha', 65, 112, 23)], dtype = person_data_def)

print(person_record_array[0].age)

#MATPLOTLIB
my_first_figure = plt.figure("My First Figure")

subplot_1 = my_first_figure.add_subplot(2, 3, 1)
subplot_2 = my_first_figure.add_subplot(2, 3, 6)

plt.plot(np.random.rand(50).cumsum(), 'k--')
plt.show()

subplot_2 = my_first_figure.add_subplot(2,3,2)
plt.plot(np.random.rand(50), 'go')
plt.show()
'''

#RUNS IN EXPONENTIAL RUN TIME
def fibonacci(term):
    if term == 1:
        return 0
    elif term == 2:
        return 1
    else:
        return fibonacci(term - 1) + fibonacci(term - 2)


print(fibonacci(32))