#!/usr/bin/python


from scanner import refresProductCache
from scanner import SearchPpProductThread
from scanner import searchPpProduct
from scanner import retryScanAllPrice
from scanner import jdKeywordsPriceByUrl
from scanner import scanAllPrices
from scanner import scanAllPrice
from scanner import scanAllPricehs
from scanner import updateMaxMinAvg

import json
from rest import app
from globUtils import logger
from globUtils import Periodic
from globUtils import config


if __name__ == '__main__':
    logger.info("爬数据")
    # thread1 = SearchPpProductThread()
    # thread1.start()
    #爬京东数据
    # scanAllPrice()
    # retryScanAllPrice()
    # scanAllPrices()
    #更新爬下来的数据（如更新最高，最低价，平均价）
    # scanAllPrice()
    #更新纬雅数据
    # scanAllPricehs()
    # 更新爬下来的数据（如更新最高，最低价，平均价）
    updateMaxMinAvg()
    port = config.get("server", "listen.port").strip()
    app.run(host='0.0.0.0', port=int(port))



