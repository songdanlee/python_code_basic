import paramiko

# 实例化对象
ssh = paramiko.Transport(
    sock=("10.10.116.70",22)
)
# 创建连接
ssh.connect(
            username="root",
            password="123456"
)

sftp = paramiko.SFTPClient.from_transport(ssh)
# 上传文件
# sftp.put("test.txt","/root/test.py")
# 下载文件
sftp.get("/root/anaconda-ks.cfg","hello.cfg")

sftp.close()