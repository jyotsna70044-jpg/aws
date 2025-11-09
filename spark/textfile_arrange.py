import findspark


findspark.init()
#import pyspark
from pyspark.sql import SparkSession

from pyspark.sql.functions import split, regexp_replace,explode
spark = SparkSession.builder.appName("demo").getOrCreate()
df=spark.read.text('./data_set/stud.txt')
df.show()
df2=df.withColumn('new_value',regexp_replace('value','(.*?\\-){3}','$0,')).drop('value')
df2.show()
df3=df2.withColumn('new_value1',explode(split(df2.new_value,'-,'))).drop('new_value')
df3.show()
df4=df3.withColumn('id',split(df3.new_value1,'-')[0]).\
            withColumn('name',split(df3.new_value1,'-')[1]).\
            withColumn('age',split(df3.new_value1,'-')[2]).drop('new_value1')
df4.show()