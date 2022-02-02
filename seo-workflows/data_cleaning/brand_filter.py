import logging
import sys
sys.path.insert(0, '..')

def brand_filter(data, brand_variants, filter_col_name):
    logging.debug(f"brand_variants = {brand_variants}")
    if brand_variants != "undefined" and brand_variants != "" and brand_variants != None and brand_variants != "None":
        logging.debug(f'PASSED: brand_variants != "undefined" and brand_variants != "" and brand_variants != None')

        if type(brand_variants) == list:
            brand_variants = "|".join(brand_variants)
        else:
            pass

        brand_variants = str(brand_variants)
        
        mask = ~data[filter_col_name].str.contains(f"{brand_variants}", case = False, regex=True)
        data = data[mask]
        
        return data

    else:
        return data