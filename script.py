# Import sys module
import sys
import numpy as np
import pandas as pd

# Get the file name from the command line argument
file_name = sys.argv[1]

# Read in the file
df = pd.read_csv(file_name)

phone_numbers = ['phone_1', 'phone_2', 'phone_3']
# remove phone numbers that are marked DO NOT CALL
df['phone_2'] = np.where(df['phone_2_do_not_call'] == 'DO NOT CALL', np.nan, df['phone_2'])
df['phone_3'] = np.where(df['phone_3_do_not_call'] == 'DO NOT CALL', np.nan, df['phone_3'])
df['phone_1'] = np.where(df['phone_1_do_not_call'] == 'DO NOT CALL', np.nan, df['phone_1'])

# drop rows where all three phone numbers are missing
out = df.loc[df[phone_numbers].dropna(axis=0, how='all').index]

# save out to a new file
out.to_csv('output.csv', index=False)
