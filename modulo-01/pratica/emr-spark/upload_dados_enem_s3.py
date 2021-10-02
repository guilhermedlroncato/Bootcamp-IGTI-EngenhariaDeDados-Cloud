import boto3
import pandas as pd

# criar um cliente para integragir com S3
s3_client = boto3.client('s3')

# fazendo upload de arquivo para o bucket S3
s3_client.upload_file('../dados/microdados_enem_2019/DADOS/MICRODADOS_ENEM_2019.csv', 'bucket-igti-roncato', 'raw-data/enem/year=2019/MICRODADOS_ENEM_2019.csv')

