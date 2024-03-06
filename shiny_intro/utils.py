import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import wbgapi as wb

# get region names
region_df = wb.region.info()
region_df = pd.DataFrame(region_df.items)

def get_region(code, df):
    region = df.loc[df['code'] == code, 'name'].iloc[0]
    return region

# get gdp df
def get_gdp_df():
    pd.options.display.float_format = '{:,.2f}'.format

    indicator_code = "NY.GDP.PCAP.PP.CD"
    gdp_ppp = wb.data.DataFrame(indicator_code, 
                                ['AFR',
                                'MEA', 
                                'NAC',
                                'EUU',
                                'SAS',
                                ],
                                range(1990, 2024, 1)) 



    # clean Year from 'YR2018' to '2018'
    gdp_ppp.columns = [col.replace("YR", "") for col in gdp_ppp.columns]
    gdp_ppp.reset_index(inplace=True)

    # chartable data format
    df = gdp_ppp.melt(
        id_vars="economy", var_name="Year", value_name="gdp (ppp) per capita"
    ).sort_values("economy")

    # rename cols
    df.columns = ["Economy", "Year", "GDP (PPP) per capita"]

    return df



def get_metadata():
    indicator_code = "NY.GDP.PCAP.PP.CD"
    metadata = wb.series.metadata.get(indicator_code) # load metadata
    return metadata


region_df = pd.DataFrame(wb.region.info().items)
# rename region code to propper region name
def get_region(code):
    region = region_df.loc[region_df['code'] == code, 'name'].iloc[0]
    return region



def gdp_plot():
    df = get_gdp_df()
    ax = sns.lineplot(
        data=df.sort_values("Year"),
        x="Year",
        y="GDP (PPP) per capita",
        hue="Economy",
        palette="bright",
    )

    # Customize plot
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    spine_width = 0.5

    for spine in ax.spines.values():
        spine.set_linewidth(spine_width)
    ax.tick_params(axis="both", width=spine_width)
    for ind, label in enumerate(ax.get_xticklabels()):
        label.set_visible(ind % 5 == 0)

    # Get handles and labels for the legend
    handles, labels = ax.get_legend_handles_labels()

    # Replace region codes with region names in legend labels
    for i, label in enumerate(labels):
        region_name = get_region(label)
        labels[i] = region_name

    # Update legend with modified labels
    ax.legend(
        handles,
        labels,
        loc="best",
        fontsize="small",
        frameon=False,
        fancybox=False,
    )

    ax.set_title("GDP (PPP current $) per capita.")
    ax.set_xlabel("Year")
    ax.set_ylabel("")
    return ax

