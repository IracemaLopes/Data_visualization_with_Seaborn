import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

miles_per_gallon=pd.read_csv('mpg.csv')
# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower",
            data=miles_per_gallon, kind="line",
            ci=None, style="origin",
            hue="origin", markers=True, dashes=False)

# Show plot
plt.show()