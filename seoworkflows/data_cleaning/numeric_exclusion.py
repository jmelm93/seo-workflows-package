def numeric_exclusion(data, numeric_exclusion_value, filter_col_name):
    if numeric_exclusion_value != "undefined" and numeric_exclusion_value != "" and numeric_exclusion_value != None and numeric_exclusion_value != 0:
        numeric_exclusion_value = str(numeric_exclusion_value)

        filter_VolumeLessThan = data[filter_col_name] > int(f"{numeric_exclusion_value}")
        data = data[filter_VolumeLessThan]

        return data
    
    else:
        return data