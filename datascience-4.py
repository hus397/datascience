import matplotlib.pyplot as mp
import numpy as np
#line graph - need x and y values
"""x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, -1, 2, -3, 5, -8, 13, -21, 34, -55]
mp.xlabel('time')
mp.ylabel('velocity')
mp.title('v(t) graph', loc='center', fontdict={'family':'Segoe UI', 'color':'green', 'size':30})
mp.plot(x, y)
mp.show()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
mp.barh(x, y)
mp.show()

sports = ['football', 'tennis', 'boxing', 'cricket', 'rugby']
hours = [2, 5, 8, 6, 9]
mp.pie(hours, labels=sports, shadow=True, autopct='%1.1f%%', startangle=90)
mp.show()"""

values = np.random.randint(0, 100, 50)
bins = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
mp.hist(values, bins=bins)
mp.show()
