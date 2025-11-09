import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_replace, explode, col, lower, trim

spark = SparkSession.builder.appName("demo").getOrCreate()
df=spark.read.option('delimiter',',').option('header',True).csv('./data_set/movie.csv',)
df1=df.select('*').filter( (col('id')%2!=0) & (trim(lower(col('description')))!='boring') )
#df2=df1.orderBy(col("rating").desc())
df2=df1.orderBy(col('rating').desc())
df2.show()
