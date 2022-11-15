import calendar
import time

def transformDate(dataStr):
    """
    对指定时间格式的字符串（'Jul 27,2022' ）
    进行类型转换
    返回如下格式
    ('Jul 27,2022', '2022-7-27 00:00:00', 1658851200, '2022/07/27 00:00:00')
    (   输入字符串 ,       时间格式一      ,时间戳格式  ,      时间格式一       )
    """
    dataStrs = dataStr.split(',')
    year = dataStrs[1]
    monthStr = dataStrs[0].split(' ')[0]
    day = dataStrs[0].split(' ')[1]
    month = list(calendar.month_abbr).index(monthStr)

    a = f"{year}-{month}-{day} 00:00:00"
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")

    # 转换为时间戳:
    timeStamp = int(time.mktime(timeArray))

    # 修改这个地方可以指定时间格式
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    return (dataStrs, a, timeStamp, otherStyleTime)


if __name__ == '__main__':
    dataStr = 'Jul 27,2022'
    str = transformDate(dataStr)
    print(str)
    print(str[3])
