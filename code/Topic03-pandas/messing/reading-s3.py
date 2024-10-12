# demonstrate reading from S3 (anonymous )
# use
# pip install s3fs
# Author Andrew Beatty

import pandas as pd
import numpy as np


#remote_file = "s3://ncei-wcsd-archive/data/processed/SH1305/18kHz/SaKe2013-D20130523-T080854_to_SaKe2013-D20130523-T085643.csv"
remote_file = "s3://noaa-gsod-pds/2020/72278023183.csv"

workbookFileName = 's3Data.xlsx'


df = pd.read_csv(
    remote_file,
    storage_options={"anon": True},
)

# just to see what is in this file
df.to_excel(workbookFileName, sheet_name='phoenix', index=False)
print(df.head(1))

