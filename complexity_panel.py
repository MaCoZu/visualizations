import numpy as np
import panel as pn
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

pn.extension(design="material", sizing_mode="stretch_width")

PRIMARY_COLOR = "#0072B5"
SECONDARY_COLOR = "#B54300"

# Logistic map function
def logistic_map(x, R, n):
    x_vals = [x]
    for _ in range(n):
        x = R * x * (1 - x)
        x_vals.append(x)
    return x_vals

# Initial parameters
x_t_init = 0.5
R_init = 3.5
n_iter_init = 50

# Compute initial logistic map data
x_values = logistic_map(x_t_init, R_init, n_iter_init)

# Create Bokeh plot
source = ColumnDataSource(data={'x': np.arange(n_iter_init + 1), 'y': x_values})

plot = figure(
    x_axis_label='$$n$$', 
    y_axis_label='$$x_t$$', 
    height=300, 
    tools="save", 
    toolbar_location="right", 
    background_fill_color="snow"
    )
plot.line('x', 'y', source=source, line_width=2, line_color='darkmagenta')

# Update function for Bokeh plot
def update_plot(x_t, R, n_iter):
    x_values = logistic_map(x_t, R, n_iter)
    source.data = {'x': np.arange(n_iter + 1), 'y': x_values}
    return plot

# Define widgets
x_t_slider = pn.widgets.FloatSlider(name='Initial $$x_t$$', start=0.0, end=1.0, value=x_t_init, step=0.000001)
R_slider = pn.widgets.FloatSlider(name='$$R$$', start=2, end=4.0, value=R_init, step=0.01)
n_slider = pn.widgets.IntSlider(name='Iterations', start=10, end=1000, value=n_iter_init)

# Bind the update function to the widgets
interactive_plot = pn.bind(update_plot, x_t=x_t_slider, R=R_slider, n_iter=n_slider)

# Display the dashboard
pn.template.EditableTemplate(
    editable=True,
    title="Logistic Map",
    header_background="gray",
    logo="logo.svg",
    sidebar_width=300,
    sidebar=[x_t_slider, R_slider, n_slider],
    main=[interactive_plot],
).servable()
