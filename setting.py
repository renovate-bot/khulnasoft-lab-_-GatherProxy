# -*- coding: utf-8 -*-
VERSION = "2.4.0"

# ############### server config ###############
HOST = "0.0.0.0"
PORT = 5010

# ############### database config ###################
# db connection uri
# example:
#      Redis: redis://:password@ip:port/db
#      Ssdb:  ssdb://:password@ip:port
DB_CONN = 'redis://:pwd@127.0.0.1:6379/0'
TABLE_NAME = 'use_proxy'

# ###### config the proxy fetch function ######
PROXY_FETCHER = [
    "freeProxy01",
    "freeProxy02",
    "freeProxy03",
    "freeProxy04",
    "freeProxy05",
    "freeProxy06",
    "freeProxy07",
    "freeProxy08",
    "freeProxy09",
    "freeProxy10",
    "freeProxy11"
]

# ############# proxy validator #################
# Proxy authentication target website
HTTP_URL = "http://httpbin.org"
HTTPS_URL = "https://www.qq.com"
VERIFY_TIMEOUT = 10
MAX_FAIL_COUNT = 0
POOL_SIZE_MIN = 20

# ############# proxy attributes #################
PROXY_REGION = True

# ############# scheduler config #################

# Set the timezone for the scheduler forcely (optional)
# If it is running on a VM, and
#   "ValueError: Timezone offset does not match system offset"
#   was raised during scheduling.
# Please uncomment the following line and set a timezone for the scheduler.
# Otherwise it will detect the timezone from the system automatically.
TIMEZONE = "Asia/Shanghai"  # Example: Set the timezone to "Asia/Dhaka"
