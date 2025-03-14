import pandas as pd

a = pd.Series([20, 15, 30, 25, 35], name='age')
b = pd.Series([68.5, 60.3, 53.4, 74.1, 80.7], name='weight')
c = pd.Series([180, 165, 155, 178, 185], name ='height')

## 1. human DataFrame 만들기
human = pd.DataFrame({'age':a,'weight':b,'height':c})
print(human.T,'\n')

def main():
    ### 2. loc(), iloc() 함수를 이용하여 `age`를 추출
    print(human.loc[:,'age'].T,'\n')
    print(human.iloc[:, 0].T,'\n')
    
    ### 3. loc(), iloc() 함수를 이용하여 `weight`와 `height`만 추출
    print(human.loc[:,['weight','height']].T,'\n')
    print(human.iloc[:, 1:3].T,'\n')
     
    sex = ['F','M','F','M','F']
    ### 4.새로운 데이터 `sex`를 `human`에 추가
    human['sex'] = sex
    print(human.T,'\n')
    
    ### 5. `human`에서 `height`를 삭제
    tmp = human.drop(columns=['height'])
    print(tmp.T, '\n')


if __name__ == "__main__":
    main()