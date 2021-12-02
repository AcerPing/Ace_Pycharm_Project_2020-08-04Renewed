import os
import sys
import time
import traceback
import xlrd
import re

def check_result():
    '''
    檢查寫入的結果檔是否是否符合格式
    '''
    Custom_Err_Msg = ''

    # TODO: 讀取 今天是否上班 檔案
    with open("今天是否上班.txt",mode="r",encoding="utf-8") as file:
        datum=file.read()
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
    with open("上一個營業日.txt",mode="r",encoding="utf-8") as file:
        datum=file.read()
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
    with open("下一個營業日.txt",mode="r",encoding="utf-8") as file:
        datum=file.read()
    # print(datum)
    o = re.fullmatch("^[0-9]{4}/[0-9]{2}/[0-9]{2}\n$", datum)
    # print(o)
    if o != None: print('True')
    else:
        Custom_Err_Msg += '下一個營業日 結果報表錯誤'
        print('Excel Error')
        print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        raise Exception('結果報表 Error', Custom_Err_Msg)
