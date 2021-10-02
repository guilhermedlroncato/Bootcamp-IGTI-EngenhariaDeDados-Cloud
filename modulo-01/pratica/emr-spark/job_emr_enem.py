from pyspark.sql.functions import max, count, mean, col, min
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName('ExerciseSpark').getOrCreate()
)

# ler dados do enenm 2019 no S3
enem = spark.read\
        .format('csv')\
        .option('header', True)\
        .option('inferSchema', True)\
        .option('delimiter', ';')\
        .load('s3://bucket-igti-roncato/raw-data/enem/')

# salvar o dado em parquet no S3
enem\
    .write\
    .mode('overwrite')\
    .format('parquet')\
    .partitionBy('year')\
    .save('s3://bucket-igti-roncato/staging/enem/')
