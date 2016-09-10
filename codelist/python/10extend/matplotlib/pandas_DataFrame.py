%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import datetime
pd.date_range("2015-1-1", periods=31)

pd.date_range(datetime.datetime(2015,2,1), periods=31)

pd.date_range("2015-1-1 00:00", "2015-1-1 12:00", freq="H")

ts1 = pd.Series(np.arange(31), index=pd.date_range("2015-1-1", periods=31))
print ts1

ts1.index[4].year, ts1.index[4].month, ts1.index[4].day

ts2 = pd.Series(np.random.rand(2), index=[datetime.datetime(2015,1,1), datetime.datetime(2015,2,1)])
ts2

#df1 = pd.read_csv("temperature_outdoor_2014.tsv", delimiter="\t", encoding="utf-8", names=["time","outdoortemp"])
#df2 = pd.read_csv("temperature_indoor_2014.tsv", delimiter="\t", encoding="utf-8", names=["time","indoortemp"])

#df1.time = (pd.to_datetime(df1.time.values, unit="s").tz_localize("UTC").tz_convert("Europe/Stockholm"))
#df1 = df1.set_index("time")
#df1.head()


#fig, ax = plt.subplots(1, 1, figsize=(12, 4))
#df1.plot(ax=ax)
#df2.plot(ax=ax)

#fig.tight_layout()
#fig.savefig("ch4-time-temperature-2014.pdf")


fig, axes = plt.subplots(1,2,figsize=(12,4))

df_month.plot(kind="bar", ax=axes[0])
df_month.plot(kind="box", ax=axes[1])

fig.tight_layout()
fig.savefig("ch4-time-temperature-2014-allmonths.pdf")