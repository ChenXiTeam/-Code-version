import numpy as np
#先使用文本进行测试
#标点符合去掉
excludes = {'，','。','/','《','》','？','；','‘','：','“','【','】','{','}',
            '、','|','！','@','#','￥','%','……','&','*','（','）','-','=',
            '——','+','·','~','”',
            ',','.','/','<','>','?',';','\'',':','"','[',']','{','}','\\','|',
            '~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=',
            ' ','\n'}

def getThetxt(str):
    d1 = open(str,encoding='utf-8').read()

    for word in excludes:
        d1 = d1.replace(word,'')
    # print(d1)
    return d1

def getSubstring(a,b):

    number = 0
    list_a = list(a)
    list_b = list(b)
    max_s = (max(len(a),len(b)))
    list2 = np.zeros((max_s,max_s))

    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i]==list_b[j] :
                if i<1 or j < 1:
                    list2[i][j] = 1
                else:
                    list2[i][j] = list2[i-1][j-1]+1

    max_number = 0
    for i in range(max_s):
        for j in range(max_s):
            if list2[i][j] > max_number:
                max_number = list2[i][j]

    return max_number

def getSimilar(A,B):

    a = int(getSubstring(A, B))

    similar = round( (2.0 * a ) / (len(A)+len(B)),2)
    return similar


#字符长度大于x计入
def getSubstring2(a,b,x):

    number = 0
    list_a = list(a)
    list_b = list(b)
    max_s = (max(len(a),len(b)))
    list2 = np.zeros((max_s,max_s))

    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i]==list_b[j] :
                if i<1 or j < 1:
                    list2[i][j] = 1
                else:
                    list2[i][j] = list2[i-1][j-1]+1

    # print(list2)

    sum_number = 0
    max_number = 0
    for i in range(max_s):
        for j in range(max_s):
            ii = i
            jj = j
            #斜方向向下找
            while ii+1 < max_s and jj+1 < max_s and list2[ii][jj] >= x:
                ii = ii + 1
                jj = jj + 1
                if list2[ii][jj] > list2[ii-1][jj-1]:
                    max_number = list2[ii][jj]
                    list2[ii][jj] = 0


            sum_number += max_number
            #列表清零
            while max_number != 0 and  list2[ii-1][jj-1] != 0:
                list2[ii-1][jj-1] = 0
                ii = ii - 1
                jj = jj - 1
            max_number = 0
    # print(list2)
    return sum_number

# 另一个计算方法，大于x以上的都计入，不仅仅取最大值
#设计一个分段的，
if __name__ == '__main__':
    txt1 = getThetxt("C:/Users/60917/Desktop/第一章.txt")
    txt2 = getThetxt("C:/Users/60917/Desktop/第二章.txt")
    print(getSubstring2(txt1,txt2,11))
    # print(getSimilar(txt1,txt2))
    # print(getSubstring2("a213pple","a1244pple",2))
