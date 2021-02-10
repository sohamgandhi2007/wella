import pandas as pd
import plotly.express as px

df=pd.read_csv("c.csv")
fig=px.scatter(df,x="Date",y="Cases",size="Percentage",color="Country",size_max=60)
fig.show()