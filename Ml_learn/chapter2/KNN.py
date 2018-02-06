from numpy import *
import operator

def createDataSet ():
    group = array ([[1.0, 1.1],[1.0,1.0], [0, 0], [0, 0.1]])
    lables = ['A','A','B','B']
    return group, lables


# 预测分类
def classify0 (inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

    # group = array([
    #                 [
    #                      [1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]
    #                 ],
    #                [
    #                    [1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]
    #                ],
    #                [
    #                    [1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]
    #                ]
    #                ])
    #
    # print(group.shape[0]);
    # print(group.shape[1]);
    # print(group.shape[2]);
    #
    # result  3,4,2
    # 从外向内计算每个维度的 长度

    diffMat = tile(inX, (dataSetSize, 1)) - dataSet

    #[0, 0] -> [[0,0][0,0][0,0][0,0]]
    #[[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]


    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        # sortedDistIndicies
        #[1,48 ,1.4, 0, 1]
        # [2,3,1,0]
        #  sortedDistIndicies[0]->labels[2]->B
        #  sortedDistIndicies[1]->labels[3]->B
        #  sortedDistIndicies[2]->labels[1]->A

        #voteIlabel = B
        # voteIlabel = B
        # voteIlabel = A



        #为什么 [1,1]->A  [0,1]->B
        # lables = ['A','A','B','B']
        voteIlabel = labels[sortedDistIndicies[i]]

        # classCount[B]->1
        # classCount[B]->2
        # classCount[A]->1

        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    #前K个值出现类别最高的频率
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=False)
    return sortedClassCount[0][0]


#print(classify0([0, 0], createDataSet()[0], createDataSet()[1], 3))


def  createDataSet_fxh() :
    group = ([[0, 0], [0, 0], [0, 0], [0, 0]])
    labels = ['A', 'A', 'B', 'B']

    return group, labels


def classify0_fxh(inX, dataSet , labels, k):
    dataSetSize = dataSet.shape[0];
    #构造一个可以和 多个点 做 差的 列表
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    sortedDistance = distance.argsort();
    classCount = {}

    #确定前K个距离最小的元素所在的主要分类
    for i in range(k):
        #
        voteLabel = labels[distance[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=False)
    return sortedClassCount[0][0]




def file2matrix (filename):
    fr = open(filename)
    arrayOLines = fr.readlines();
    numberOfLines = len(arrayOLines)
    returnMaT = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMaT[index, :] = listFromLine[0:3]
        classLabelVector.append(str(listFromLine[-1]))
        index += 1
    return returnMaT, classLabelVector








