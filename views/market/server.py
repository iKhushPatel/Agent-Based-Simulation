from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from market.agents import amazonprime, disneyplus, netflix
#from market.agents import appletv
from market.model import market


def corona_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is amazonprime:
        portrayal["Shape"] = "market/resources/amazonprime.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    elif type(agent) is netflix:
        portrayal["Shape"] = "market/resources/netflix.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["text_color"] = "White"
    
    elif type(agent) is disneyplus:
        portrayal["Shape"] = "market/resources/disneyplus.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["text_color"] = "White"
        
    # elif type(agent) is appletv:
    #     portrayal["Shape"] = "market/resources/appletv.png"
    #     portrayal["scale"] = 0.9
    #     portrayal["Layer"] = 2
    #     portrayal["text_color"] = "White"

    
    return portrayal


canvas_element = CanvasGrid(corona_portrayal, 30, 30, 500, 500)
chart_element = ChartModule([{"Label": "amazonprime", "Color": "#0000FF"},
                                {"Label": "netflix", "Color": "#FF0000"},
                                {"Label": "disneyplus", "Color": "#00FF00"}
                                #{"Label": "appletv", "Color": "#000000"}
                              ])

model_params = {"quality_amazonprime": UserSettableParameter('slider', 'Quality amazonprime',25, 1, 100, 1),
                "quality_netflix": UserSettableParameter('slider', 'Quality netflix',50, 1, 100, 1),
                "quality_disneyplus": UserSettableParameter('slider', 'Quality disneyplus', 15, 1, 100 , 1),
                "content_amazonprime": UserSettableParameter('slider', 'Content amazonprime', 15, 1, 100 , 1),
                "content_netflix": UserSettableParameter('slider', 'Content netflix', 5, 1, 100 , 1),
                "content_disneyplus": UserSettableParameter('slider', 'Content disneyplus', 7, 1, 100 , 1)
                #"initial_appletv": UserSettableParameter('slider', 'Initial appletv', 10, 1, 100, 1)
               }

server = ModularServer(market, [canvas_element, chart_element], "DIgital TV Effect", model_params)
server.port = 8521
