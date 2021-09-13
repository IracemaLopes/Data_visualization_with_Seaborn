import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

miles_per_gallon=pd.read_csv('mpg.csv')
# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower",
            data=miles_per_gallon, kind="line",
            ci=None, style="origin", hue="origin")

# Show plot
plt.show()