from itertools import count

import pandas as pd
from pip._internal.commands import show

#Load our dataset
df=pd.read_csv("data/supermarket_sales")

#Display our first five rows and columns
print(df.head())

#Number of rows and columns of the dataset
print("\nRows,columns")
print(df.shape)

#Display the column names
print("\ncolumn names",df.columns)

#checking for missing data
print(df.isnull().sum())
print("\nTotal missing values",df.isnull().sum().sum())

#checking the datatype of each  columns
print("\nDatatypes of each column")
print(df.dtypes)

#checking number of duplicated values
print("\nNumber of duplicate data",df.duplicated(keep=False).sum())

#checking if there is missing entries and duplicate invoices
print("\nMissing entries of Invoice  ID :",df["Invoice ID"].isnull().any())
print("Duplicate Invoice ID:",df["Invoice ID"].duplicated().any())

#Inspecting dates
df["Date"]=pd.to_datetime(df["Date"],errors="coerce")

print("\n",df["Date"].describe())
print("\nNumber of missing values after inspection:",df["Date"].isnull().sum())
print("\n------IT IS TRUE THAT------")
print("The dataset lies between the three month period "
      f"That is from {df["Date"].min()} to {df["Date"].max()}"
      )

#Inspecting Quantities
print("")
print(df["Quantity"].describe().round(3))
print(df["Quantity"].value_counts().sort_index())
print("Number of value:",df["Quantity"].value_counts().sum())

print("\n------AFTER INSPECTING QUANTITY IT WAS FOUND OUT THAT------")
print("The number of values at the Quantity column is 1000.")
print("Quantity 10 appears most(119 times) and Quantity 8 appears less(85 times)")

#Inspecting prices
print("\n",df["Unit price"].describe())

#identifying zero or negative prices
print(df[df["Unit price"]<=0])

#Examining highest prices
print(df.nlargest(10,"Unit price")[["Product line","Unit price"]])

#check whether the total sells are consistent
import numpy as np
print(df[["Unit price","Quantity","Total"]].head(10))

print("\nGrand total",df["Total"].sum())

expected_total=df["Unit price"]*df["Quantity"]

print("\n")
print(
      df[
      ~np.isclose(df["Total"],expected_total,rtol=1e-05,atol=0.01)
      ][["Unit price","Quantity","Total"]])


print("\n----------SUMMARY OF INSPECTIONS----------")
print("Missing dates:", df["Date"].isna().sum())
print("Zero or negative quantities:", (df["Quantity"] <= 0).sum())
print("Zero or negative prices:", (df["Unit price"] <= 0).sum())
print("Missing quantities:", df["Quantity"].isna().sum())
print("Missing prices:", df["Unit price"].isna().sum())

# Analyzing the business performance

# Total sales across all branches
Total_sales=df["Total"].sum()

print("\nTotal sales of the three branches:",Total_sales.round(3))

# Total sales of Branch A
Total_sales_A=df.loc[df["Branch"]=="A","Total"].sum()
print("Total sales of Branch A:",Total_sales_A.round(3))

# Total sales of Branch B
Total_sales_B=df.loc[df["Branch"]=="B","Total"].sum()
print("Total sales of Branch B:",Total_sales_B.round(3))

# Total sales of Branch C
Total_sales_C=df.loc[df["Branch"]=="C","Total"].sum()
print("Total sales of Branch C:",Total_sales_C.round(3))

#Average transactions sales

Total_average_sales=df["Total"].mean()
print("\nAverage transactions sales for all the branches:",Total_average_sales.round(3))

#Total transactions sales of Branch A
Total_average_sales_A=df.loc[df["Branch"]=="A","Total"].mean()
print("Average transactions sales A:",Total_average_sales_A.round(3))

#Total transactions sales of branch B
Total_average_sales_B=df.loc[df["Branch"]=="B","Total"].mean()
print("Average transactions sales B:",Total_average_sales_B.round(3))

#Total transactions sales of branch C
Total_average_sales_C=df.loc[df["Branch"]=="C","Total"].mean()
print("Average transactions sales C:",Total_average_sales_C.round(3))

#Total Quantity

Total_Quantity=df["Quantity"].sum()
print("\nTotal quantity of goods of the three branches",Total_Quantity)

#Total Quantity of branch A
Total_quantity_A=df.loc[df["Branch"]=="A","Quantity"].sum()
print("Total quantity of goods of Branch A:",Total_quantity_A.round(3))

#Total Quantity of branch C
Total_quantity_B=df.loc[df["Branch"]=="B","Quantity"].sum()
print("Total quantity of goods of Branch B:",Total_quantity_B.round(3))


#Total Quantity of branch C
Total_quantity_C=df.loc[df["Branch"]=="C","Quantity"].sum()
print("Total quantity of goods of Branch C:",Total_quantity_C.round(3))


# Customer Ratings
print("\n")
print(df["Rating"])
print("\nThe maximum rating is:",df["Rating"].max())
print("The minimum rating attained:",df["Rating"].min())

#Average customer ratings
Average_Rating=df["Rating"].mean()
print("\nThe average rating of customers across the three branches is:",Average_Rating)

#average rating of customers in branch A
Average_Rating_A=df.loc[df["Branch"]=="A","Rating"].mean()
print("The average rating of customers in branch A:",Average_Rating_A.round(3))

#average rating of customers in branch B
Average_Rating_B=df.loc[df["Branch"]=="B","Rating"].mean()
print("The average rating of customers in branch B:",Average_Rating_B.round(3))

#average rating of customers in branch C
Average_Rating_C=df.loc[df["Branch"]=="C","Rating"].mean()
print("The average rating of customers in branch C:",Average_Rating_C.round(3))

#comparison of sales across the three branches
print("\n-----comparison of sales across the three branches-------")
Range=Total_sales_C-Total_sales_B
print("The range of the total sales",Range.round(3))

import matplotlib.pyplot as pit
branches=["Branch A","Branch B","Branch C"]

pit.figure(figsize=(8,5))

total_sales_All=[Total_sales_A,Total_sales_B,Total_sales_C]

#creating the bar graph of total sales across the branches
bars=pit.bar(branches,total_sales_All,color="skyblue",edgecolor="black")

pit.bar_label(bars,fmt="%.1f",padding=3)
#Formatting the graph
pit.title("Comparison of branches by total sales",fontsize=16)
pit.xlabel("Branches of company",fontsize=12)
pit.ylabel("Total sales",fontsize=12)
pit.tight_layout()

#saving the bar graph
pit.savefig("images/Comparison of branches by total sales.png",dpi=300,bbox_inches="tight")

#Display the bar graph
pit.show()

#creating a bar graph of average sales for all three branches
Total_Average_sales_All=[Total_average_sales_A,Total_average_sales_B,Total_average_sales_C]

pit.figure(figsize=(8,5))
#creating the bar graph of total sales across the branches
bars=pit.bar(branches,Total_Average_sales_All,color="skyblue",edgecolor="black")
pit.bar_label(bars,fmt="%.1f",padding=3)

#Formatting the graph
pit.title("Comparison of branches by there average sales",fontsize=16)
pit.xlabel("Branches of company",fontsize=12)
pit.ylabel("Average sales",fontsize=12)
pit.tight_layout()

#saving the bar graph
pit.savefig("images/Comparison of branches by Average sales.png",dpi=300,bbox_inches="tight")

#Display the bar graph
pit.show()

range_average_sales=Total_average_sales_C-Total_average_sales_A
print("The range of average sales is:",range_average_sales.round(3))

#creating a bar graph of quantity of goods for all three branches
Total_Quantity_All=[Total_quantity_A,Total_quantity_B,Total_quantity_C]

pit.figure(figsize=(8,5))
#creating the bar graph of total sales across the branches
bars=pit.bar(branches,Total_Quantity_All,color="skyblue",edgecolor="black")
pit.bar_label(bars,fmt="%.1f",padding=3)

#Formatting the graph
pit.title("Comparison of branches by Quantity of goods",fontsize=16)
pit.xlabel("Branches of company",fontsize=12)
pit.ylabel("Quantity of goods",fontsize=12)
pit.tight_layout()

#saving the bar graph
pit.savefig("images/Comparison of branches by quantity of goods ",dpi=300,bbox_inches="tight")

#Display the bar graph
pit.show()


#creating bar charts to show comparison
sales=[Total_sales_A,Total_sales_B,Total_sales_C]
pit.pie(sales,labels=branches,autopct="%1.1f%%",startangle=90,shadow=True)
pit.title("A bar chart showing comparison of branches by sales",fontsize=16)
pit.savefig("images/Bar chart of comparison of sales.png",dpi=300,bbox_inches="tight")
pit.show()

#Ratings of the three branches
Ratings=[Average_Rating_A,Average_Rating_B,Average_Rating_C]
pit.pie(Ratings,labels=branches,autopct="%1.1f%%",startangle=90,shadow=True)
pit.title("A bar chart showing comparison of branches by Rating",fontsize=16)
pit.savefig("images/Bar chart of comparison of ratings .png",dpi=300,bbox_inches="tight")
pit.show()

#calculating the range of quantity of goods
Range_Quantity=max(Total_Quantity_All)-min(Total_Quantity_All)
print("The range of quantity is:",Range_Quantity)

#The spread of sales of Branch A
print("The standard deviation of branch A sales is:",df.loc[df["Branch"]=="A","Total"].std().round(2))
print ("The mean of branch A sales is:",df.loc[df["Branch"]=="A","Total"].mean().round(2))

#The spread of sales of Branch B
print("The standard deviation of branch B sales is:",df.loc[df["Branch"]=="B","Total"].std().round(2))
print ("The mean of branch B sales is:",df.loc[df["Branch"]=="B","Total"].mean().round(2))

#The spread of sales of Branch C
print("The standard deviation of branch C sales is:",df.loc[df["Branch"]=="C","Total"].std().round(2))
print ("The mean of branch C sales is:",df.loc[df["Branch"]=="C","Total"].mean().round(2))


