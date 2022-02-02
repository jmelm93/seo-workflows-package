def grouped_gsc(df, groupby_list: list, round_decimals: int = None):
    output = (df.groupby(groupby_list)
    .agg({"clicks": "sum",
        "impressions": "sum",
        "ctr" : "mean",
        "position":["size","max","min","mean"]})
    .reset_index()
    .pipe(lambda x: x.set_axis([f'{a}' if b == '' else f'{a}_{b}' for a,b in x.columns], axis=1, inplace=False))
    .round(round_decimals))
    return output