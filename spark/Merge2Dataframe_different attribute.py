import findspark
findspark.init()
#import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
spark = SparkSession.builder.appName("demo").getOrCreate()
df1 = spark.createDataFrame(
    [
        (1,'Ram','CS','Bangalore',80),
        (2,'Shalini','His','Patna',90)
    ],
    ['Id','Name','dept','city','marks']
)
df2 = spark.createDataFrame(
    [
        (1,'Ram','CS','Bangalore'),
        (2,'Shalini','His','Patna')
    ],
    ['Id','Name','dept','city']
)
df1.show()
df2.show()
df2=df2.withColumn("marks",lit("null").alias("marks"))
df=df1.union(df2)
df.show()


