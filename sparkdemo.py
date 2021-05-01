from pyspark import SparkConf, SparkContext

sc = SparkContext(master="local", appName="Spark Demo")
print(sc.textFile("C:\\test\\deckofcards.txt").first())