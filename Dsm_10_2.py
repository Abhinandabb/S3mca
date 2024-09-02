[02/09, 2:41 pm] +91 95264 35933: import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 18])
ypoints = np.array([3, 10, 12, 20])

plt.plot(xpoints, ypoints,marker = 'o',color="red",mec = 'g', mfc = 'g',linestyle = 'dotted')
plt.show()
[02/09, 2:41 pm] +91 95264 35933: Matplotlib_1
[02/09, 2:42 pm] +91 95264 35933: import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([12,14,16,18,20,22,24])
ypoints = np.array([100,200,250,400,300,450,500])

plt.plot(xpoints, ypoints,marker = 'o',color="red",mec = 'g', mfc = 'g',linestyle = 'dotted')
plt.show()
[02/09, 2:42 pm] +91 95264 35933: Mathplotlib_2
[02/09, 2:43 pm] +91 95264 35933: import matplotlib.pyplot as plt

with open("3_data.txt") as f:
    data = f.read()
    
data = data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x, y)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('graph')
plt.show()
[02/09, 2:43 pm] +91 95264 35933: Matplotlib_3
[02/09, 2:44 pm] +91 95264 35933: import matplotlib.pyplot as plt


x1 = [10,20,30]
y1 = [10,20,30]
plt.plot(x1, y1, label = "line 1")

x2 = [30,40,50]
y2 = [30,40,50]
plt.plot(x2, y2, label = "line 2")

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('Two Line plot')

plt.legend()
plt.show()
[02/09, 2:44 pm] +91 95264 35933: Matplotlib_4
[02/09, 2:45 pm] +91 95264 35933: import matplotlib.pyplot as plt

figure, axis = plt.subplots(2,2)


x1 = [10,20,30]
y1 = [10,20,30]
axis[0, 0].plot(x1, y1)
axis[0, 0].set_title("Plot 1")

x2 = [10,10,10]
y2 = [30,40,50]
axis[0, 1].plot(x2, y2)
axis[0, 1].set_title("Plot 2")

plt.show()
[02/09, 2:46 pm] +91 95264 35933: Matplotlib_5
[02/09, 2:46 pm] +91 95264 35933: import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':7.7,'C++':6.7}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='maroon',width = 0.4)

plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()
[02/09, 2:46 pm] +91 95264 35933: Matplotlib_6 (a)
[02/09, 2:47 pm] +91 95264 35933: import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':7.7,'C++':6.7}

courses = list(data.keys())
values = list(data.values())

#fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.barh(courses, values, color ='red')

plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()
[02/09, 2:48 pm] +91 95264 35933: Matplotlib_6(b)
[02/09, 2:48 pm] +91 95264 35933: import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':7.7,'C++':6.7}
color=("red","yellow","maroon","green","black","cyan")
courses = list(data.keys())
values = list(data.values())

#fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color =color)

plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()
[02/09, 2:48 pm] +91 95264 35933: Matplotlib_6(c)
[02/09, 2:50 pm] +91 95264 35933: import numpy as np
import matplotlib.pyplot as plt

y1 = [22,30,35,35,26]
y2 = [25,32,30,35,29]
x_labels = ['G1','G2','G3','G4','G5']
x1 = np.arange(5)
width = 0.40

plt.bar(x1-0.2,y1,color="green",width=width,label='Men')
plt.bar(x1+0.2,y2,color="red",width=width,label='Women')
plt.xticks(x1,x_labels)



plt.xlabel("Person")
plt.ylabel("Scores")
plt.legend()

plt.title("scores by group and gender")
plt.show()
[02/09, 2:51 pm] +91 95264 35933: Matplotlib_7
[02/09, 2:52 pm] +91 95264 35933: import pandas as pd

names = ['a','b','c']
x = pd.Series(names)
print(names)
[02/09, 2:52 pm] +91 95264 35933: Pandas 1
[02/09, 2:53 pm] +91 95264 35933: import pandas as pd

sr = pd.Series(pd.date_range('2021-05-01','2021-05-12',freq = 'D'))
# To avoid dtype
# Series.to_string
print(sr.to_string(index=False))
[02/09, 2:53 pm] +91 95264 35933: Pandas 2
[02/09, 2:53 pm] +91 95264 35933: import pandas as pd

details = {
    'Name' : ['a','b','c','d'],
    'Age' : [24,25,26,27],
}
  

df = pd.DataFrame(details)
  
print(df)
[02/09, 2:53 pm] +91 95264 35933: Pandas 3
[02/09, 2:54 pm] +91 95264 35933: import pandas as pd

details = [[1,2],[3,4]]
  
df = pd.DataFrame(details)
  
print(df)
[02/09, 2:54 pm] +91 95264 35933: Pandas 4
[02/09, 2:54 pm] +91 95264 35933: import pandas as pd

df = pd.read_csv('5_Pandas.csv')

print(df.to_string())
[02/09, 2:54 pm] +91 95264 35933: Pandas 5
[02/09, 2:55 pm] +91 95264 35933: import pandas as pd

df = pd.DataFrame({'Name': ['e','a','a','b','c','d'],
                   'Age': [1,2,1,3,3,4],
                   'Rank': [0,1,2,3,4,5]})

print(df.to_string())

print('SORTED DATAFRAME')
df = df.sort_values(by=['Name','Age'], ascending=[True,True])

print(df.to_string())
[02/09, 2:55 pm] +91 95264 35933: Pandas 6
[02/09, 2:56 pm] +91 95264 35933: import pandas as pd

data = {'Name': ['e','a','a','b','c','d'],
                   'Age': [1,2,1,3,3,4],
                   'Rank': [0,1,2,3,4,5]}

index = {'a1', 'b1', 'c1', 'd1', 'e1','f1'}

df = pd.DataFrame(data,index)
#df.reset_index(inplace = True)
print(df.to_string())
df.reset_index(inplace = True, drop = True)
print(df.to_string())
[02/09, 2:56 pm] +91 95264 35933: Pandas 7
[02/09, 2:56 pm] +91 95264 35933: import pandas as pd

details = {
    'Name' : ['a','b','c','d'],
    'Age' : [24,25,26,27],
}
  

df = pd.DataFrame(details)
  
print(df[:2])
[02/09, 2:57 pm] +91 95264 35933: Pandas 8
[02/09, 2:58 pm] +91 95264 35933: import pandas as pd

details = {
    'Name' : ['a','b','c','d','e'],
    'Occupation' : ['A1','A1','A1','B1','B1'],
    'Salary' : [20,30,40,27,23],
}
  

df = pd.DataFrame(details)
print(df)
occ_average_age = df.groupby('Occupation')['Salary'].mean()
print("Average salary per occupation : ")
print(occ_average_age)
[02/09, 2:58 pm] +91 95264 35933: Pandas 9
[02/09, 2:58 pm] +91 95264 35933: import pandas as pd
import numpy as np

nums = {'Set_of_Numbers': [2, 3, 5, 7, 11, 13,np.nan, 19, 23, np.nan]}
df = pd.DataFrame(nums, columns =['Set_of_Numbers'])
df['Set_of_Numbers'] = df['Set_of_Numbers'].fillna(0)
print(df)
[02/09, 2:58 pm] +91 95264 35933: Pandas 10
