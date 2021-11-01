import os
import sys
import time
import traceback
import xlrd

# import datetime

#Custom Function Defination
def ErrorMessenger(e, fileName='', lineNum=0, funcName='', Custom_Err_Msg=''):
    '''
    發生錯誤時，處理錯誤的函式
    '''
    error_class = e.__class__.__name__ #取得錯誤類型
    detail = e.args[0] #取得詳細內容
    if fileName == '' and funcName == '':
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_stack(tb)[-1] #取得Call Stack的最後一筆資料
        fileName = lastCallStack[0] #取得發生的檔案名稱
        lineNum = lastCallStack[1] #取得發生的行號
        funcName =  lastCallStack[2] #取得發生的函數名稱
    if Custom_Err_Msg != "":
        errMsg = Custom_Err_Msg
    else:
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    return errMsg

#數字轉換
def ConvertNum(s):
    '''
    讀取Excel時，數字會自動轉為小數，利用此函式再轉換為整數
    '''
    try:
        s = str(float(str(s).strip().replace(',', '')))
        if s.count('.') == 0:
            s = s.replace('.0', '')
            return int(s)
        if s.count('.') == 1:
            sl = s.split('.')
            left = sl[0]
            right = sl[1]
            if int(right) == 0:
                return int(left)
            else:
                return float(s)
        else: raise Exception
    except:
        return s

def ExcelRead(filename, TargetSheetName, key_column):
    '''
    讀取Excel表格
    '''
    ModuleObj = {'Status':'fail',
                 'Custom_Err_Msg': '',
                 'SourceExcelList': [],
                 'key_column': [],
                 'key_column_id': [],
                 'max_row': '',
                 'max_col' : '',
                 'WB':[],
                 'WS':[],
                 'Error': {'e_detail': '', 'e_fileName': '', 'e_lineNum': '', 'e_funcName': ''}}
    try:
        SourceExcelList = []
        #Read Xlrd
        print('Loading Excel:')
        print(filename)
        wb = xlrd.open_workbook(filename)
        print('Worksheets loaded')
        print(wb.sheet_names())        
        
        #表名搜尋
        sheet_names = wb.sheet_names()
        SheetFound = False
        SheetCount = 0
        SheetNo = 0
        for sheet in wb.sheet_names():
            if sheet == TargetSheetName:
                SheetFound = True
                SheetNo = SheetCount
            SheetCount = SheetCount +1
        if SheetFound == False:
            ModuleObj = {'Custom_Err_Msg': 'Cannot find sheet name 「' + TargetSheetName + '」.'}
            del wb, ws
            return ModuleObj 
        print('Sheet 「' + TargetSheetName + '」 Found:', SheetFound, SheetCount, SheetNo)
        ws = wb.sheet_by_name(sheet_names[SheetNo])
        print('Columns: [%s] Rows: [%s]' % (ws.ncols, ws.nrows))
        MaxRow = ws.nrows
        MaxCol = ws.ncols
        
        key_column_id = {}
        for item in key_column:
            key_column_id[item] = ''
        
        #欄位比對
        MaxCheck = len(key_column)
        KeyColCount = 0
        ColCount = 0
        for i in range(0, MaxCheck):
            for item in key_column:
                if ws.cell(0, i).value.strip() == key_column[item]:
                    key_column_id[item] = ColCount
                    KeyColCount = KeyColCount + 1
                    print(key_column_id[item], item)
            ColCount = ColCount + 1
        print(KeyColCount, MaxCheck)
        if KeyColCount < MaxCheck:
            MissedCol = ''
            for item in key_column_id:
                MissedCol = MissedCol + '「 ' + item + '」'
            print('Excel File missing columns as below, please check.\n' + MissedCol)
            ModuleObj = {'Custom_Err_Msg': 'Excel File missing columns as below, please check.\n' + MissedCol}
            del wb, ws
            return ModuleObj
        
        # print(key_column)
        # print(KeyColCount, MaxCheck)
        # print(key_column_id)
        
        # 讀取表資料內容
        for i in range(1, MaxRow):
            CrntRow = ws.row_values(i)
            SourceExcelList.append(CrntRow)
        print('Sheet 「' + TargetSheetName + '」 Loaded. ColumnCount: ', MaxCol, ' RowCount: ', MaxRow, ' DataCapture: ', len(SourceExcelList))
        ModuleObj['Status'] = 'success'
        ModuleObj['SourceExcelList'] = SourceExcelList
        ModuleObj['key_column'] = key_column
        ModuleObj['key_column_id'] = key_column_id
        ModuleObj['max_row'] = MaxRow
        ModuleObj['max_col'] = MaxCol
        ModuleObj['WB'] = wb
        ModuleObj['WS'] = ws
        # ModuleObj = {'Status':'success', 'SourceExcelList': SourceExcelList, 'key_column': key_column, 'key_column_id': key_column_id}
        del wb, ws
        return ModuleObj
    except Exception as e:
        ModuleObj['Error'] = e
        ModuleObj['Error']['e_class'] = e.__class__.__name__ #取得錯誤類型
        ModuleObj['Error']['e_detail'] = e.args[0] #取得詳細內容
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_stack(tb)[-1] #取得Call Stack的最後一筆資料
        ModuleObj['Error']['e_fileName'] = lastCallStack[0] #取得發生的檔案名稱
        ModuleObj['Error']['e_lineNum'] = lastCallStack[1] #取得發生的行號
        ModuleObj['Error']['e_funcName'] = lastCallStack[2] #取得發生的函數名稱
        return ModuleObj

# 主函式
def main(runmode = '2'):
    '''
    1. 當天是否為上班日
    2. 上一次上班日是什麼時候?
    3. 下一次上班日是什麼時候?
    '''
    # 參數設定
    # TODO: 使用者輸入執行模式
    # runmode = ''
    # runmode = '1'
    while runmode == '' or (len(runmode) != 1 and (runmode != '1' and runmode != '2' and runmode != '3')): 
        runmode = input('請輸入執行模式，\n1為查詢當天是否為工作日，2為查詢前一個工作日，3為查詢後一個工作日，\n輸入模式：')
    print('執行模式: ' + str(runmode))
    runmode = int(runmode) # 將runmode轉換為數字型式，後續傳如def
    # TODO: 設定讀取檔案的位置及表單資訊
    File_Directory = r'D:\何哲平\RPA\工作日查詢' #D:\何哲平\RPA\工作日查詢
    File_Name = r'工作日查詢.xls'
    FilePath = os.path.join(File_Directory, File_Name)
    SourceFilePath_Excel = FilePath
    SourceFilePath_Excel = SourceFilePath_Excel.replace('\u202a','')
    #檢查檔案路徑是否存在
    if os.path.exists(SourceFilePath_Excel) == False: #檔案不存在
        PrintText = 'File is not existed. Please check the path of the file.'
        print(PrintText)
        Custom_Err_Msg = PrintText
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception ('File Not Existed Error')
    
    SourceFile_ExcelSheet = 'reorganize'
    KeyColumn =  {'本日':'本日',
                '星期':'星期',
                '營業':'營業',}

    #Read Excel
    Excel_todo_list = []
    ModuleObj = ExcelRead(SourceFilePath_Excel, SourceFile_ExcelSheet, KeyColumn)
    print(ModuleObj)
    if ModuleObj['Status'] == 'success':
        print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
    else:
        print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
        print('Excel Error')
        raise Exception('Excel Error')
    Excel_todo_list = ModuleObj['SourceExcelList']
    key_column = ModuleObj['key_column']
    key_column_id = ModuleObj['key_column_id']
    WB = ModuleObj['WB']
    WS = ModuleObj['WS']
    MaxRow = ModuleObj['max_row']
    MaxCol = ModuleObj['max_col']
    if len(Excel_todo_list) == 0:
        Custom_Err_Msg = 'No Data found in Excel. Pleaser Check Your Report.'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error')

    today = time.strftime("%Y/%m/%d", time.localtime()) # 今天日期

    # print(Excel_todo_list[0]) # 與Excel檔案列號差2
    # print (i + 2) 
    # print(Excel_todo_list[i]) 
    # print(ConvertNum(Excel_todo_list[i][key_column_id['營業']])) 
    CrntRow = 0
    for i in range(0, len(Excel_todo_list)):
        CrntRow = i + 1
        # 
        if Excel_todo_list[i][key_column_id['本日']] == today: break #抓取今日日期的index
    else: 
        Custom_Err_Msg = '今天日期沒有在Excel Report'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error')
    
    if ConvertNum(Excel_todo_list[i][key_column_id['營業']]) != 1: 
        print('不用上班')
        Whether_Work = '不用上班'
    else: 
        print('Go to Work.')
        Whether_Work = 'Go to Work.'

    # TODO: 1. 當天是否為上班日
    if runmode == 1 : return Whether_Work, None
    
    # TODO: 2. 上一次上班日是什麼時候?
    elif runmode == 2 :
        for ii in range(i-1, 0, -1):
            if ConvertNum(Excel_todo_list[ii][key_column_id['營業']]) ==  1 : 
                PreviousWorkingDay = Excel_todo_list[ii][key_column_id['本日']]
                break
        else: 
            Custom_Err_Msg = '沒有上一個營業日'
            print('Excel Error')
            print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
            raise Exception('Excel Error')
        return Whether_Work, PreviousWorkingDay
    
    # TODO: 3. 下一次上班日是什麼時候?
    elif runmode == 3 :
        # print(Excel_todo_list[len(Excel_todo_list)-1]) # 若用len(Excel_todo_list)會發生out of range 的錯誤
        # print(len(Excel_todo_list))
        for ii in range(i+1, len(Excel_todo_list)-1):
            if ConvertNum(Excel_todo_list[ii][key_column_id['營業']]) ==  1 : 
                NextWorkingDay = Excel_todo_list[ii][key_column_id['本日']]
                break
        else: 
            Custom_Err_Msg = '沒有下一個營業日'
            print('Excel Error')
            print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
            raise Exception('Excel Error')
        return Whether_Work, NextWorkingDay
        
if __name__ == "__main__":
    Whether_Work, InquiryWorkingDay = main()
    print(Whether_Work, InquiryWorkingDay)
    time.sleep(10)
    input('Key Enter')
    raise Exception ('Stop')
    






# import pandas as pd
# def calendar (FilePath, sheet_name, runmode=2, n=1):
#     '''
#     1. 當天是否為上班日
#     2. 上一次上班日是什麼時候?
#     '''
#     DataFrame_Calendar = pd.read_excel(FilePath, sheet_name) # 讀取工作日Excel報表
#     # print(DataFrame_Calendar)

#     # TODO: 1. 當天是否為上班日
#     if runmode == 1 :
#         today = time.strftime("%Y/%m/%d", time.localtime())
#         DataFrame_Whether_Work = DataFrame_Calendar[DataFrame_Calendar['本日'] == today]
#         if DataFrame_Whether_Work['營業'].iloc[0] != 1: 
#             print('不用上班')
#             Whether_Work = '不用上班'
#         else: 
#             print('Go to Work.')
#             Whether_Work = 'Go to Work.'
#         return Whether_Work, None
    
#     # TODO: 2. 上一次上班日是什麼時候?
#     elif runmode == 2 or runmode == 3 :
#         DataFrame_PreviousWorkingDay = DataFrame_Calendar[DataFrame_Calendar['營業'] == 1] # 篩選出只有營業的日期
#         list_WorkingDay = list(DataFrame_PreviousWorkingDay['本日']) # 取出所有營業的日期
#         # today = pd.Timestamp(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')) # 若格式為時間，改用Timestamp
#         today = time.strftime("%Y/%m/%d", time.localtime())
#         # print(list_WorkingDay)
#         if today not in list_WorkingDay: #若今天日期不再營業日期list中 
#             Whether_Work = '不用上班'
#             return Whether_Work, None
#         Current_Index = list_WorkingDay.index(today)
#         # Current_Index = DataFrame_PreviousWorkingDay[DataFrame_PreviousWorkingDay['本期'] == today].index
#         # print(int(Current_Index))
#         if runmode == 2 :
#             PreviousWorkingDay = list_WorkingDay[Current_Index-n] # 取出前n次的營業日期
#             Whether_Work = 'Go to Work.'
#             return Whether_Work, PreviousWorkingDay
#         elif runmode == 3 :
#             NextWorkingDay = list_WorkingDay[Current_Index+n] # 取出前n次的營業日期
#             Whether_Work = 'Go to Work.'
#             return Whether_Work, NextWorkingDay


# #主流程
# if __name__ == "__main__":
#     # 參數設定
#     runmode = ''
#     while runmode == '' or (len(runmode) != 1 and (runmode != '1' and runmode != '2' and runmode != '3')): 
#         runmode = input('請輸入執行模式，\n1為查詢當天是否為工作日，2為查詢前一個工作日，3為查詢後一個工作日，\n輸入模式：')
#     print('執行模式: ' + str(runmode))
#     runmode = int(runmode) # 將runmode轉換為數字型式，後續傳如def
#     # 路徑設定
#     File_Directory = r'D:\哲平\新光銀行\RPA\Calendar'
#     File_Name = r'工作日查詢.xls'
#     FilePath = os.path.join(File_Directory, File_Name)
#     # print(FilePath)
#     sheet_name='reorganize'
#     Whether_Work, InquiryWorkingDay = calendar (FilePath=FilePath, sheet_name=sheet_name, runmode=runmode)
#     print(Whether_Work, InquiryWorkingDay)



    

