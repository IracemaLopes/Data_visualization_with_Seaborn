import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time")

# Show plot
plt.show()