import pandas as pd

import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(df, x="Date", y="Number of Cases", color="Country" )

fig.show()