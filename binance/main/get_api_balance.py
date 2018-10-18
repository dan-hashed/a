import dateparser
import datetime
import json
import os
import pytest
import requests_mock

from datetime import datetime
from pandas import DataFrame

from binance.client import Client
from binance.exceptions import BinanceWithdrawException

API_KEY = os.environ.get('BINANCE_API_KEY')
API_SECRET = os.environ.get('BINANCE_API_SECRET')

client = Client(API_KEY, API_SECRET)

def test_withdraw_api_exception():
    """Test Withdraw API response Exception"""

    with pytest.raises(BinanceWithdrawException):

        with requests_mock.mock() as m:
            json_obj = {"success": False, "msg": "Insufficient funds"}
            m.register_uri('POST', requests_mock.ANY, json=json_obj, status_code=200)
            client.withdraw(asset='BTC', address='BTCADDRESS', amount=10000)


if __name__ == '__main__':
    try:
        client.test_withdraw_api_exception()
    except:
        pass
        # mail me

    info = client.get_account()
    balance = DataFrame(info['balance'])
    today = datetime.datetime.now().strftime('%Y%m%d')
    balance.to_csv(f'balance_binance_{today}.csv', index=False)
    # change to to_sql later
    


# FYI

# ## Get account info
# info = client.get_account()
# # info sample: {'makerCommission': 10, 'takerCommission': 10, 'buyerCommission': 0, 'sellerCommission': 0, 'canTrade': True, 'canWithdraw': True, 'canDeposit': True, 'updateTime': 1539154766316, 'balances': []}

# ## Get asset balance
# balance = client.get_asset_balance(asset='BTC')

# ## Get account status
# status = client.get_account_status()

# ## Get trades
# trades = client.get_my_trades(symbol='BNBBTC')

# ## Get trade fees
# # get fees for all symbols
# fees = client.get_trade_fee()

# # get fee for one symbol
# fees = client.get_trade_fee(symbol='BNBBTC')

# ## Get asset details
# details = client.get_asset_details()
# ## Get dust log
# log = client.get_dust_log()