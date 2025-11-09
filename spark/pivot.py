import findspark
findspark.init()
#import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_replace,explode
spark = SparkSession.builder.appName("demo").getOrCreate()
df=spark.read.option('sep',',').option('inferSchema',True).csv('./data_set/studentpivot.csv',header=True)
df.show()
df.printSchema()
df1=df.groupby('roll').pivot('subject').max('marks')
df1.show()
df2=df1.withColumn('Total',df1['phy']+df1['che']+df1['math']).show()
