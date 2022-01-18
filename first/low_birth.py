import pandas as pd

age = pd.read_csv('전국 시군구,연령,연도별 출산율(17~20년).csv', sep=',', encoding='cp949')
age = age[age['시군구별']=='전국']
age.loc[age['항목']=='모의 연령별출산율:15-19세', '항목']='15-19세'
age = age.drop([0])
age.drop(columns = '시군구별', inplace = True)
age.set_index('항목', inplace=True)
age

import matplotlib.pyplot as plt
plt.plot(age)
plt.rcParams['figure.figsize'] = (15, 8)
plt.title('2017~2020년 모의 연령대별 출산율')
plt.legend(['2017년','2018년','2019년','2020년'])
plt.savefig('age.png')



number = pd.read_csv('전국 성, 30-39세 주민등록연앙인구(93~20년).csv', sep=',', encoding='cp949')
number = number[number['성별']=='여자']
number.drop(columns = '행정구역(시군구)별', inplace = True)
number.drop(columns = '성별', inplace = True)
number.set_index('연령별', inplace=True)
number.loc['30대 합계'] = number.sum()
number

plt.rcParams['figure.figsize'] = (15, 8)
plt.plot(number.loc['30대 합계'])
plt.legend(['30대 합계'])
plt.title('주 출산 연령대 여성의 감소')
plt.text(x = 10, y = 4362617.5 + 10000, s ='4,360,000', color = 'r')
plt.text(x = 26, y = 3359589.5 - 20000, s = '3,360,000', color = 'r')
plt.text(x = (10+26)/2 +4, y = (4362617.5+3359589.5)/2, s = '대략 100만명 감소')
plt.text(x = (10+26)/2 +4, y = (4362617.5+3359589.5)/2 +30000, s = '16년 만에')
plt.savefig('number.png')



corona = pd.read_excel('전국 월별 출생아수,혼인건수(17~21년).xlsx')
corona.drop(columns = '행정구역별(1)', inplace = True)
corona['시점'] = corona['시점'].str.replace(' p','')
corona.tail()

from pandas.api.types import is_string_dtype
for col in corona.columns:
        if is_string_dtype(corona[col]):
            corona[col] = corona[col].str.replace('[^A-Za-z0-9-\s]+', '')
corona.tail()

corona['시점'] = corona['시점'].str.replace(' ','-')
corona['시점'] = pd.to_datetime(corona['시점'])
corona['연'] = corona['시점'].dt.year 
corona['월'] = corona['시점'].dt.month 
corona['혼인 감소율'] = corona['혼인건수(건)'].pct_change(periods=6)
corona

import numpy
label = ['1월','2월','3월','4월','5월','6월']
plt.figure()
plt.rcParams['figure.figsize'] = (20, 8)
x = numpy.arange(len(label))
plt.bar(x-0.2, corona[corona['연']==2017]['출생아수(명)'], label='2017년', width=0.1, color='grey', edgecolor="black")
plt.bar(x-0.1, corona[corona['연']==2018]['출생아수(명)'], label='2018년', width=0.1, color='grey', edgecolor="black")
plt.bar(x+0.0, corona[corona['연']==2019]['출생아수(명)'], label='2019년', width=0.1, color='grey', edgecolor="black")
plt.bar(x+0.1, corona[corona['연']==2020]['출생아수(명)'], label='2020년', width=0.1, color='green', edgecolor="black")
plt.bar(x+0.2, corona[corona['연']==2021]['출생아수(명)'], label='2021년', width=0.1, color='yellow', edgecolor="black")
plt.xticks(x, label)
plt.legend()
plt.xlabel('월')
plt.ylabel('출생아수')
plt.title('2017~2021년 상반기 월별 출생아수')
plt.savefig('birth.png')
plt.show()



label = ['1월','2월','3월','4월','5월','6월']
plt.figure()
plt.rcParams['figure.figsize'] = (13, 8)
x = numpy.arange(len(label))
plt.bar(x-0.2, corona[corona['연']==2017]['혼인건수(건)'], label='2017년', width=0.1, color='grey', edgecolor="black")
plt.bar(x-0.1, corona[corona['연']==2018]['혼인건수(건)'], label='2018년', width=0.1, color='grey', edgecolor="black")
plt.bar(x+0.0, corona[corona['연']==2019]['혼인건수(건)'], label='2019년', width=0.1, color='grey', edgecolor="black")
plt.bar(x+0.1, corona[corona['연']==2020]['혼인건수(건)'], label='2020년', width=0.1, color='green', edgecolor="black")
plt.bar(x+0.2, corona[corona['연']==2021]['혼인건수(건)'], label='2021년', width=0.1, color='yellow', edgecolor="black")
plt.xticks(x, label)
plt.legend()
plt.xlabel('월')
plt.ylabel('혼인건수')
plt.title('2020/2021년 월별 혼인건수')
plt.text(x = 0+0.2, y = 18000, s = '-0.18% (3539건)')
plt.text(x = 1+0.2, y = 17000, s = '-0.22% (4130건)')
plt.text(x = 2+0.2, y = 18000, s = '-0.13% (2595건)')
plt.text(x = 3+0.1, y = 17000, s = '-0.22% (4357건)')
plt.text(x = 4+0.1, y = 19000, s = '-0.21% (4901건)', color = 'r')
plt.savefig('marriage.png')
plt.show()



cause = pd.read_csv('연령,사유,연도별 경력단절여성(17~20년).csv', sep=',', encoding='cp949')
cause = cause[cause['사유별'] != '경력단절여성']
cause

categories = ['결혼','임신/출산','육아','자녀교육','가족돌봄']
explode = [0, 0.10, 0, 0, 0]
plt.pie(cause[cause['연령대별']=='계']['2020'], labels=categories, autopct='%0.1f%%', explode = explode)
plt.title('여성의 경력단절 사유')
plt.savefig('cause.png')
plt.show()



sex = pd.read_csv('성,연령별 경제활동인구(10,20년).csv', sep=',', encoding='cp949')
sex = sex.drop([0, 1, 2, 4, 7, 10, 13])
sex.set_index('연령계층별', inplace=True)
sex = sex.apply(pd.to_numeric)
sex

sex_g = plt.plot(sex)
plt.legend(['2010년 남자','2010년 여자','2020년 남자','2020년 여자'])
plt.xlabel('연령대')
plt.title('성/연령대별 경제활동 참가율')
plt.text(x = 4, y = 40, s = '남녀격차 최대 31.7%p', color = 'r', fontsize = 12)
plt.text(x = 4.3, y = 36.5, s = '(35-39세)', color = 'r', fontsize = 12)
plt.savefig('sex.png')



marriage = pd.read_csv('결혼에 대한 견해.csv', sep=',', encoding='cp949')
marriage.drop(columns = '행정구역별(1)', inplace = True)
marriage.drop(columns = '특성별(1)', inplace = True)
marriage.drop(columns = '특성별(2)', inplace = True)
marriage.set_index('항목', inplace=True)
marriage = marriage.transpose()
marriage

marriage.plot(kind = 'barh', stacked=True, figsize=(10,8))
plt.legend(loc = 'best')
plt.savefig('view.png')
plt.show()



fertility = pd.read_excel('SF_2_1_Fertility_rates.xlsx')
fertility = fertility[['Unnamed: 11', 'Unnamed: 15']]
fertility = fertility.drop([0,1,2])
fertility.columns = ['국가명','2019년']
fertility = fertility.loc[[3,47,37,32,27,25,22,20,56,55,11,39,35]]
fertility.sort_values(by=['2019년'], axis=0, inplace = True)
fertility.set_index('국가명', inplace=True)
fertility

label = fertility.index
plt.figure()
plt.rcParams['figure.figsize'] = (11, 8)
x = numpy.arange(len(label))
plt.bar(x, fertility['2019년'], label='2019년')
plt.xticks(x, label, rotation = 20)
plt.legend()
plt.title('2019년 국가별 출생율')
plt.savefig('fertility.png')
plt.show()



outside = pd.read_excel('SF_2_4_Share_births_outside_marriage.xlsx')
outside = outside[['Unnamed: 11', 'Unnamed: 12']]
outside = outside.drop([0,1,2])
outside.columns = ['국가명','2018년']
outside = outside.loc[[46,7,12,18,25,15,33,23,43,45,27,35]]
outside.sort_values(by=['2018년'], axis=0, inplace = True)
outside.set_index('국가명', inplace=True)
outside

label = outside.index
plt.figure()
plt.rcParams['figure.figsize'] = (11, 8)
x = numpy.arange(len(label))
plt.bar(x, outside['2018년'], label='2018년')
plt.xticks(x, label, rotation = 20)
plt.legend()
plt.title('2018년 국가별 혼외출생율')
plt.text(x = 3.5, y = 35, s ='생활동반자법')
plt.text(x = 7.5, y = 49, s ='Civil partership')
plt.text(x = 8.5, y = 53, s ='생활동반자법')
plt.text(x = 9.8, y = 55.5, s ='동거법')
plt.text(x = 10.8, y = 61, s ='Pacs')
plt.savefig('outside.png')
plt.show()
