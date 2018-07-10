# coding=utf-8
'''
实现福星实验数据读取以及数据分析绘图
author: 汪礼浩
date:   2018年7月10日
'''
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
def main():
##一些字符串数组
    color=['r','g','y','b','m']
    xLabel=['Delay','Packet Loss Rate']
    title=['CDF of Delay','CDF of Pakcet Loss Rate']

##按照delay和packet loss rate两种参数将不同数据流的CDF曲线绘制在一个子图里        
    codeOfCurve = 1 #0代表画时延CDF曲线，1代表丢包率CDF曲线    
    prefixFileName=['data/delay','data/PacketLossRate']
    colorIndex = 0
    numbersOfDataRate=[5,15,25,35,40]
    plt.figure(figsize=(16,9), dpi=100)
    ##为避免delay参数在不同数据流下数量不同，逐个读取csv文件并绘制CDF曲线
    for number in numbersOfDataRate:
        fileName = prefixFileName[codeOfCurve]+str(number)+'.csv'
        originalData=pd.read_csv(fileName,header=None)
        sample=originalData[0:1].values[0]
        sns.kdeplot(sample,cumulative=True,color=color[colorIndex],label=number,linewidth = '2')
        colorIndex+=1
##设置x轴的显示范围（根据需要是否选取）
#         axes = plt.gca()
#         axes.set_xlim([min(sample),max(sample)]) 
     
##单行数据快速绘图,使用集成的csv文件
#     codeOfCurve = 1 #0代表画时延CDF曲线，1代表丢包率CDF曲线
#     testRow=4 #选择要绘制曲线使用数据所在的行数，0代表5,1代表15,2代表25,3代表35,4代表40   
#     prefixFileName=['data/delay.csv','data/PacketLossRate.csv']
#     originalData=pd.read_csv(prefixFileName[codeOfCurve],header=None)
#     sample=originalData[testRow:testRow+1].values[0]
#     sns.kdeplot(sample,cumulative=True,color=color[testRow],label=testRow,linewidth = '2')
  
##出图相关设置   
    plt.title(title[codeOfCurve],fontsize=30)  
    plt.xlabel(xLabel[codeOfCurve],fontsize=30)     
    plt.ylabel('CDF',fontsize=30)
    pictureName=title[codeOfCurve]+'.png'
    plt.savefig(pictureName)   
    plt.show()    
if __name__=='__main__':
    main()  