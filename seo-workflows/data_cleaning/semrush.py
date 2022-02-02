import sys
sys.path.insert(0, '..')

from seoworkflows_lib.data_cleaning.url_cleaning_helpers import *
from seoworkflows_lib.data_cleaning.semrush_mods_helpers import *


def semrush_analysis_cols(df):
    """The semrush_analysis_cols() function takes in a DataFrame of SEMRush data and returns a new DataFrame.
    Returns: A dataframe with the following columns added:
        - Position_Range
        - Top20
        - Traffic_Exists
        - Traffic_Rank
        - Domain
    """
    domain_name = get_domains_helper(input=df['URL']) 
    data = (
        df.assign(
                Position_Range=df["Position"].apply(position_range_helper),
                Top20=df["Position"].apply(top20_helper),
                Traffic_Exists=df["Traffic"].apply(traffic_exists_helper),
                Traffic_Rank=df["Traffic"].rank(ascending = False).astype(int),
                Domain=domain_name
                )
            .sort_values(by='Traffic', ascending=False)
            )
    data = data[['URL','Domain','Keyword', 'Position', 'Previous position', 'Search Volume', 'Keyword Difficulty', 'CPC', 'Traffic', 'Traffic (%)', 'Traffic Cost', 'Competition', 'Number of Results', 'Trends', 'Timestamp', 'SERP Features by Keyword', 'Keyword Intents', 'Position_Range', 'Top20', 'Traffic_Exists', 'Traffic_Rank', ]]

    return data

