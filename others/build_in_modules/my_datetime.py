# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如
# UTC+5:00，均是str，请编写一个函数将其转换为timestamp

import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):
    time_list = re.match(r'^([12]?\d{3})-(1?\d)-([123]?\d) ([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$', dt_str).groups()
    # print("time_list", time_list)
    tz_offset = int(re.match(r'UTC([+-][01]?\d):[03]0', tz_str).groups()[0])
    tz = timezone(timedelta(hours=tz_offset))
    time_list = list(map(lambda x: int(x), time_list))
    utc_0_timestamp = datetime(*time_list).replace(tzinfo=tz).timestamp()
    return utc_0_timestamp


# t1 = to_timestamp('2015-6-1 08:10:39', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
assert t2 == 1433121030.0, t2
# t3 = to_timestamp('399-4-1 07:07:07', 'UTC+8:00')
# t4 = to_timestamp('399-4-1 17:07:07', 'UTC+8:00')

print('Pass')
