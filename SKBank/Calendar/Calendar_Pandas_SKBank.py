import os, sys
import pandas as pd
import time
import datetime
import re

# 字串轉換為時間
def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)

def check_result():
    '''
    檢查寫入的結果檔是否是否符合格式
    '''
    Custom_Err_Msg = ''

    # TODO: 讀取 今天是否上班 檔案
    with open("今天是否上班.txt",mode="r",encoding="utf-8") as file: datum=file.read()
    # print(datum)
    o = re.fullmatch("^[0-9]{1}\n$", datum)
    # print(o)
    if o != None: print('True')
    else:
        Custom_Err_Msg += '今天是否上班 結果報表錯誤'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('結果報表 Error', Custom_Err_Msg)

    # TODO: 讀取 上一個營業日 檔案
    with open("上一個營業日.txt",mode="r",encoding="utf-8") as file: datum=file.read()
    # print(datum)
    o = re.fullmatch("^[0-9]{4}.[0-9]{2}.[0-9]{2}\n$", datum)
    # print(o)
    if o != None: print('True')
    else:
        Custom_Err_Msg += '上一個營業日 結果報表錯誤'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('結果報表 Error', Custom_Err_Msg)
    
    # TODO: 讀取 下一個營業日 檔案
    with open("下一個營業日.txt",mode="r",encoding="utf-8") as file: datum=file.read()
    # print(datum)
    o = re.fullmatch("^[0-9]{4}/[0-9]{2}/[0-9]{2}\n$", datum)
    # print(o)
    if o != None: print('True')
    else:
        Custom_Err_Msg += '下一個營業日 結果報表錯誤'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('結果報表 Error', Custom_Err_Msg)


def calendar_pandas (FilePath, sheet_name, n=1):
    '''
    1. 當天是否為上班日
    2. 上一次上班日是什麼時候?
    '''
    Custom_Err_Msg = ''
    DataFrame_Calendar = pd.read_excel(FilePath, sheet_name) # 讀取工作日Excel報表
    # print(DataFrame_Calendar)

    today = time.strftime("%Y/%m/%d", time.localtime())
    # today = pd.Timestamp(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')) # 若格式為時間，改用Timestamp

    # TODO: 1. 當天是否為上班日
    DataFrame_Whether_Work = DataFrame_Calendar[DataFrame_Calendar['本日'] == today]

    #TODO: 檢查報表是否有今天日期 -> 是否有成功更新
    if DataFrame_Whether_Work.empty:
        Custom_Err_Msg += '今天日期沒有在Excel Report'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error', Custom_Err_Msg)
    
    elif len(DataFrame_Whether_Work) >= 2: 
        Custom_Err_Msg += '今天日期在Excel Report中出現2次以上.'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error', Custom_Err_Msg)

    if DataFrame_Whether_Work['營業'].iloc[0] != 1: print('不用上班')
    else: print('Go to Work.')

    Whether_Work = DataFrame_Whether_Work['營業'].iloc[0]
    file=open("今天是否上班.txt",mode="w",encoding="utf-8") #開啟檔案
    file.write(str(Whether_Work).strip()+"\n") #撰寫檔案
    file.close() #關閉檔案
    
    # TODO: 2. 上一次上班日是什麼時候?
    DataFrame_PreviousWorkingDay = DataFrame_Calendar[DataFrame_Calendar['營業'] == 1] # 篩選出只有營業的日期
    list_WorkingDay = list(DataFrame_PreviousWorkingDay['本日']) # 取出所有營業的日期
    
    #若今天日期不再營業日期list中 
    if today not in list_WorkingDay: 
        # 字串轉換為時間
        for i in range(0, len(list_WorkingDay)):
            list_WorkingDay[i] = strTodatetime(list_WorkingDay[i],"%Y/%m/%d")  
        # 比較時間大小 -> 插入
        today_strTodatetime = strTodatetime(today,"%Y/%m/%d")
        for i in range(0, len(list_WorkingDay)):
            if today_strTodatetime < list_WorkingDay[i]:
                list_WorkingDay.insert(i, today_strTodatetime)
                break
        else:
            list_WorkingDay.append(today_strTodatetime) #EX. 2021/12/31
        # 時間轉換為字串
        for i in range(0, len(list_WorkingDay)):
            list_WorkingDay[i] = datetime.datetime.strftime(list_WorkingDay[i], '%Y/%m/%d')
    
    Current_Index = list_WorkingDay.index(today)
    # Current_Index = DataFrame_PreviousWorkingDay[DataFrame_PreviousWorkingDay['本期'] == today].index
    # print(int(Current_Index))
    # print(list_WorkingDay)
    
    #TODO: 取出前n次的營業日期
    if Current_Index == 0:
        Custom_Err_Msg += '沒有上一個營業日'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error', Custom_Err_Msg)
    PreviousWorkingDay = list_WorkingDay[Current_Index-n]
    file=open("上一個營業日.txt",mode="w",encoding="utf-8") #開啟檔案
    file.write(str(PreviousWorkingDay).strip()+"\n") #撰寫檔案
    file.close() #關閉檔案
    
    #TODO: # 取出後n次的營業日期
    if Current_Index == len(list_WorkingDay)-1:
        Custom_Err_Msg += '沒有下一個營業日'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error', Custom_Err_Msg)
    NextWorkingDay = list_WorkingDay[Current_Index+n] 
    file=open("下一個營業日.txt",mode="w",encoding="utf-8") #開啟檔案
    file.write(str(NextWorkingDay).strip()+"\n") #撰寫檔案
    file.close() #關閉檔案


#主流程
if __name__ == "__main__":
    try:
        # 參數設定
        Custom_Err_Msg = ''
        # 路徑設定
        File_Directory = os.getcwd()
        File_Name = r'工作日查詢.xls'
        FilePath = os.path.join(File_Directory, File_Name)
        # print(FilePath)
        sheet_name='reorganize'

        #檢查檔案路徑是否存在
        if not os.path.isfile(FilePath): #檔案不存在
            PrintText = 'File is not existed. Please check the path of the file.'
            print(PrintText)
            Custom_Err_Msg += PrintText
            print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
            raise Exception ('File Not Existed Error', Custom_Err_Msg)
        
        calendar_pandas (FilePath=FilePath, sheet_name=sheet_name)

    except:
        error_message = sys.exc_info() #取得Call Stack
        print(error_message)
        with open("Error_Log.txt",mode="w",encoding="utf-8") as file:
            file.write(str(error_message).strip()+'\n')
        input('Please "Key Enter" to continue the process.')
        sys.exit(1)
    
    try:
        check_result()
    except:
        error_message = sys.exc_info() #取得Call Stack
        print(error_message)
        with open("Error_Log.txt",mode="w",encoding="utf-8") as file:
            file.write(str(error_message).strip()+'\n')
        input('Please "Key Enter" to continue the process.')
        sys.exit(1)
    



    

