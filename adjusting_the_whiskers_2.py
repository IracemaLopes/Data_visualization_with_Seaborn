import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5,95])

# Show plot
plt.show()