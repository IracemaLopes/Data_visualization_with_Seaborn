import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

survey_data=pd.read_csv('young-people-survey-responses.csv')
# Change the orientation of the plot
sns.catplot( y="Internet usage",data=survey_data,
            kind="count")

# Show plot
plt.show()