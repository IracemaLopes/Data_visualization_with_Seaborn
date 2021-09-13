import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

survey_data=pd.read_csv('young-people-survey-responses.csv')
# Create count plot of internet usage
sns.catplot(x="Internet usage", data=survey_data, kind="count")

# Show plot
plt.show()