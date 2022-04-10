import pandas as pd

class Class_1():###디폴트 값 만들어주기
    def __init__C(self,r):
        self.url=r

    def csv_read(self,input_sort="Country",input_inplace=True):#변수 더 받아서하기
        self.read=pd.read_csv(self.url)
        self.read.sort_values(input_sort,inplace=input_inplace)
        self.read.reset_index(drop =True ,inplace=input_inplace)
        return self.read
    
    def make__(self,input_list = []):
        self.read.drop(input_list,axis=1,inplace=True)
        
        return self.read
    
    def remove_2(self, input_s_column, input_e_column):
        self.read.drop(self.read.loc[:, input_s_column: input_e_column], axis=1)
        return self.read