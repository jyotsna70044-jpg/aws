import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("demo").getOrCreate()

df=spark.createDataFrame(
    [
        (1,'jyotsna'),
        (2,'sneha')
    ],
    ['id','name']
)

df.show()



