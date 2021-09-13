import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet",y="G3",kind="box", data=student_data, hue="location", sym="")


# Show plot
plt.show()