import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn-v0_8-darkgrid')

# create dates using datetime
dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle='solid')
# get current figure, formating the dates labels in x-axis
plt.gcf().autofmt_xdate()

# change the way dates are presented to month, day year
date_format = mpl_dates.DateFormatter('%b, %d %Y')
# get current axis
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()

plt.show()
