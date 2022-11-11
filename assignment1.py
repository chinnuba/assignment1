# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 01:32:23 2022

@author: CHINNU BABY
"""
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
#creating a dataframe to read csv file using pandas and print
ADR=pd.read_csv('age dependency ratio.csv')
print(ADR)
#extracting rows 115 to 119 from the original dataframe ADR and print
ratio=ADR[115:120]
print(ratio)
#function to plot a line chart
def plotFunction():
   
    plt.figure()
#plotting the line chart with suitable labels 
    plt.plot(ratio["Country Name"],ratio["2021"],label="2021")
    plt.plot(ratio["Country Name"],ratio["1990"],label="1990")
    plt.plot(ratio["Country Name"],ratio["1960"],label="1960")
#labelling x-axis and y-axis
    plt.xlabel("Country")
    plt.ylabel("Age Dependency Ratio")
#giving a title to the line chart
    plt.title("Age Dependency Ratio")
#add the legend
    plt.legend()
#saving the output line chart
    plt.savefig("line_chart.png")
#displaying the chart
    plt.show()
#calling the function
plotFunction()

#function to plot bar chart
def barFunction():
    plt.figure()
#plotting the bar chart with suitable labels and adding alpha for the transparency of bars
    plt.bar(ratio["Country Name"],ratio["2021"],label="2021", alpha=0.4)
    plt.bar(ratio["Country Name"],ratio["1990"],label="1990", alpha=0.4)
    plt.bar(ratio["Country Name"],ratio["1960"],label="1960", alpha=0.4)
#labelling x-axis and y-axis
    plt.xlabel("Country")
    plt.ylabel("Age Dependency Ratio")
#giving a title to the bar chart
    plt.title("Age Dependency Ratio")
#adding the legend
    plt.legend()
#saving the output bar chart
    plt.savefig("bar_chart.png")
    plt.show()
#calling the function
barFunction()

#function to plot the box plot
def boxplotFunction():
    plt.figure()
#plotting the box plot with suitable labels
    plt.boxplot([ratio["2021"],ratio["1990"],ratio["1960"]],labels=["2021","1990","1960"])
#labelling x-axis and y-axis    
    plt.xlabel("Year")
    plt.ylabel("Age Dependency Ratio")
#giving a title to the box plot
    plt.title("Age Dependency Ratio")
#add the legend
    plt.legend()
#saving the output box plot
    plt.savefig("box_plot.png")
    plt.show()
#calling the function
boxplotFunction()   