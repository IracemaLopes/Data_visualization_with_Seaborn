import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

miles_per_gallon=pd.read_csv('mpg.csv')

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", data=miles_per_gallon, style="origin", kind="scatter", hue="origin")

# Show plot
plt.show()