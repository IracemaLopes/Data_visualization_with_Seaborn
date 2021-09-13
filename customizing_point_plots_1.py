import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel", y="absences", data=student_data, kind="point")

# Show plot
plt.show()