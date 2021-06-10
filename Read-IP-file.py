## Read Combined IP address file into a list
#
import pandas as pd
#
print ("Reading a CSV file into a Data Frame")
#
csv_path = "Combined_Subset.csv"
#
# Using Data Frames
#
csvDF = pd.read_csv(csv_path)
#
# The the data frame method "head" reads the first 5 records of the file
#
# df.head()
#
print("type(csvDF) = ", type(csvDF) )
#
print("csvDF       = \n", csvDF       )
#
print ("===========================")
#
print("END")