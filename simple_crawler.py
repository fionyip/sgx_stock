#stock
import requests
import pandas as pd
import json
from datetime import datetime
from pytz import timezone


params = 'nc%2Cadjusted-vwap%2Cb%2Cbv%2Cp%2Cc%2Cchange_vs_pc%2Cchange_vs_pc_percentage%2Ccx%2Ccn%2Cdp%2Cdpc%2Cdu%2Ced%2Cfn%2Ch%2Ciiv%2Ciopv%2Clt%2Cl%2Co%2Cp_%2Cpv%2Cptd%2Cs%2Csv%2Ctrading_time%2Cv_%2Cv%2Cvl%2Cvwap%2Cvwap-currency'

stock_link ={
    'd05':'https://api.sgx.com/securities/v1.1/stocks/code/D05?params=',
    'cc3':'https://api.sgx.com/securities/v1.1/stocks/code/CC3?params=',
    's68':'https://api.sgx.com/securities/v1.1/stocks/code/S68?params=',
    'z74':'https://api.sgx.com/securities/v1.1/stocks/code/Z74?params=',
}


def request_stock_p():
  tmp_list = []
  for key,item in stock_link.items():
    tmp_dict = {}
    req= requests.get(item+params)
    data_dict = json.loads(req.text)
    tmp_dict['status_code'] = data_dict['meta']['code']
    tmp_dict['stock'] = key
    tmp_dict['price']= data_dict['data']['prices'][0]['lt']
    now_utc = datetime.now(timezone('UTC'))
    tmp_dict['crawl_time'] = now_utc.astimezone(timezone('Hongkong')).strftime("%m/%d/%Y, %H:%M:%S")
    timestamp = datetime.fromtimestamp(int(data_dict['meta']['processedTime']*0.001))
    tmp_dict['stock_processed_time'] = timestamp.astimezone(timezone('Hongkong')).strftime("%m/%d/%Y, %H:%M:%S")
    tmp_list.append(tmp_dict)
  return tmp_list





