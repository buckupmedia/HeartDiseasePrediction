# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

df = pd.read_csv("heart.csv")

##df = pd.DataFrame(data)

df.head()

#checking for the null values or missing values in the data set 
df.isnull().sum()

df.describe()

df.info()

df.head()

## **Age Analysis**

plt.figure(figsize = (12,6))
sns.displot( x = df["Age"] , edgecolor = "black", linewidth = 2, palette = "husl")
plt.title("No of Observers from Different Age Groups", color = "red", fontsize = 22)
plt.show()



sns.distplot(df["Age"], hist = True, bins = 10)

## **SEX ANALYSIS**

fig , ax =plt.subplots(1,2,figsize = (12,6))
df.groupby("Sex").size().plot( kind = "bar", edgecolor = "black", linewidth = 2,  ax = ax[0])

plt.title("SEX of Observers", color = "red", fontsize = 22)

df.groupby("Sex").size().plot(kind = "pie", autopct = "%.2f", ax = ax[1])
plt.show()


## **Chest Pain Analysis**

fig , ax =plt.subplots(1,2,figsize = (12,6))
df.groupby("ChestPainType").size().plot( kind = "bar", edgecolor = "black", linewidth = 2,  ax = ax[0])

plt.title("No of Observers having Diffrent types of Chestpains", color = "red", fontsize = 22)

df.groupby("ChestPainType").size().plot(kind = "pie", autopct = "%.2f", ax = ax[1])
plt.show()


## *Cholesterol Analysis*

plt.figure(figsize = (12,6))
sns.displot( x = df["Cholesterol"] , edgecolor = "black", linewidth = 2, palette = "husl", kde = True)
plt.title("Cholesterol Range in the Observers", color = "red", fontsize = 22)
plt.show()



## *FastingBS Analyis*

fig , ax =plt.subplots(1,2,figsize = (12,6))
df.groupby("FastingBS").size().plot( kind = "bar", edgecolor = "black", linewidth = 2,  ax = ax[0])

plt.title("FastingBS", color = "red", fontsize = 22)

df.groupby("FastingBS").size().plot(kind = "pie", autopct = "%.2f", ax = ax[1])
plt.legend()
plt.show()



## *RestingECG Analysis*

fig , ax =plt.subplots(1,2,figsize = (12,6))
df.groupby("RestingECG").size().plot( kind = "bar", edgecolor = "black", linewidth = 2,  ax = ax[0])
ax[0].set_xlabel("Type of ECG", fontsize = 12)

plt.title(" Type of RestingECG to the Observers", color = "red", fontsize = 22)

df.groupby("RestingECG").size().plot(kind = "pie", autopct = "%.2f", ax = ax[1])
plt.show()

## **Heart Rate Analysis** 

plt.figure(figsize = (12,6))
sns.displot( x = df["MaxHR"] , edgecolor = "black", linewidth = 2, palette = "husl", kde = True)
plt.title("Max HeartRate in the Obersvers", color = "red", fontsize = 22)
plt.show()

## *ExerciseAngina*

fig , ax =plt.subplots(1,2,figsize = (12,6))
df.groupby("ExerciseAngina").size().plot( kind = "bar", edgecolor = "black", linewidth = 2,  ax = ax[0])

plt.title("ExerciseAngina  in Observers", color = "red", fontsize = 22)

df.groupby("ExerciseAngina").size().plot(kind = "pie", autopct = "%.2f", ax = ax[1])
plt.show()

## *Oldpeak Analysis*

plt.figure(figsize = (12,6))
sns.displot( x = df["Oldpeak"] , edgecolor = "black", linewidth = 2, palette = "husl", kde = True)
plt.title("Oldpeak of the Obersvers", color = "red", fontsize = 22)
plt.show()

## *ST_Slope Analysis*

fig , ax =plt.subplots(1,2,figsize = (12,6))
df.groupby("ST_Slope").size().plot( kind = "bar", edgecolor = "black", linewidth = 2,  ax = ax[0])

plt.title("ST SLOPE  in Observers", color = "red", fontsize = 22)

df.groupby("ST_Slope").size().plot(kind = "pie", autopct = "%.2f", ax = ax[1])
plt.show()

## *HeartDisease Analysis*

df.groupby("HeartDisease").size().plot(kind = "pie", autopct = "%.2f")
plt.title("HeartDisease to the Obersvers", color = "red", fontsize = 22)
plt.show()

## **Multicolumn Analysis**

sns.countplot(data = df, x = "HeartDisease", hue = "Sex", edgecolor = "black", linewidth = 2)
plt.title("Gender wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

plt.figure(figsize = (12,6))

sns.countplot(data = df, x = "Age", hue = "HeartDisease", edgecolor = "black", linewidth = 2)
plt.title("Age wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

plt.figure(figsize = (12,6))

sns.countplot(data = df, x = "ChestPainType", hue = "HeartDisease", edgecolor = "black", linewidth = 2)
plt.title("ChestPainType wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

plt.figure(figsize = (12,6))

sns.countplot(data = df, x = "ChestPainType", hue = "HeartDisease", edgecolor = "black", linewidth = 2)
plt.title("ChestPainType wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

plt.figure(figsize = (12,6))

sns.countplot(data = df, x = "FastingBS", hue = "HeartDisease", edgecolor = "black", linewidth = 2, width = 0.4)
plt.title("FastingBS wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

plt.figure(figsize = (12,6))

sns.countplot(data = df, x = "RestingECG", hue = "HeartDisease", edgecolor = "black", linewidth = 2)
plt.title("RestingECG Type wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

plt.figure(figsize = (12,6))

sns.countplot(data = df, x = "ExerciseAngina", hue = "HeartDisease", edgecolor = "black", linewidth = 2, width = 0.5)
plt.title("ExerciseAngina wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

plt.figure(figsize = (12,6))

sns.countplot(data = df, x = "ST_Slope", hue = "HeartDisease", edgecolor = "black", linewidth = 2)
plt.title("ST_Slope wise Analysis of Observers having Heart Disease", fontsize = 14, color = "Red")

## **Correlation**

df1 = df[["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak","HeartDisease"]]

df1.corr()

sns.heatmap(df1.corr(), cmap = "Greens")


sns.pairplot(df1)