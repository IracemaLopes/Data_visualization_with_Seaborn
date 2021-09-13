import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

miles_per_gallon=pd.read_csv('mpg.csv')
# Create point plot
sns.catplot(x="origin",
            y="acceleration",
            data=miles_per_gallon,
            kind="point",
            join=False,
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()