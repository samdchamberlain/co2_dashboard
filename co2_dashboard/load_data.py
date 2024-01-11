import re
import gzip
import numpy as np
import pandas as pd
from typing import Optional, List

def get_variable_vals(fields: List[str]) -> dict:
    ''' Extract the co2, temp, and rh values by string matching
      and export row as dictionary
    '''
    vars = ["ppm", "temp", "rh"]
    var_dict = {key: None for key in vars}
    for var in var_dict:
        final = [field for field in fields if var in field]
        final_val = re.sub(r'[^0-9 .-]', '', final[0]).strip()
        var_dict[var] = final_val
    return var_dict


def load_raw_data_to_df(frequency: Optional[int] = 600) -> pd.DataFrame:
	# Loads data from log file to Pandas df
	print(f"Loading and aggregating index at {frequency}...")
	co2_list, rh_list, temp_list = [], [], []
	with gzip.open("data/scd30Log.log.gz", mode='rt', encoding='UTF-8') as f:
	    for line in f:
	        if line.startswith("INFO:root:CO2"):
	            fields = (
	                line.replace("INFO:root:CO2:", "")
	                .strip()
	                .split(',')
	            )
	            var_dict = get_variable_vals(fields)

	            co2_list.append(var_dict.get('ppm'))
	            temp_list.append(var_dict.get('temp'))
	            rh_list.append(var_dict.get('rh'))

	df = pd.DataFrame(
		{
		    "temp": temp_list,
		    "rh": rh_list,
		    "co2": co2_list
		}
	).reset_index().astype(float)
	df.rename(columns={'index': 'raw_timestamp'}, inplace=True)
	print(f"Data loaded to dataframe of len {df.shape[0]}")

	# Aggregate to smaller frequency
	df['timestamp'] = df['raw_timestamp'] // frequency
	agg_df = df.groupby('timestamp')[['co2', 'rh', 'temp']].mean().reset_index()
	print(f"Data aggregated to dataframe of len {agg_df.shape[0]}")
	return agg_df