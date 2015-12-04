Wrote profile results to testeBubble.py.lprof
Timer unit: 1e-06 s

Total time: 0.001187 s
File: /home2/Dropbox/AnaliseAlgoritmos/aula3/src/ordena.py
Function: bubble_sort at line 3

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     3                                           @profile
     4                                           def bubble_sort(a):
     5                                               """ Implementação do método da bolha """
     6        33           20      0.6      1.7      for i in range(len(a)):
     7       528          253      0.5     21.3          for j in range(len(a)-1-i):
     8       496          392      0.8     33.0              if a[j] > a[j+1]:
     9       271          161      0.6     13.6                  t = a[j]
    10       271          201      0.7     16.9                  a[j] = a[j+1]
    11       271          160      0.6     13.5                  a[j+1] = t

