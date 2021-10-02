import boto3
import pandas as pd

# criar um cliente para integragir com S3
s3_client = boto3.client('s3')

# baixa o arquivo do bucket S3
s3_client.download_file('bucket-igti-roncato', 'data_saude.csv', 'data/data_saude.csv')

# fazendo upload de arquivo para o bucket S3
s3_client.upload_file('data/comp_bikes_mod.csv', 'bucket-igti-roncato', 'comp_bikes_mod.csv')

