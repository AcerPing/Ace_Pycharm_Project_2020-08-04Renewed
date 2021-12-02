import os
import sys
import time
import traceback
import xlrd
import re

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

# Download Excel
def download_excel():
    '''
    下載工作日查詢.xls
    '''
    from urllib.request import urlretrieve 
    import Download_Website
    Excel_Path = Download_Website.Download_Website #下載網址
    save_path = os.getcwd()
    urlretrieve(Excel_Path, save_path) #利用urlretrieve下載檔案
    return True

def month_n():
    '''
    抓取檔名，判斷第N個營業日
    '''
    Custom_Err_Msg = ''
    print(os.path.basename(__file__)) # 抓取程式檔名
    exe_filename = (os.path.basename(__file__)) # 抓取程式檔名
    n = exe_filename[exe_filename.find('第')+1:exe_filename.find('個')]
    if not n.isdigit():
        Custom_Err_Msg += '檔名錯誤'
        print('檔名 Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('檔名 Error', Custom_Err_Msg)
    return int(n)

def check_result(datum=''):
    '''
    檢查寫入的結果檔是否是否符合格式
    '''
    Custom_Err_Msg = ''
    o = re.fullmatch("^[0-9]{4}/[0-9]{2}/[0-9]{2}$", datum)
    # print(o)
    if o != None: 
        print('True')
        return True
    else:
        Custom_Err_Msg += '日期格式設定錯誤'
        print('Date Format Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Date Format Error', Custom_Err_Msg)

# 主函式
def main(TxtName):
    '''
    #判斷今天是否為第N個營業日(同檔名的營業日)
    '''
    # 參數設定
    Custom_Err_Msg = ''

    # TODO: 設定讀取檔案的位置及表單資訊
    File_Directory = os.getcwd() #D:\何哲平\RPA\工作日查詢
    File_Name = r'工作日查詢.xls'
    FilePath = os.path.join(File_Directory, File_Name)
    SourceFilePath_Excel = FilePath
    SourceFilePath_Excel = SourceFilePath_Excel.replace('\u202a','')
    #檢查檔案路徑是否存在
    if os.path.exists(SourceFilePath_Excel) == False: #檔案不存在
        PrintText = 'File is not existed. Please check the path of the file.'
        print(PrintText)
        Custom_Err_Msg += PrintText
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception ('File Not Existed Error', Custom_Err_Msg)
    
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
        Custom_Err_Msg += 'No Data found in Excel. Pleaser Check Your Report.'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error', Custom_Err_Msg)

    today = time.strftime("%Y/%m/%d", time.localtime()) # 今天日期

    #TODO:測試時設定today日期
    if (os.path.isdir(os.path.join(os.getcwd(), 'Test'))) and \
    (os.path.isfile(os.path.join(os.getcwd(),'Test', (os.path.splitext(os.path.basename(__file__))[0]+'.txt')))):
        f = open((os.path.join(os.getcwd(),'Test', (os.path.splitext(os.path.basename(__file__))[0]+'.txt'))), 'r', encoding='utf-8')
        for x in f:
            if 'today=' in x.lower():
                today = x.lower().strip().replace('today=', '').strip()
                check_result(datum=today)
                print('today set to: ' + today)

    list_month_n = [today]
    n = month_n() #?個工作天
    this_month = today.split('/')[1] #today月份

    # print(Excel_todo_list[0]) # 與Excel檔案列號差2
    # print (i + 2) 
    # print(Excel_todo_list[i]) 
    # print(ConvertNum(Excel_todo_list[i][key_column_id['營業']])) 
    for i in range(0, len(Excel_todo_list)):
        if Excel_todo_list[i][key_column_id['本日']] == today: break #抓取今日日期的index
    else: 
        Custom_Err_Msg += '今天日期沒有在Excel Report'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error', Custom_Err_Msg)

    if ConvertNum(Excel_todo_list[i][key_column_id['營業']]) != 1: 
        print('不用上班')
    else: 
        print('Go to Work.')
    Whether_Work = ConvertNum(Excel_todo_list[i][key_column_id['營業']])

    # TODO: 取n前天日期
    for ii in range(i-1, -1, -1):
        if ConvertNum(Excel_todo_list[ii][key_column_id['營業']]) ==  1 : 
            PreviousWorkingDay = Excel_todo_list[ii][key_column_id['本日']]
            list_month_n.append(PreviousWorkingDay)
        if len(list_month_n) == n+1: break
    else: 
        Custom_Err_Msg += '日期錯誤'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('Excel Error', Custom_Err_Msg)

    #TODO: 檢查是否為第n個營業日 -> True/False
    #First:判斷list_month_n最後一個是否為前一月份 
    #Second:判斷list_month_n倒數第二個是否同當月份
    print('list_month: {}'.format(list_month_n))
    if (int(list_month_n[-1].split('/')[1]) == int(this_month)-1) and \
        (ConvertNum(list_month_n[-2].split('/')[1]) == ConvertNum(this_month)):
        print('今天是第{}個營業日'.format(str(n).strip()))
        with open(TxtName, mode="w", encoding="utf-8") as file: file.write(str('True').strip()+'\n')
    else: 
        print('今天不是第{}個營業日'.format(str(n).strip()))
        with open(TxtName, mode="w", encoding="utf-8") as file: file.write(str('False').strip()+'\n')

if __name__ == "__main__":
   
    # # TODO: 下載 "工作日查詢.xls" 報表
    # # download_excel()

    # TODO: 執行檔名
    Name = os.path.splitext(os.path.basename(__file__))[0].strip()+'.txt'
    print(Name)
    TxtName = os.path.join(os.getcwd(), 'Result', Name)
    print(TxtName)
    
    #TODO: 建立Result資料夾
    if not ((os.path.exists('Result')) and (os.path.isdir('Result'))): os.mkdir('Result')

    # TODO: 執行，將結果寫入txt
    try:
        main(TxtName=TxtName)
        time.sleep(3)
        print('Done. 終わり！')
    except:
        error_message = sys.exc_info() #取得Call Stack
        with open(TxtName, mode="w", encoding="utf-8") as file:
            file.write(str(error_message).strip()+'\n')
        # input('Please "Key Enter" to continue the process.')
        time.sleep(5)
        sys.exit(1)


    
    
    






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


    # # TODO: 1. 當天是否為上班日
    # file=open("今天是否上班.txt",mode="w",encoding="utf-8") #開啟檔案
    # file.write(str(Whether_Work).strip()+"\n") #撰寫檔案
    # file.close() #關閉檔案
    
       
    # file=open("上一個營業日.txt",mode="w",encoding="utf-8") #開啟檔案
    # file.write(str(PreviousWorkingDay).strip()+"\n") #撰寫檔案
    # file.close() #關閉檔案
    
    # # TODO: 3. 下一次上班日是什麼時候?
    # for ii in range(i+1, len(Excel_todo_list)):
    #     if ConvertNum(Excel_todo_list[ii][key_column_id['營業']]) ==  1 : 
    #         NextWorkingDay = Excel_todo_list[ii][key_column_id['本日']]
    #         break
    # else: 
    #     Custom_Err_Msg += '沒有下一個營業日'
    #     print('Excel Error')
    #     print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
    #     raise Exception('Excel Error', Custom_Err_Msg)
    
    # file=open("下一個營業日.txt",mode="w",encoding="utf-8") #開啟檔案
    # file.write(str(NextWorkingDay).strip()+"\n") #撰寫檔案
    # file.close() #關閉檔案
        

