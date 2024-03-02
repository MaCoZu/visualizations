from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Statistics")

with ui.sidebar(open="closed", bg="#f8f8f8"): 
    TOPICS = {"topic": ["education", "jobs", "industry"]}
    ui.input_selectize("x", None, choices=TOPICS["topic"])
    ui.input_selectize("refinement1", None, choices=["Option1", "Option2"])
    ui.input_selectize("refinement2", None, choices=["OptionA", "OptionB", "OptionC"])


    @reactive.effect
    def _():
        choices = "upper" if input.uppercase() else "lower"
        ui.update_selectize("x", choices=CHOICES[choices])


"Stats"
with ui.main(): 
    # Placeholder for statistical chart
    ui.plotly_chart(None)

    # Placeholder for general stats boxes
    ui.div("Stat1", style="border: 1px solid black; padding: 10px; margin-bottom: 10px;")
    ui.div("Stat2", style="border: 1px solid black; padding: 10px; margin-bottom: 10px;")
    ui.div("Stat3", style="border: 1px solid black; padding: 10px; margin-bottom: 10px;")

    # Placeholder for table view
    ui.div("Table View", style="border: 1px solid black; padding: 10px; margin-bottom: 10px;")
