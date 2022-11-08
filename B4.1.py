import logging

def init_logger(out_pth:str=''):
    # 日志信息记录到文件
    logging.basicConfig(filename=out_pth, level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
init_logger('C:/Users/Lenovo/Desktop/test/A4/A4.4.1')
#级别越高打印的日志越少，级别等级：critical>error>warning>info>debug
#debug:打印全部的日志（notset等同于debug)
#info:打印info,warning,error,critical级别的日志
#warning：打印warning,error,critical级别的日志
#error：打印error,critical级别的日志
#critical:打印critical级别