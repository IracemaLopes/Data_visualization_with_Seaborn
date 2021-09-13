import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Rearrange the categories
categories=["<2 hours","2 to 5 hours", "5 to 10 hours",">10 hours"]
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar", order=categories)

# Show plot
plt.show()