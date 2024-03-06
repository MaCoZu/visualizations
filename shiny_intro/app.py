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
from utils import gdp_plot

ui.page_opts(title="Sidebar layout", fillable=True)

with ui.sidebar(open="open", bg="#f8f8f8"):
    with ui.accordion(id="acc", open="Section A"):
        with ui.accordion_panel("work"):
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
    'hello'
    # metadata['Longdefinition']


@render.plot(alt="GDP (PPP current $) per capita.")
def plot():
    ax = gdp_plot()
    return ax
