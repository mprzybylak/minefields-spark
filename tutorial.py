from pyspark.sql import SparkSession
from pyspark import SparkContext



fileName = 'rdu-weather-history.csv'

sc = SparkContext("local", "First App")
spark = SparkSession(sc)

# print helps to see where application output starts
print("!!!!\n\n\n")

file = spark.read.load(fileName, format='csv', sep=";", header="true")

print(file.take(1))
file.show()

# print helps to see where application output ends
print("\n\n\n!!!!")

spark.stop()