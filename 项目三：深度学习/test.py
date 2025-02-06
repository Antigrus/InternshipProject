from sklearn.linear_model import LinearRegression #导入线性回归模型
import matplotlib.pyplot as plt #绘图库
import numpy as np

x = np.array([121, 125, 131, 141, 152, 161]).reshape(-1,1)#x 是房屋面积，作为特征
y = np.array([300, 350, 425, 405,496,517])#y 是房屋的
plt.scatter(x,y)
plt.xlabel("area")#添加横坐标面积
plt.ylabel("price")#添加纵坐标价

lr = LinearRegression()#将线性回归模型封装为对象
lr.fit(x,y)#模型在数据上训

w = lr.coef_#存储模型的斜率
b = lr.intercept_#存储模型的截距
print('斜率:',w)
print('截距:',b)

plt.scatter(x,y)
plt.xlabel("area")#添加横坐标面积
plt.ylabel("price")#添加纵坐标价格
plt.plot([x[0],x[-1]],[x[0]*w+b,x[-1]*w+b])

plt.show()

