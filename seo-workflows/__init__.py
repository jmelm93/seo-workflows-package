__version__ = '0.0.1'

import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, TypeVar, Optional
# from logger import setup_logging # Import and call custom logger
# setup_logging()

PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')

def send_email(subject_line, content):
    from send_email.sendgrid import send_email
    send_email(subject_line=subject_line, content=content)


def send_gmail(email_from, email_list_to, email_password, subject, message, attachment="No Attachment"):
    from send_email.gmail import send_gmail
    send_gmail(email_from=email_from, email_to_list=email_list_to, email_password=email_password, subject=subject, message=message, attachment=attachment)

def send_error_notification_email(tool_name, error_message, uid):
    from send_email.gmail import error_notification_email
    error_notification_email(tool_name=tool_name, error_message=error_message, uid=uid)


@dataclass
class CustomJoins:
    full_values: list
    matching_criteria: list

    def partial_match_join_first_match_returned(self):
        from data_cleaning import partial_match_join_first_match_returned
        output = partial_match_join_first_match_returned(full_values=self.full_values, matching_criteria=self.matching_criteria)
        final = pd.concat(output)
        return final

    def partial_match_join_all_matches_returned(self):
        from data_cleaning import partial_match_join_all_matches_returned
        output = partial_match_join_all_matches_returned(full_values=self.full_values, matching_criteria=self.matching_criteria)
        final = pd.concat(output)
        return final


@dataclass
class NgramAnalysis:
    input_list: list
    ngram_type: str
    characters: int

    """
        The url_ngrams() function takes a series of URLs and select imputs and 
        returns ngrams and ngram frequencies in a dataframe.

        Parameters
        ----------
        characters: int 
            int of '1' for unigram, '2' for bigram, etc...
        ngram_type: str 
            str that'll be returned in 'ngram_type' column
        input_series: series
            series that contains urls

        Returns
        -------
        A dataframe with 4 columns: 'ngram', 'frequency', 'type', 'ngram_cleaned' 

    """

    def url_ngrams(self):
        from data_cleaning import url_ngrams
        final = url_ngrams(input_list=self.input_list, ngram_type=self.ngram_type, characters=self.characters)
        return final

    def query_ngrams(self):
        from data_cleaning import query_ngrams
        final = query_ngrams(input_list=self.input_list, ngram_type=self.ngram_type, characters=self.characters)
        return final
@dataclass
class UrlCleaning:
    url_list: list

    """
    A class for cleaning series objects of urls.

    Parameters
    ----------
    url_list : list
        Urls for data cleaning.

    Methods
    -------
    get_url_path():
        Takes a Url list and returns the input URLs + URL paths.

    get_domain():
        Takes a Url list and returns the input URLs + domain

    get_url_parts():
        Takes a Url list and returns all URL parts (<scheme>://<netloc>/<path>;<params>?<query>).

    get_path_and_directories():
        Takes a Url list and returns the path and directories (directories are in single sell list).

    get_all_directories_1_per_row():
        Takes a Url list and returns the path and directories (1 directory per column - duplicating the path).
    """
    
    def get_url_path(self):
        from data_cleaning import get_url_path # No timers on all below as conflicts with ngram timers
        final = get_url_path(url_list=self.url_list)
        return final

    def get_domain(self):
        from data_cleaning import get_domain # No timers on all below as conflicts with ngram timers
        final = get_domain(url_list=self.url_list)
        return final

    def get_url_parts(self):
        from data_cleaning import get_url_parts # No timers on all below as conflicts with ngram timers
        final = get_url_parts(url_list=self.url_list)
        return final

    def get_path_and_directories(self):
        from data_cleaning import get_path_and_directories # No timers on all below as conflicts with ngram timers
        final = get_path_and_directories(url_list=self.url_list)
        return final

    def get_all_directories_1_per_row(self):
        from data_cleaning import get_all_directories_1_per_row # No timers on all below as conflicts with ngram timers
        final = get_all_directories_1_per_row(url_list=self.url_list)        
        return final



@dataclass
class CustomExcelWriter:
    filename: str
    dict_of_dfs: Dict[str, PandasDataFrame]

    """
    A class for cleaning series objects of urls.

    Parameters
    ----------
    filename : list
        Name for output .xlsx file (without the .xlsx extension).
    
    dict_of_dfs : Dict[str, pandas.core.frame.DataFrame]
        Dict of {'sheet_name': Dataframe}

    Methods
    -------
    excel_writer_with_proper_col_widths():
        Takes a ____ and ____  and returns the Excel File with proper col widths.

    excel_bytes_writer_with_proper_col_widths():
        Takes a ____ and ____  and returns the Excel File in bytes format with proper col widths.

    """
    def excel_writer_with_proper_col_widths(self):
        from file_writers import with_proper_col_widths # No timers on all below as conflicts with ngram timers
        final = with_proper_col_widths(filename=self.filename, dict_of_dfs=self.dict_of_dfs)        
        return final

    def excel_bytes_writer_with_proper_col_widths(self):
        from file_writers import bytes_writer_with_proper_col_widths # No timers on all below as conflicts with ngram timers
        final = bytes_writer_with_proper_col_widths(filename=self.filename, dict_of_dfs=self.dict_of_dfs)        
        return final

@dataclass
class BrandedKeywordFilter:
    data: PandasDataFrame
    brand_variants: str
    filter_col_name: str

    def brand_filter(self):
        from data_cleaning import brand_filter
        final = brand_filter(data=self.data, brand_variants=self.brand_variants, filter_col_name=self.filter_col_name)        
        return final 

@dataclass
class NumericValueFilter:
    data: PandasDataFrame
    numeric_exclusion_value: int
    filter_col_name: str

    def numeric_exclusion(self):
        from data_cleaning import numeric_exclusion
        final = numeric_exclusion(data=self.data, numeric_exclusion_value=self.numeric_exclusion_value, filter_col_name=self.filter_col_name)        
        return final 

@dataclass
class SEMRushDataCleaning:
    data: PandasDataFrame
    search_volume_exclusions: int
    brand_variants: str
    volume_filter_col_name:  Optional[str] = field(default="Search Volume") # default value if none provided as arguments
    keyword_filter_col_name: Optional[str] = field(default="Keyword") # default value if none provided as arguments

    def semrush_analysis_cols(self):
        from data_cleaning import semrush_analysis_cols
        volume_excl_df = NumericValueFilter(data=self.data, numeric_exclusion_value=self.search_volume_exclusions, filter_col_name=self.volume_filter_col_name).numeric_exclusion()
        brand_excl_df = BrandedKeywordFilter(data=volume_excl_df, brand_variants=self.brand_variants, filter_col_name=self.keyword_filter_col_name).brand_filter()
        final = semrush_analysis_cols(df=brand_excl_df)  
        return final




