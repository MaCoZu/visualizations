import numpy as np
import panel as pn
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

pn.extension(design="material", sizing_mode="stretch_width")


## LOGISTIC GROWTH
def logistic_growth(N0, r, K, t):
    t_vals = np.arange(t)
    N_vals = K / (1 + (K / N0 - 1) * np.exp(-r * t_vals))
    return t_vals, N_vals

# Initial parameters
N0_init = 5
r_init = 0.1
K_init = 100
t_init = 100

# Compute initial logistic growth data
t_values, N_values = logistic_growth(N0_init, r_init, K_init, t_init)

# Data source for Bokeh plot
source_log = ColumnDataSource(data={'t': t_values, 'N': N_values})

# Create Bokeh plot
plot_log = figure(
    height=300, 
    tools="save", 
    toolbar_location="right", 
    background_fill_color="snow"
    )
plot_log.line('t', 'N', source=source_log, line_width=2, line_color='darkmagenta')

# Update function for Bokeh plot
def update_log(N0, r, K, t):
    t_values, N_values = logistic_growth(N0, r, K, t)
    source_log.data = {'t': t_values, 'N': N_values}
    return plot_log

# Define widgets
N0_slider = pn.widgets.IntSlider(name='Initial population: $$N_0$$', start=1, end=1000, value=N0_init, step=1)
K_slider = pn.widgets.IntSlider(name='Carrying capacity', start=0, end=1000, value=K_init)
r_slider = pn.widgets.FloatSlider(name='Growth rate: $$r$$', start=0, end=1, value=r_init, step=0.001)
t_slider = pn.widgets.FloatSlider(name='Iterations', start=1, end=1000, value=t_init)

# Bind the update function to the widgets
logistic_log_plot = pn.bind(update_log, N0=N0_slider, r=r_slider, K=K_slider, t=t_slider)

## LOGISTIC MAP
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
source_map = ColumnDataSource(data={'x': np.arange(n_iter_init + 1), 'y': x_values})

plot_map = figure(
    x_axis_label='$$n$$', 
    y_axis_label='$$x_t$$', 
    height=300, 
    tools="save", 
    toolbar_location="right", 
    background_fill_color="snow"
    )
plot_map.line('x', 'y', source=source_map, line_width=2, line_color='darkmagenta')

# Update function for Bokeh plot
def update_map(x_t, R, n_iter):
    x_values = logistic_map(x_t, R, n_iter)
    source_map.data = {'x': np.arange(n_iter + 1), 'y': x_values}
    return plot_map

# Define widgets
x_t_slider = pn.widgets.FloatSlider(name='Initial $$x_t$$', start=0.0, end=1.0, value=x_t_init, step=0.000001)
R_slider = pn.widgets.FloatSlider(name='$$R$$', start=2, end=4.0, value=R_init, step=0.01)
n_slider = pn.widgets.IntSlider(name='Iterations', start=10, end=1000, value=n_iter_init)

# Bind the update function to the widgets
logistic_map_plot = pn.bind(update_map, x_t=x_t_slider, R=R_slider, n_iter=n_slider)


# Model selection
model_selection = pn.widgets.Select(name='Model', options=["Logistic Growth", "Logistic Map"])

# Explanation
explanation_log = pn.pane.Markdown(
    """The logistic growth model describes how a population grows more slowly as it approaches its carrying capacity.

    $$\\frac{dN}{dt} = rN \\left(1 - \\frac{N}{K}\\right)$$

    where:
    - $$N$$ is the population size
    - $$r$$ is the intrinsic growth rate
    - $$K$$ is the carrying capacity

    You can observe how the population evolves over time by adjusting the initial population, growth rate, and carrying capacity."""
)

explanation_map = pn.pane.Markdown(
    """The logistic map is a simplified version of a logistic (population) growth model with the effects of birth rate and death rate combined into one number, called $$R$$. The population size is replaced by a related concept called the “<em>fraction of carrying capacity</em>,” denoted as $$x$$.

    $$x_{t+1} = R x_t (1 - x_t)$$ 

    The logistic map equation is completely deterministic: every $$x_t$$ maps onto one and only one value of $$x_{t+1}$$. However, a change in the higher decimal places of $$x_0$$ can make $$x_t$$ unpredictable after around 30 iterations.

    You can observe this “<em>sensitive dependence on initial conditions</em>” by setting $$R \\approx 4$$ and trying different initial values of $$x_0$$ with small variations. Initially, the trajectories will be close, but after around 30 iterations, they will diverge significantly."""
)

# Function to update the layout based on the selected model
def update_layout(model):
    if model == "Logistic Growth":
        return pn.Column(
            plot_log,
            N0_slider, r_slider, K_slider, t_slider,
            explanation_log)
            
    elif model == "Logistic Map":
        return pn.Column(
            plot_map,
            x_t_slider, R_slider, n_slider,
            explanation_map
        )

# Bind the layout update function to the model selection
dashboard = pn.Column(
    model_selection,
    pn.bind(update_layout, model_selection)
)

# Display the dashboard
pn.template.EditableTemplate(
    editable=True,
    title="Growth Models",
    header_background="gray",
    logo="logo.svg",
    sidebar=[model_selection],
    main=[dashboard]
).servable()


