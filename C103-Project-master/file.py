import pandas as pd
import plotly_express as px

dataFrame = pd.read_csv("Copy+of+data+-+data.csv")
figure = px.scatter(dataFrame, x="Date", y="Cases", color="Country")
figure.show()