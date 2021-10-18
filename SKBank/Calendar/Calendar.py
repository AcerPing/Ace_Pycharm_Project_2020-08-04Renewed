import os
import pandas as pd
import time
import datetime


def calendar (FilePath, sheet_name, runmode=2, n=1):
    '''
    1. 當天是否為上班日
    2. 上一次上班日是什麼時候?
    '''
    DataFrame_Calendar = pd.read_excel(FilePath, sheet_name) # 讀取工作日Excel報表
    # print(DataFrame_Calendar)

    # TODO: 1. 當天是否為上班日
    if runmode == 1 :
        today = time.strftime("%Y/%m/%d", time.localtime())
        DataFrame_Whether_Work = DataFrame_Calendar[DataFrame_Calendar['本日'] == today]
        if DataFrame_Whether_Work['營業'].iloc[0] != 1: 
            print('不用上班')
            Whether_Work = '不用上班'
        else: 
            print('Go to Work.')
            Whether_Work = 'Go to Work.'
        return Whether_Work, None
    
    # TODO: 2. 上一次上班日是什麼時候?
    elif runmode == 2 or runmode == 3 :
        DataFrame_PreviousWorkingDay = DataFrame_Calendar[DataFrame_Calendar['營業'] == 1] # 篩選出只有營業的日期
        list_WorkingDay = list(DataFrame_PreviousWorkingDay['本日']) # 取出所有營業的日期
        # today = pd.Timestamp(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')) # 若格式為時間，改用Timestamp
        today = time.strftime("%Y/%m/%d", time.localtime())
        # print(list_WorkingDay)
        if today not in list_WorkingDay: #若今天日期不再營業日期list中 
            Whether_Work = '不用上班'
            return Whether_Work, None
        Current_Index = list_WorkingDay.index(today)
        # Current_Index = DataFrame_PreviousWorkingDay[DataFrame_PreviousWorkingDay['本期'] == today].index
        # print(int(Current_Index))
        if runmode == 2 :
            PreviousWorkingDay = list_WorkingDay[Current_Index-n] # 取出前n次的營業日期
            Whether_Work = 'Go to Work.'
            return Whether_Work, PreviousWorkingDay
        elif runmode == 3 :
            NextWorkingDay = list_WorkingDay[Current_Index+n] # 取出前n次的營業日期
            Whether_Work = 'Go to Work.'
            return Whether_Work, NextWorkingDay


#主流程
if __name__ == "__main__":
    # 參數設定
    runmode = ''
    while runmode == '' or (len(runmode) != 1 and (runmode != '1' and runmode != '2' and runmode != '3')): 
        runmode = input('請輸入執行模式，\n1為查詢當天是否為工作日，2為查詢前一個工作日，3為查詢後一個工作日，\n輸入模式：')
    print('執行模式: ' + str(runmode))
    runmode = int(runmode) # 將runmode轉換為數字型式，後續傳如def
    # 路徑設定
    File_Directory = r'D:\哲平\新光銀行\RPA\Calendar'
    File_Name = r'工作日查詢.xls'
    FilePath = os.path.join(File_Directory, File_Name)
    # print(FilePath)
    sheet_name='reorganize'
    Whether_Work, InquiryWorkingDay = calendar (FilePath=FilePath, sheet_name=sheet_name, runmode=runmode)
    print(Whether_Work, InquiryWorkingDay)



    

