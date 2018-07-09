# coding=utf-8
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#读取数据，传入文件名，返回n,delay,time
def readData(fileName):
    originalData=pd.read_csv(fileName)
    n=originalData['n'].values
    delay=originalData['delay'].values
    time=originalData['time'].values
    return n,delay,time
def main():     
    fileName="data/test.csv"
    X,Y,Z=readData(fileName)#返回读取数据的结果
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
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.linspace(0, 1, 100)
    z = np.sin(x * 2 * np.pi) / 2 + 0.5
    for n in range(1,11):
        ax.plot(x, z, zs=n, zdir='y')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
if __name__=='__main__':
    main()