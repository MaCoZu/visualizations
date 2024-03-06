from functools import partial

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import wbgapi as wb
from faicons import icon_svg as icon
from shiny import render
from shiny.express import input, render, ui
from shiny.ui import page_navbar
from shinywidgets import render_widget
from utils import gdp_plot, get_metadata

ui.page_opts(title="Economics Indicators Dashboard", fillable=True)

with ui.sidebar(open="open", bg="#f8f8f8"):
    with ui.accordion(id="acc", open="Section A"):
        
        with ui.accordion_panel("growth"):
            ui.input_select("var", "Select variable", choices=["total_bill", "tip"])

        with ui.accordion_panel("households"):
            "Section B content"

        with ui.accordion_panel("state"):
            "Section C content"

        with ui.accordion_panel("industry"):
            "Section D content"

        with ui.accordion_panel("nature"):
            "Section E content"


with ui.tooltip():
    icon("circle-info")
    "GDP comparisons using PPP are arguably more useful than those using nominal GDP when assessing the domestic market of a state because PPP takes into account the relative cost of local goods, services and inflation rates of the country, rather than using international market exchange rates, which may distort the real differences in per capita income. It is however limited when measuring financial flows between countries and when comparing the quality of same goods among countries.\n\nSource: Wikipedia"


@render.plot(alt="GDP (PPP current $) per capita.")
def gdp_ppp_plot():
    ax = gdp_plot()
    return ax


