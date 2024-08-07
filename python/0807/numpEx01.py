import matplotlib.pyplot as plt
X=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
Y=[15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2=[20.1, 30.9, 26.8, 67.6, 46.3, 36.9, 25.9]
Y3=[23.1, 33.9, 23.8, 62.6, 44.3, 36.9, 25.9]
plt.plot(X,Y,label="Seoul")
plt.plot(X,Y2,label="Busan")
plt.bar(X,Y3,label="Tusan")
plt.xlabel("day")
plt.ylabel("num")
plt.legend(loc="upper left")
plt.show()

