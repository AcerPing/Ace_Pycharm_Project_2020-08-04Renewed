#TODO:引用套件
import boto3


#TODO:上傳檔案到S3
#Upload File to S3 boto3

#TODO:創建客戶端

#第二種方法:隱藏資料夾
s3_client = boto3.client('s3')


'''
第一種方法:程式碼
s3_client = boto3.client('s3',
                         aws_access_key_id="AKIAR4NDUH53GWDLQFNM",
                         aws_secret_access_key="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")
'''


'''
#TODO:用客戶端上傳到S3的Bucket
response = s3_client.upload_file("ngrok_is_shit.txt"
                                 , "iii-tutorial-v2"
                                 , "student_30_Ace/ngrok_is_shit.txt")
#打印結果
print(response)
'''


#TODO:用戶從S3下載檔案
#Download File by boto3
s3_client.download_file("iii-tutorial-v2", "student_30_Ace/sample.html", "download_sample.html")