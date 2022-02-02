import logging
import sys
sys.path.insert(0, '..')

def numeric_exclusion(data, numeric_exclusion_value, filter_col_name):

    logging.debug(f"numeric_exclusion_value = {numeric_exclusion_value}")
    if numeric_exclusion_value != "undefined" and numeric_exclusion_value != "" and numeric_exclusion_value != None and numeric_exclusion_value != 0:
        logging.debug(f'PASSED: numeric_exclusion_value != "undefined" and numeric_exclusion_value != "" and numeric_exclusion_value != None')
        numeric_exclusion_value = str(numeric_exclusion_value)

        filter_VolumeLessThan = data[filter_col_name] > int(f"{numeric_exclusion_value}")
        data = data[filter_VolumeLessThan]

        return data
    
    else:
        return data