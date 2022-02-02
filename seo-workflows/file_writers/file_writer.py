import pandas as pd
from datetime import datetime
import io
import logging

date = datetime.today().strftime('%Y-%m-%d')
time_of_day = datetime.today().strftime('%H:%M')

def with_proper_col_widths(filename, dict_of_dfs):
    file_name = f"seoworkflows_{filename}_{date}-{time_of_day}.xlsx"
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter', engine_kwargs={'options': {'strings_to_urls': False}})
    for sheetname, df in dict_of_dfs.items():  # loop through `dict` of dataframes
        df.to_excel(writer, sheet_name=sheetname, index=False)  # send df to writer
        worksheet = writer.sheets[sheetname]  # pull worksheet object
        for idx, col in enumerate(df):  # loop through all columns
            series = df[col]
            max_len = max((
                series.astype(str).map(len).max(),  # len of largest item
                len(str(series.name))  # len of column name/header
                )) + 1  # adding a little extra space
            ### Below sets the max width to 70 - so they don't get overly long!
            if max_len < 70:
                worksheet.set_column(idx, idx, max_len)  # set column width
            else: 
                worksheet.set_column(idx, idx, 70)
    writer.save()
    return writer




def bytes_writer_with_proper_col_widths(filename, dict_of_dfs):
    buffer = io.BytesIO()
    writer = pd.ExcelWriter(buffer, engine='xlsxwriter', engine_kwargs={'options': {'strings_to_urls': False}})    
    logging.debug(f'Withing `bytes_writer_with_proper_col_widths` function')
    for sheetname, df in dict_of_dfs.items():  # loop through `dict` of dataframes
        logging.debug(f'for loop to create sheets')
        df.to_excel(writer, sheet_name=sheetname, index=False)  # send df to writer
        worksheet = writer.sheets[sheetname]  # pull worksheet object
        for idx, col in enumerate(df):  # loop through all columns
            series = df[col]
            max_len = max((
                series.astype(str).map(len).max(),  # len of largest item
                len(str(series.name))  # len of column name/header
                )) + 1  # adding a little extra space
            ### Below sets the max width to 70 - so they don't get overly long!
            if max_len < 70:
                worksheet.set_column(idx, idx, max_len)  # set column width
            else: 
                worksheet.set_column(idx, idx, 70)
    writer.save()
    # data contains the binary data of excel file. 
    # For instance, you can use requests module to upload file somewhere.
    data = buffer.getvalue()
    file_size = buffer.tell()
    file_size_mb = round(file_size * 0.000001,2)
    logging.debug(f'File Size: {file_size_mb}mb')
    file_name = f"seoworkflows_{filename}_{date}-{time_of_day}.xlsx"
    file_dict = {file_name: data}
    return file_dict
