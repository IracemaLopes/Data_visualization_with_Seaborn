import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

miles_per_gallon=pd.read_csv('mpg.csv')
# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=miles_per_gallon,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()