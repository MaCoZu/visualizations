import numpy as np
import panel as pn
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

pn.extension('mathjax', 'TooltipIcon')
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
    x_axis_label='$$t$$',
    y_axis_label='$$x_t$$',
    # height=300,
    tools="save",
    toolbar_location="right",
    background_fill_color="snow")
plot_log.line('t',
              'N',
              source=source_log,
              line_width=2,
              line_color='darkmagenta')

plot_log.xaxis.axis_label_text_font_size = "16pt"
plot_log.yaxis.axis_label_text_font_size = "18pt"


# Update function for Bokeh plot
def update_log(N0, r, K, t):
  t_values, N_values = logistic_growth(N0, r, K, t)
  source_log.data = {'t': t_values, 'N': N_values}


# Define widgets
N0_slider = pn.widgets.IntSlider(name='Initial population: $$N_0$$',
                                 start=1,
                                 end=1000,
                                 value=N0_init,
                                 step=1)

K_slider = pn.widgets.IntSlider(name='Carrying capacity',
                                start=0,
                                end=1000,
                                value=K_init)

r_slider = pn.widgets.FloatSlider(name='Growth rate: $$r$$',
                                  start=0,
                                  end=1,
                                  value=r_init,
                                  step=0.001)

t_slider = pn.widgets.FloatSlider(name='Iterations',
                                  start=1,
                                  end=1000,
                                  value=t_init)

# Bind the update function to the widgets
logistic_log_plot = pn.bind(update_log,
                            N0=N0_slider,
                            r=r_slider,
                            K=K_slider,
                            t=t_slider)


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
source_map = ColumnDataSource(data={
    'x': np.arange(n_iter_init + 1),
    'y': x_values
})

plot_map = figure(
    x_axis_label='$$t$$',
    y_axis_label='$$x_t$$',
    tools="save",
    # toolbar_location="right",
    background_fill_color="snow")
plot_map.line('x',
              'y',
              source=source_map,
              line_width=2,
              line_color='darkmagenta')

plot_map.xaxis.axis_label_text_font_size = "16pt"
plot_map.yaxis.axis_label_text_font_size = "18pt"


# Update function for Bokeh plot
def update_map(x_t, R, n_iter):
  x_values = logistic_map(x_t, R, n_iter)
  source_map.data = {'x': np.arange(n_iter + 1), 'y': x_values}


# Define widgets
x_t_slider = pn.widgets.FloatSlider(name='Initial $$x_t$$',
                                    start=0.0,
                                    end=1.0,
                                    value=x_t_init,
                                    step=0.000001)

R_slider = pn.widgets.FloatSlider(name='$$R$$',
                                  start=2,
                                  end=4.0,
                                  value=R_init,
                                  step=0.01)

n_slider = pn.widgets.IntSlider(name='Iterations',
                                start=10,
                                end=1000,
                                value=n_iter_init)

# Bind the update function to the widgets
logistic_map_plot = pn.bind(update_map,
                            x_t=x_t_slider,
                            R=R_slider,
                            n_iter=n_slider)

stylesheet = """
div.bk-input-group label {
    font-size:20px;
    margin: -0.3rem 0.5rem;
}

div.bk-input-group select#input.bk-input option {
    font-size:18px;
    line-height:2em;
    margin:7px;
}
"""

explanation_css = """
.explanation {font-size: 15px;}
"""

# Explanation
explanation_log = pn.pane.Markdown("""
    <div class="explanation">
    The logistic growth model describes how a population grows more slowly as it approaches its carrying capacity.

    $$\\frac{dN}{dt} = rN \\left(1 - \\frac{N}{K}\\right)$$

    where:
    - $$N$$ is the population size
    - $$r$$ is the intrinsic growth rate
    - $$K$$ is the carrying capacity

    You can observe how the population evolves over time by adjusting the initial population, growth rate, and carrying capacity.""",
                                   stylesheets=[explanation_css])

explanation_map = pn.pane.Markdown("""
    <div class="explanation">
    The logistic map is simplified version of a logistic (population) growth model with the effects birth rate and death rate combined into one number, called $$R$$. While population size is replaced by a related concept, called “<em>fraction of carrying capacity</em>,” denominated $$x$$.

    $$x_{t+1} = R x_t (1 - x_t)$$

    The logistic map equation is completely deterministic, every $$x_t$$ maps onto one and only one value of $$x_t+1$$. Still a change in the higher decimal places of $$x_0$$ can make $$x_t$$ <em>unpredictable</em> at $$t \approx 30$$.

    You can observe this “<em>sensitive dependence on initial conditions</em>” by setting $$R \approx 4$$ and trying different initial values of $$x_0$$ with small variations. Initially, the trajectories will be close, but after around 30 iterations, they will diverge significantly.

    The map might fall into a fixed point (e.g. $$R=2, x_0=0.5$$), a fixed cycle/oscillation (e.g. $$R=3.1, x_0=0.2$$, or chaos. Fixed points and fixed cycles are called “<em>attractors</em>” since any initial condition will eventually be attracted to it. When $$R$$ increases the trajectories fluctuate more and more, between $$R=3.4$$ and $$R=3.5$$ the system oscillates among four different values, with growing $$R$$ the values the system oscillates between double fast until they are infinite at approximately $$R=3.569946$$.

    Before this point the logistic map was roughly predictable, after the values of $$x$$ become <em>chaotic</em>. And very small changes in $$x_0$$ lead to widely diverging trajectories.

    You can observe this “<em>sensitive dependence on initial conditions</em>” by setting $$R \\approx 4$$ and trying different $$x_0$$ with small variations, say $$x_0=0.2$$ and $$x_0=0.2000001$$. They will start off very close to one another but after 30 or so iterations they begin to diverge significantly, and soon after there is no correlation between them.

    The corollary is this: since we can never know the initial conditions of $$x_0$$ to infinitely many decimal places <strong>perfect prediction is impossible</strong>.</div>""",
                                   stylesheets=[explanation_css])

# LOG GROWTH PANE
log_growth_pane = pn.GridSpec(
    sizing_mode='stretch_both',
    min_height=700,
)
log_growth_pane[0:1, :18] = pn.Spacer(styles=dict(background='white'))
log_growth_pane[1:7, 1:11] = plot_log
log_growth_pane[8:12, 3:9] = pn.Column(N0_slider, r_slider, K_slider, t_slider)
log_growth_pane[1:12, 12:17] = explanation_log

# LOG MAP PANE
log_map_pane = pn.GridSpec(
    sizing_mode='stretch_both',
    min_height=700,
)
log_map_pane[0:1, :18] = pn.Spacer(styles=dict(background='white'))
log_map_pane[1:7, 1:11] = plot_map
log_map_pane[8:12, 3:9] = pn.Column(x_t_slider, R_slider, n_slider)
log_map_pane[1:12, 12:17] = explanation_map

# Model selection
model_selection = pn.widgets.Select(
    name='Model',
    options=["Logistic Map", "Logistic Growth"],
    size=10,
    stylesheets=[stylesheet])


# Function to update the layout based on the selected model
def update_layout(model):
  if model == "Logistic Growth":
    return log_growth_pane

  elif model == "Logistic Map":
    return log_map_pane


# Bind the layout update function to the model selection
dashboard = pn.bind(update_layout, model_selection)

# Display the dashboard
pn.template.EditableTemplate(editable=True,
                             title="Growth Models",
                             header_background="teal",
                             logo="logo.svg",
                             sidebar=[model_selection],
                             sidebar_width=250,
                             collapsed_sidebar=True,
                             main=[dashboard]).servable()
