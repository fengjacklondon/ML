from numpy import  *


# a = array([0, 1, 2])
# demo_a1 = tile(a, 2)
# demo_a2 = tile(a, (2, 2))
# demo_a3 = tile(a, (3, 2, 2))
#
# [
#     [[0 1 2 0 1 2],[0 1 2 0 1 2]]
#     [[0 1 2 0 1 2],[0 1 2 0 1 2]]
#     [[0 1 2 0 1 2],[0 1 2 0 1 2]]
#
#
#
# ]
#
# demo_a4 = tile(a, (2, 2, 1))



# print(demo_a1)
#
# print("**************")
# print(demo_a2)
#
# print("**************")
# print(demo_a3)
#
# print("**************")
# print(demo_a4)
#
# b = array([[1, 2], [3, 4]])
#
# demo_b = tile(b, 2)
#
# demo_b1 = tile(b, (2, 1))
#
#
#
# print("**************")
# print(demo_b)
#
#
# print("**************")
# print(demo_b1)
#
#
#
# c = array([1,2,3,4])
# demo_c = tile(c,(4,1))
#
#
# print("**************")
# print(demo_c)
#
# print("[[[1 2 3 4 1 2 3 4] [1 2 3 4 1 2 3 4]] [[1 2 3 4 1 2 3 4] [1 2 3 4 1 2 3 4]]]")
#

# classCount = {}
# classCount['a'] = 1
# classCount['b'] = 2
#
# print(classCount.get('cc',1))
#
# testList = [];
# testList.append(1);
# testList.append(2);
# print(testList)

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
# print(group.shape[3]);


array = [[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]
print(sum(array, axis=1))
