from pyspark.sql import SparkSession
from pyspark import SparkContext

fileName = 'rdu-weather-history.csv'

sc = SparkContext("local", "First App")
file = sc.textFile(fileName, minPartitions=None, use_unicode=True)

print("!!!!\n\n\n")
print(file)
print("\n\n\n!!!!")