import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

miles_per_gallon=pd.read_csv('mpg.csv')
# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", data=miles_per_gallon, kind="scatter", size="cylinders")

# Show plot
plt.show()