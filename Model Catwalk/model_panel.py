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
N0_init, r_init, K_init, t_init = 5, 0.1, 100, 100

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
    background_fill_color="snow",
    sizing_mode='stretch_width',
)
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
  return plot_log


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
interactive_log_plot = pn.bind(update_log,
                               N0=N0_slider,
                               r=r_slider,
                               K=K_slider,
                               t=t_slider)

widgets = pn.Column(N0_slider,
                    r_slider,
                    K_slider,
                    t_slider,
                    sizing_mode="fixed",
                    min_width=500)

log_pane = pn.Column(
    interactive_log_plot,
    widgets,
)

# Display the dashboard
pn.template.EditableTemplate(
    editable=True,
    title="Growth Models",
    header_background="teal",
    logo="logo.svg",
    #  sidebar=[N0_slider, r_slider, K_slider, t_slider],
    sidebar_width=250,
    collapsed_sidebar=True,
    main=[log_pane]).servable()
