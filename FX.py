# coding=utf-8
from matplotlib import pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd
codeOfCurve = 1 #0代表时延，1代表丢包率 
fileName=['data/delay.CSV','data/PacketLossRate.CSV']
color=['r','g','y','b']
xLabel=['Delay','Packet Loss Rate']
title=['CDF of Delay','CDF of Pakcet Loss Rate']
    #返回dataframe
originalData=pd.read_csv(fileName[codeOfCurve],header=None)
    #获取数据总行数
dataSize=originalData.shape[0]
numbersOfDataRate=[5,15,25,35]
    #按行打印出所有的数据
plt.figure(figsize=(16,9), dpi=100)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
for row in range(0,dataSize): 
        sample=originalData[row:row+1].values[0]
        ecdf = sm.distributions.ECDF(sample)
        print (sample)        
        x = np.linspace(0, max(sample),100)
        y = ecdf(x)
        z1 = np.polyfit(x, y, 3)#用3次多项式拟合
        p1 = np.poly1d(z1)
        yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
        plt.plot(x, yvals, color[row],label=numbersOfDataRate[row])

# plt.ylim(0,1)
plt.xlabel(xLabel[codeOfCurve]) 
plt.ylabel("CDF") 
# plt.xlabel('丢包率') 
# plt.ylabel('丢包率累计概率分布曲线') 
plt.legend(loc=4)
plt.title(title[codeOfCurve]) 
plt.savefig('CDF.png') 
plt.show()  



# from matplotlib import pyplot as plt
# import pandas as pd
# import numpy as np
# import seaborn as sn
# from mpl_toolkits.mplot3d import Axes3D

#读取数据，传入文件名，返回n,delay,time
# def readData(fileName):
#     originalData=pd.read_csv(fileName)
#     n=originalData['n'].values
#     delay=originalData['delay'].values
#     time=originalData['time'].values
#     return n,delay,time
# def main():     
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
# 
# # load some test data for demonstration and plot a wireframe
#     X = np.arange(-4, 4, 0.25)
#     Y = np.arange(1,33)
#     Z = (X**3 - X**2 + X - Y)
#     ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
# 
# # rotate the axes and update
#     for angle in range(0, 360):
#         ax.view_init(30, angle)
#         plt.draw()
#         plt.pause(.001)
#     fileName="data/test.csv"
#     originalData=pd.read_csv(fileName)
#     x=originalData[2:5]
#     print(x)
    #绘制三维曲面图
    # 
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # X = np.arange(-4, 4, 0.25)
    # Y = np.arange(-4, 4, 0.25)
    # X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X**2 + Y**2)
    # Z = np.sin(R)
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    # plt.show() 
    
#绘制散点图
#     ax = plt.subplot(111, projection='3d')
#     ax.scatter(X,Y,Z,c='r') 
#     plt.show()
    
#在立体坐标系中绘多条2D曲线（以沿着Y轴画10条正弦曲线为例）
#     fig = plt.figure()
#     ax = fig.gca(projection='3d')
#     x = np.linspace(0, 1, 100)
#     z = np.sin(x * 2 * np.pi) / 2 + 0.5
#     for n in range(1,11):
#         ax.plot(x, z, zs=n, zdir='y')
#     ax.set_xlim(0, 1)
#     ax.set_ylim(0, 10)
#     ax.set_zlim(0, 1)
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     plt.show()
#     testData=np.random.randn(100)
#     sn.kdeplot(testData) 
# if __name__=='__main__':
#     main()

# 
# import matplotlib.pyplot as plt 
# from scipy.optimize import curve_fit 
# import numpy as np
# import statsmodels.api as sm
# 
# sample = np.loadtxt('E:\\Tencent\\画图\\DelayData200.txt', skiprows=1)
# ecdf = sm.distributions.ECDF(sample)
# 
# x = np.linspace(min(sample), max(sample),1000)
# y = ecdf(x)
# 
# def func(x,a,b): 
#     return a*np.exp(b/x) 
# 
# popt, pcov = curve_fit(func, x, y) 
# a=popt[0]#popt里面是拟合系数，读者可以自己help其用法 
# b=popt[1] 
# yvals=func(x,a,b) 
# plot1=plt.plot(x, y,‘*’,label=’original values’) 
# plot2=plt.plot(x, yvals, ‘r’,label=’curve_fit values’) 
# plt.xlabel(‘x axis’) 
# plt.ylabel(‘y axis’) 
# plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法 
# plt.title(‘curve_fit’) 
# plt.show() 
# plt.savefig(‘p2.png’) 