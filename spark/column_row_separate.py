import findspark
findspark.init()
#import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode

spark = SparkSession.builder.appName("demo").getOrCreate()
df=spark.read.option('header',True).option('sep',',').csv('./data_set/student.csv')
df.show()
df1=df.withColumn('physics',split(df.marks,'\\|')[0]).\
     withColumn('chemistry',split(df.marks,'\\|')[1]).\
     withColumn('math',split(df.marks,'\\|')[2])
df2=df1.drop(df1.marks)
df2.show()
df3=df.select('id','name','age',explode(split(df.marks,'\\|')))
df3.show()

