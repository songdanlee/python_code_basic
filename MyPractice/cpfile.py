import time
import subprocess

while True:
    if time.localtime().tm_hour == 9:
        log_file = open("/opt/data/log.log","a")
        now = time.strftime("%Y-%m-%d-%S")
        try:
            subprocess.Popen("cp /opt/1.py /opt/data/%s.py" % now)
            print ("%s拷贝成功"% now,log_file)
        except Exception as e:
            # print (e)
            print ("%s 拷贝失败 异常为：%s"%(now,str(e)),log_file)
        finally:
            log_file.close()
