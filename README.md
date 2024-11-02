# Visualizations

Exploration of the widely used charting libraries. So far matplotlib, seaborn, plotly, holoviews and D3 charts. The notebooks start from the basics and fastly progress to the minutiae that pop up when creating nice visualizaions. 

For example in the notebooks you'll find:

**matplotlib**: 
- changing the defaults rcParams, styles like `ggplot`
- subplots, secondary axis
- Scatterplot with trendline
- Barplots grouped/horizontal, inside lables, confinded axis
- Histogramms, Bins, Pie Charts
- Frames and Axis
- Colors: BASE_COLORS, TABLEAU_COLORS, CSS4_COLORS, XKCD_COLORS

**seaborn**
- styles & context
- formatting lables
- Relplot: confidence interval, subgraphs
- changing the lable format in sns
- fixing axis lables
- color palettes


## Primary uses for data visualization:
- to explore, reveal and communicate data effectively
- provide the reader with important, meaningful, and useful insight

## Tufte's Graphical Excellence:
> Excellence in statistical grahics consists of complex ideas communicated with clarity, precision and efficiency. 

__Graphical display should:__
- show the data
- induce the viewer to think about the substance rather than about methodology, graphic design, the technology of grahpic production, or something else
- avoid distorting what the data have to say
- present many numbers in a small space
- make large number sets coherent
- encourage the eye to compare different pieces of data
- reveal the data at several levels of detail, from a broad overview to the fine structure
- serve a reasonable clear purpose: description, exploration, tabulation, or decoration
- be closely integrated with the statistical and verbal descriptions of  a data set. 

__Design for the human brain:__
- Length on an aligned scale may be the best option to compare numbers accurately
- Color hue is a good way of encoding categorical data. 
- Vertical columns often work well when few items are being compared, while horizontal bars may be a better option when there are many items to compare
- Sacrosanct rule with bar and column charts: Because they rely on the length of the bars to encode data, you must start the bars at zero.