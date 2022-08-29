from cl_model import CL
import pandas as pd
import plotly.express as px
import json


with open("config.json", encoding="utf8") as file:
    config = json.load(file)

cl = CL(config)

df_simulations = pd.DataFrame(
                    cl.generate_simulations(config["num_simulations"])
                    ).T


px.line(df_simulations)