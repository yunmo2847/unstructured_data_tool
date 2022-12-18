#%%
import csv
from pylab import *
# 폰트 설정 방법 1
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
file = input()
asd = int(input('파일 출처 입력(1번은 네이버 데이터랩,2번은 행정안전부,3번은 구글 트렌드'))

def naver(file):
    f = open(file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    first_csv = []
    second_csv = []
    data = []
    fig = ''
    title = ''
    for index,line in enumerate(rdr):
        if line == []:
            continue
        if index<=7:
            first_csv.append(line)
        else:
            second_csv.append(line)
    for i in range(1,len(second_csv[0])):
        zxcv = []
        for j in range(1,len(second_csv)):
            zxcv.append(int(second_csv[j][i]))
        data.append(zxcv)
    for i in range(1,len(second_csv[0])):
        title = title + second_csv[0][i]
        title = title + ','
    title = title.rstrip(",")
    title = title + ' 클릭량 추이'
    for i in range(2,len(first_csv)):
        fig = fig +" "+ first_csv[i][0] + " |"
    plt.title(title)
    for i in range(len(second_csv[0])-1):
        plt.plot(data[i] , label=second_csv[0][i+1])
    figtext(-.01, .01, fig)
    plt.legend()
    plt.show()
    f.close()

def hang(file):
    f = open(file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    csv1 = []
    csv2 = []
    data = []
    label = []
    title = []
    for index,i in enumerate(rdr):
        a = 0
        if index == 0:
            for l in i:
                if a<=7:
                    title.append(l)
        if index>1:
            csv2=[]
            a = 0
            for k in i:
                if a == 7:
                    a = 0
                if a == 0:
                    label.append(k)
                a+=1
            for j in i[1:]:
                if j.find(',') != -1:
                    j = int(j.replace(',', '')) 
                    csv2.append(j)
                else:
                    j = float(j)
                    csv2.append(j)
            csv1.append(csv2)
    for i in range(len(csv1)):
        data.append(csv1[i][0])
    plt.title(title[0+1])
    plt.pie(data,labels = label,autopct='%.1f%%')

def google(file):
    f = open(file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    header = next(rdr)
    header = next(rdr)
    title = '구글 관련 인기 검색어' + str(header)
    csv1 = []
    data = []
    label = []
    RISING_ = False
    for index,i in enumerate(rdr):
        if index>1:
            if i == []:
                continue
            if i == ['RISING']:
                RISING_ = True
            if RISING_ == False:
                csv1.append(i)
    for i in range(len(csv1)-1):
        data.append(csv1[i][1])
        label.append(csv1[i][0])
    plt.title(title)
    plt.pie(data,labels = label,autopct='%.1f%%')
    
if asd ==1:
    naver(file)
elif asd == 2:
    hang(file)
else:
    google(file)
# %%
