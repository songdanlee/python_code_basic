import paramiko

# 创建终端
ssh = paramiko.SSHClient()
# 创建白名单
know_hosts = paramiko.AutoAddPolicy()
# 加载白名单
ssh.set_missing_host_key_policy(know_hosts)
# 链接服务器
ssh.connect(hostname="10.10.116.70", username="root", password="123456", port=22)
# 执行命令
# stdin, stdout, stderr = ssh.exec_command("ls -al")
# 创建shell终端
shell = ssh.invoke_shell()
while True:
    command = input("输入命令>>>:")+"\n"
    shell.send(command)
    result = shell.recv(521).decode()
    print(result)

# 关闭链接
ssh.close()
