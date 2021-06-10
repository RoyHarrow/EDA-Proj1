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
print("Number of Rows:", len(csvDF) )
#
print ("===========================")
#
# Add empty columns
#
csvDF["Country-Code"]   = ""
csvDF["Country"]        = ""
csvDF["City"]           = ""
csvDF["Latitude"]       = 0.0
csvDF["Longitude"]      = 0.0
#
print("csvDF       = \n", csvDF       )
#
print ("===========================")
#
for i in range(len(csvDF) ):
    print(i, csvDF.loc[i,"IP Address"])
    csvDF.loc[i,"Country-Code"] = "XX" + str(i)
    csvDF.loc[i,"Country"]      = "XXXX" + str(i)
    csvDF.loc[i,"City"]         = "CCCC" + str(i)
    csvDF.loc[i,"Latitude"]     = float(i)
    csvDF.loc[i,"Longitude"]    = float(i)
#
print("csvDF       = \n", csvDF       )
#
# Write updated file out from Pandas Dataframe
#
out_path = "Combined_Subset2.csv"
#
csvDF.to_csv(out_path,index=False)
#
#
print("END")