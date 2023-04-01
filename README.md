# dataNumpy
빅데이터 수업 

week 4 : ndim이 1이냐 2냐에 따라서 fill_value가 제대로 안 돌아갈 수도 있음. (주로 1에서)
add는 한쪽만 존재해도 계산이 되는데, sub는 한쪽만 없어도 NaN이 나옴
axis = 0는 row operation // axis = 1 column operation 

floordiv == // 
rdiv == / 

iloc := index location Ex) df1.iloc[ [1,3,4], [4,5]], df1.iloc[ [1:], 3], df1.iloc[ :, 0] 


loc := name location  EX) df2.loc['one':'three', ['year', 'points']], df2.loc[:, 'year'], df2.loc['one':'three', 'year':'points']

df.drop does not delete the original data
