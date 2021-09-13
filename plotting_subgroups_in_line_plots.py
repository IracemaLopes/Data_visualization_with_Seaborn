import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

miles_per_gallon=pd.read_csv('mpg.csv')

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year",y="horsepower", data=miles_per_gallon, ci=None, kind="line")



# Show plot
plt.show()