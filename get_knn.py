from html import entities
import random
from numpy import sort
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'      # 使用 GPU 0


entitys = []
with open('entity2vec100_2 copy.init','r')as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(' ')
        entitys.append(line)
relations = []
with open('relation2vec100_2 copy.init','r')as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(' ')
        relations.append(line)



#knn
#距离--欧氏距离
def distance(d1,d2,r):
    res = 0
    for key in range(1,101):
        res = res + float(entitys[d1][key]) + float(relations[r][key]) - float(entitys[d2][key])
    res = abs(res)
    res = round(res,5)
    res = res ** 0.5
    res = float(res)

    return res


K = 31

def knn(x):
    
    #1.计算所有距离
    res = []
    for relation in relations:
        for entity in entitys:
            res.append(
                {'name':entity[0],'distance':distance(int(x[0]),int(entity[0]),int(relation[0]))}  )
   
    #2.排序--升序
    res = sorted(res,key = lambda item:item['distance'])
    #print(res)
    #3.取前k个
    res2 = res[0:K]
    return res2

#res = knn(entitys[0])
#print(res)
#'''
for i in range(706,800):
    res = knn(entitys[i])
    with open('aaa.txt','a')as f1:
        for i in range(len(res)):
            for j in res[i].values():
                #print(j)
                f1.write(str(j))
                f1.write(' ')
        f1.write('\n')
#'''