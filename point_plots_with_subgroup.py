import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Create a point plot with subgroups
sns.catplot(x="romantic",y="absences",hue="school",data=student_data, kind="point")

# Show plot
plt.show()