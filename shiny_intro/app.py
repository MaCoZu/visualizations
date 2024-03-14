import matplotlib.pyplot as plt
import numpy as np
from htmltools import br
from shiny import App, Inputs, Outputs, Session, render, ui
from utils import gdp_plot, mil_spending_plot

app_ui = ui.page_fluid(
    ui.page_navbar(
        ui.nav_panel("progress", "progress"),
        ui.nav_panel("work", "work"),
        ui.nav_panel("nature", "nature"),
        ui.nav_panel("equality", "equality"),
        ui.nav_panel("social", "social"),
        title="Indicators",
        selected="progress",
        id="page",
        position="fixed-top",
        fluid=True,
    ),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_selectize(
                "var",
                "Select Indicators",
                [
                    "bill_length_mm",
                    "bill_depth_mm",
                    "flipper_length_mm",
                    "body_mass_g",
                    "year",
                ],
            ),
            bg="#f8f8f8",
        ),
        ui.panel_main(
            ui.row(
                ui.column(5, ui.output_plot("gdp1")),
                ui.column(5, ui.output_plot("mil_spend")),
                
            ),
            
            ui.row(
                ui.column(5, ui.output_plot("gdp2")),


            ),
        ),
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
    def mil_spend():
        fig = mil_spending_plot()
        return fig




app = App(app_ui, server)
