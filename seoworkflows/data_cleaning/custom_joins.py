def partial_match_join_first_match_returned(full_values, matching_criteria):
    """The partial_match_join_first_match_returned() function takes two series objects and returns a dataframe with the first matching value.
    Args:
        full_values = None: This is the series that contains the full values for matching pair.
        partial_values = None: This is the series that contains the partial values for matching pair.
    Returns:
            A dataframe with 2 columns - 'full' and 'match'.  
    """

    matching_criteria = matching_criteria.to_frame("match")
    full_values = full_values.to_frame("full").drop_duplicates() 

    output=[]
    for n in matching_criteria['match']:
        mask = full_values['full'].str.contains(n, case=False, na=False)
        df = full_values[mask]
        df_copy = df.copy()
        df_copy['match'] = n 
        # leaves us with only the 1st of each URL
        df_copy.drop_duplicates(subset=['full'])
        output.append(df_copy)

    return output


def partial_match_join_all_matches_returned(full_values, matching_criteria):
    """The partial_match_join_first_match_returned() function takes two series objects and returns a dataframe with all matching values (duplicating the full value).
    Args:
        full_values = None: This is the series that contains the full values for matching pair.
        partial_values = None: This is the series that contains the partial values for matching pair.
    Returns:
            A dataframe with 2 columns - 'full' and 'match'.  
    """
    
    matching_criteria = matching_criteria.to_frame("match")
    full_values = full_values.to_frame("full")

    full_values = full_values.drop_duplicates() 
    
    output=[]

    # import numpy as np
    # match_array = np.array(matching_criteria['match'])
    # full_values_array = np.array(full_values['full'])
    # mask = np.isin(full_values_array, match_array)
    # print(mask)


    for n in matching_criteria['match']:
        mask = full_values['full'].str.contains(n, case=False, na=False)
        df = full_values[mask]
        df_copy = df.copy()
        df_copy['match'] = n 
        output.append(df_copy)

    # final = pd.concat(output)

    return output