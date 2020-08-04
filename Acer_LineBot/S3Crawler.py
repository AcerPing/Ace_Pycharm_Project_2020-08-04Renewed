'''
爬網頁下來，並存到S3的桶子內
request example python
'''

#TODO:爬網頁下來
#request example python
import requests
res = requests.get('https://www.toutiao.com/')

#TODO:存成檔案
#write string to file python
text_file = open("sample.html", "w",encoding="utf8")
n=text_file.write(res.text)
text_file.close()

'''
s3demo.py
'''

import boto3

#TODO:上傳檔案到S3
#Upload File to S3 boto3
#TODO:創建客戶端
s3_client = boto3.client('s3',
                         aws_access_key_id="AKIAR4NDUH53GWDLQFNM",
                         aws_secret_access_key="DHHfSg5PrBysKBzcNaEo2qTWYQksrhTFgPqwNKm7")
#TODO:用客戶端上傳到S3的Bucket
response = s3_client.upload_file("sample.html"
                                 , "iii-tutorial-v2"
                                 , "student_30_Ace/sample.html")

#打印結果
print(response)