import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges"],
    "Amount": [4, 1],
    "City": ["SF", "SF"]
})

fig = px.bar(df, x = "Fruit", y = "Amount", color = "City")

#==========================
#layout

app.layout = html.Div(id="div.1",
                      
    children=[
        html.H1("Hello Dash", id="h1"),

        html.Div("Dash: Um framework web para python"),

        html.H6("Altere o valor abaixo para ver o callback em ação"),

        html.Div(["Entrada:",
                  dcc.Input(id="my-input", value="Valor incial", type="text")]),

        html.Br(),

        html.Div(id="my-output"),
        
        dcc.Graph(figure=fig, id="graph")
    ]
)

@app.callback(
        Output(component_id="my-output", component_property="children"), 
        [Input(component_id="my-input", component_property="value")]
)
def update_output_div(value):
    return "Saída: {}".format(value)

# Expondo o Flask server para o Render (importante!)
server = app.server  

if __name__ == '__main__':
    print("Rodando o app...")
    app.run_server(debug=True, host="0.0.0.0", port=8050)
