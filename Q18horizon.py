import matplotlib.pyplot as plt

y=['java', 'python', 'php', 'javascript', 'c#', 'c++']
x=[22.2, 27.6, 8.8, 8, 7.7, 6.7]

plt.barh(y,x)

plt.ylabel('programming languages')
plt.xlabel('popularity')
plt.title('horizontal bar graph')

plt.show()