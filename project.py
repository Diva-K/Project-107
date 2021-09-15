import pandas as pd
import csv
import plotly.graph_objects as go
import plotly_express as px
df=pd.read_csv("data.csv")
mean=(df.groupby(["student_id","level"],as_index=False)["attempt"].mean())
#fig=go.Figure(go.Scatter(x=df.groupby("level")["attempt"].mean(),
#y=['level 1', 'leave 2', 'level 3', 'level 4'], orientation='h'
fig=px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")

fig.show()