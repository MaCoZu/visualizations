from functools import partial

import plotly.express as px
from shiny.express import input, render, ui
from shiny.ui import page_navbar
from shinywidgets import render_widget



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


@render_widget
def hist():
    fig = px.histogram(
        px.data.tips(),
        input.var(),
        color_discrete_sequence=["pink"],  # Set the color of the histogram bars
        template="simple_white",  # Set the background
    )

    return fig
