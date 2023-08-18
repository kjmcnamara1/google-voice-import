import pandas as pd
import pytz

"Aug 7, 2023 13:55:11"

"Timestamp Now"
pd.Timestamp.now(tz="US/Central").tz_convert("UTC")
pd.Timestamp.now()

print()
"Message Timestamp"
pd.Timestamp(1691434511000, unit="ms", tz="UTC")
pd.Timestamp(1691434511000, unit="ms", tz="UTC").tz_convert("US/Central")
pd.Timestamp(1691434511000, unit="ms", tz="UTC").tz_convert("US/Central").value / 1e6


pytz.all_timezones
