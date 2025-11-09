import findspark

findspark.init()
#import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode
spark = SparkSession.builder.appName("demo").getOrCreate()
df=spark.createDataFrame(
    [
        (1,['jyotsna','thakur']),
        (2,['ayansh','kumar'])
    ],
    ['id','name']

)
df.show()
df1=df.select(col('id'),explode(col('name')))
df1.show()