import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

miles_per_gallon=pd.read_csv('mpg.csv')
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=miles_per_gallon, kind="line", ci="sd")

# Show plot
plt.show()