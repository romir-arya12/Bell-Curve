import plotly.figure_factory as ff
import random 
import plotly.express as px
import csv
import pandas as pd

df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["weight"],show_hist=False)
fig.show()
