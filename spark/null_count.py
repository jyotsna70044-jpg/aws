import findspark

findspark.init()
#import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, when,count

spark = SparkSession.builder.appName("demo").getOrCreate()
df=spark.read.option("nullvalue",'null').option('header',True).csv('./data_set/emp.csv')
df.show()


df1=df.select([count(when(col(i).isNull(),i)).alias(i) for i in df.columns])
df1.show()
# print(df[col('id').isNull()].count())
# print(df[col('name').isNull()].count())
# print(df[col('age').isNull()].count())

