import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("demo").getOrCreate()
df=spark.createDataFrame(
    [
        ('jyotsna','70044549a80'),
        ('ram',66998867474)
    ],
    ['name','contact']
)
df.show()
df.select('*').filter(col('mobile').rlike('^[0-9]*$')).show()
#df=spark.sql("select * from student")
#df.show()
#spark.sql(select * from student where contact rlike'^[0-9]*$').show()