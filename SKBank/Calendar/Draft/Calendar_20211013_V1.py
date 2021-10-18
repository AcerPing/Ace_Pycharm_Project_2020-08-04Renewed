import os
import pandas as pd
import time
import datetime


def calendar (FilePath, sheet_name, runmode=2, n=1):
    '''
    1. 當天是否為上班日
    2. 上一次上班日是什麼時候?
    '''
    DataFrame_Calendar = pd.read_excel(FilePath, sheet_name)
    # print(DataFrame_Calendar)
    # TODO: 1. 當天是否為上班日
    if runmode == 1 :
        today = time.strftime("%Y/%m/%d", time.localtime())
        DataFrame_Whether_Work = DataFrame_Calendar[DataFrame_Calendar['本期'] == today]
        if DataFrame_Whether_Work['上班'].iloc[0] != 1: 
            print('不用上班')
            Whether_Work = '不用上班'
        else: 
            print('Go to Work.')
            Whether_Work = 'Go to Work.'
        return Whether_Work, None
    # TODO: 2. 上一次上班日是什麼時候?
    elif runmode == 2 :
        DataFrame_PreviousWorkingDay = DataFrame_Calendar[DataFrame_Calendar['上班'] == 1]
        list_WorkingDay = list(DataFrame_PreviousWorkingDay['本期'])
        today = pd.Timestamp(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d'))
        if today not in list_WorkingDay: 
            Whether_Work = '不用上班'
            return Whether_Work, None
        Current_Index = list_WorkingDay.index(today)
        # print(int(Current_Index))
        PreviousWorkingDay = list_WorkingDay[Current_Index-n]
        PreviousWorkingDay = datetime.datetime.strptime(str(PreviousWorkingDay), "%d-%m-%Y") 
        print(str(PreviousWorkingDay))
        # Current_Index = DataFrame_PreviousWorkingDay[DataFrame_PreviousWorkingDay['本期'] == today].index
        Whether_Work = 'Go to Work.'
        return Whether_Work, PreviousWorkingDay
        


#主流程
if __name__ == "__main__":
    # 路徑設定
    File_Directory = r'D:\哲平\新光銀行\RPA\Calendar'
    File_Name = r'Calendar.xls'
    FilePath = os.path.join(File_Directory, File_Name)
    # print(FilePath)
    sheet_name='reorganize'
    calendar (FilePath=FilePath, sheet_name=sheet_name)


    

