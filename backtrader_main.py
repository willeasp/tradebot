""" This file is used when running strategies from strategies.py  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import pandas
#import os.path  # To manage paths
#import sys  # To find out the script name (in argv[0])

# from backtrader.strategies.sma_crossover import MA_CrossOver as Strategy
from strategies import DefaultStrategy as Strategy


# Import the backtrader platform
import backtrader as bt

if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    optimizer = False

    if optimizer:
        # Add a strategy
        strats = cerebro.optstrategy(
            Strategy,
            maperiod=range(3, 10),
            printlog=False,
            daysofrisingma=range(2, 5),
            daysofdroppingma=range(2, 5)
        )
    else:
        # Add a strategy
        cerebro.addstrategy(
            Strategy,
            maperiod=9,
            daysofrisingma=4,
            daysofdroppingma=3
        )


    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    datapath = 'data/extended_intraday_IBM_15min_year1month2_adjusted.csv'

    # Create a Data Feed
    # data = bt.feeds.YahooFinanceCSVData(
    #     dataname=datapath,
    #     # Do not pass values before this date
    #     fromdate=datetime.datetime(2020, 11, 17),
    #     # Do not pass values after this date
    #     todate=datetime.datetime(2020, 12, 14),
    #     reverse=False)

    dataframe = pandas.read_csv(datapath,
                                parse_dates=True,
                                index_col=0)

    data = bt.feeds.PandasData(
        dataname=dataframe
    )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(10000000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    # Set the commission - 0.1% ... divide by 100 to remove the %
    cerebro.broker.setcommission(commission=0.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run(maxcpus=1, runonce=False)

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    if not optimizer:
        cerebro.plot(path="./plot")