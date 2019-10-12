#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.version.version)
"""
1.16.4
"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2,3,5))


#4. Print a.
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))



#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
a.size == b.size """True"""
#Pero eso solo dice el numero de elementos, que sí es igual
a.shape == b.shape """False"""
#No tienen la misma forma


#8. Are you able to add a and b? Why or why not?
print(a+b)
""" ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) """
#No porque no tienen la misma forma.

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = b.transpose()
print(c.shape) """(3, 2, 5) lo que significa que todavia no se pueden sumar"""

c3 = np.reshape(b,(2, 3, 5))
print(c3.shape) """(2, 3, 5) ahora sí se puede"""

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
print(a+c)
"""ValueError: operands could not be broadcast together with shapes (2,3,5) (3,2,5)"""
d = a + c3
""" Así si se puede sumar"""

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)
"""
[[[0.10089404 0.47425582 0.65888045 0.42768441 0.75238416]
  [0.35549729 0.61287511 0.92889048 0.98137872 0.36459196]
  [0.75622695 0.44622602 0.45861232 0.81349337 0.28433015]]

 [[0.97756303 0.10268017 0.97294379 0.06021004 0.89129591]
  [0.20659711 0.07436427 0.6045743  0.1838502  0.46637056]
  [0.56628554 0.58463528 0.35290935 0.39668979 0.2166689 ]]]
  
[[[1.10089404 1.47425582 1.65888045 1.42768441 1.75238416]
  [1.35549729 1.61287511 1.92889048 1.98137872 1.36459196]
  [1.75622695 1.44622602 1.45861232 1.81349337 1.28433015]]

 [[1.97756303 1.10268017 1.97294379 1.06021004 1.89129591]
  [1.20659711 1.07436427 1.6045743  1.1838502  1.46637056]
  [1.56628554 1.58463528 1.35290935 1.39668979 1.2166689 ]]]
  
  Noto que difieren en 1 en cada elemento, no noto una diferencia de decimales, 
"""

#12. Multiply a and c. Assign the result to e.
e = a*c3
"""
       [[[0.10089404, 0.47425582, 0.65888045, 0.42768441, 0.75238416],
        [0.35549729, 0.61287511, 0.92889048, 0.98137872, 0.36459196],
        [0.75622695, 0.44622602, 0.45861232, 0.81349337, 0.28433015]],

       [[0.97756303, 0.10268017, 0.97294379, 0.06021004, 0.89129591],
        [0.20659711, 0.07436427, 0.6045743 , 0.1838502 , 0.46637056],
        [0.56628554, 0.58463528, 0.35290935, 0.39668979, 0.2166689 ]]]
"""


#13. Does e equal to a? Why or why not?
e == a
"""
array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])
        
        
c3 viene de reshapear la matriz de unos que era b, la multiplicación de a*c3 fue elemento por elemento por lo que a no cambió, a*c3 no es la multiplicación de matrices matemática usual        
"""


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print(d_max, d_min, d_mean) """1.9813787182558984 1.0602100424123968 1.502461981907922 """


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2,3,5))
print(f)
"""
[[[6.92888001e-310 6.92888005e-310 6.92888002e-310 6.92888453e-310
   6.92888001e-310]
  [6.92888001e-310 6.92888002e-310 6.92888002e-310 6.92888002e-310
   6.92887997e-310]
  [6.92888456e-310 6.92888002e-310 6.92888454e-310 6.92888002e-310
   6.92888456e-310]]

 [[6.92888454e-310 6.92888002e-310 6.92888454e-310 6.92887997e-310
   6.92888002e-310]
  [6.92888455e-310 6.92888455e-310 6.92888456e-310 6.92888002e-310
   6.92888249e-310]
  [6.92888456e-310 6.92888002e-310 6.92888002e-310 6.92888453e-310
   6.92887997e-310]]]

Crea un arreglo de los valores más cercanos a cero, pero no cero
"""



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
for i in range(2):
    for j in range(3):
        for k in range(5):
            if f[i][j][k] == d_mean:
                f[i][j][k] = 50
            elif f[i][j][k] > d_min and f[i][j][k] < d_mean:
                f[i][j][k] = 25
            elif f[i][j][k] > d_mean and f[i][j][k] < d_max:
                f[i][j][k] = 75
            elif f[i][j][k] == d_min:
                f[i][j][k] = 0
            elif f[i][j][k] == d_max:
                f[i][j][k] = 100
            else: False
print(f)
"""
[[[ 25.  25.  75.  25.  75.]
  [ 25. 100.  25.  25.  25.]
  [ 75.  25.  75.  75.  25.]]

 [[ 25.  25.  25.  75.  75.]
  [ 75.  75.  25.  25.  25.]
  [ 75.   0.  75.  25.  25.]]]
  
Yey :)  
"""


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
#La respuesta está incluida arriba, en la 16

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

g = np.empty((2,3,5),str)

for i in range(2):
    for j in range(3):
        for k in range(5):
            if d[i][j][k] == d_mean:
                g[i][j][k] = 'C'
            elif d[i][j][k] > d_min and d[i][j][k] < d_mean:
                g[i][j][k] = 'B'
            elif d[i][j][k] > d_mean and d[i][j][k] < d_max:
                g[i][j][k] = 'D'
            elif d[i][j][k] == d_min:
                g[i][j][k] = 'A'
            elif d[i][j][k] == d_max:
                g[i][j][k] = 'E'
            else: False
print(g)

"""
[[['B' 'D' 'B' 'D' 'A']
  ['B' 'E' 'D' 'B' 'B']
  ['B' 'D' 'B' 'B' 'D']]

 [['B' 'B' 'D' 'B' 'D']
  ['D' 'D' 'D' 'B' 'B']
  ['B' 'D' 'B' 'D' 'B']]]
  
 Yey :) 
"""