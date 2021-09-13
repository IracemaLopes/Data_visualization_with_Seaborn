import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0,100])

# Show plot
plt.show()