""" 
This file was created when following the quickstart tutorial by Backtrader at https://www.backtrader.com/docu/quickstart/quickstart/
 """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
#import os.path  # To manage paths
#import sys  # To find out the script name (in argv[0])

from strategies import TestStrategy3 as TestStrategy

# Import the backtrader platform
import backtrader as bt

if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    #cerebro.addstrategy(TestStrategy)
    # Add a strategy
    strats = cerebro.optstrategy(
        TestStrategy,
        maperiod=range(10, 31))

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    datapath = 'data/orcl-1995-2014.txt'

    # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2000, 12, 31),
        reverse=False)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(1000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    # Set the commission - 0.1% ... divide by 100 to remove the %
    cerebro.broker.setcommission(commission=0.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run(maxcpus=1)

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    #cerebro.plot(path="./plot")