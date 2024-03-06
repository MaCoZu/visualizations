import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui
from utils import gdp_plot, get_metadata

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider("n", "N", min=0, max=100, value=20),
    ),
    
    ui.row(
        ui.column(5, ui.output_plot("gdp1")),
        ui.column(5, ui.output_plot("gdp2")),
    ),
    
    ui.row(
        ui.column(5, ui.output_plot("gdp3")),
        ui.column(5, ui.output_plot("gdp4")),
    ),
)

def server(input, output, session):
    @output
    @render.plot(alt="GDP (PPP current $) per capita.")
    def gdp1():
        ax = gdp_plot()
        return ax
    
    @output
    @render.plot(alt="GDP (PPP current $) per capita.")
    def gdp2():
        ax = gdp_plot()
        return ax
    
    @output
    @render.plot(alt="GDP (PPP current $) per capita.")
    def gdp3():
        ax = gdp_plot()
        return ax
    
    @output
    @render.plot(alt="GDP (PPP current $) per capita.")
    def gdp4():
        ax = gdp_plot()
        return ax

app = App(app_ui, server)

