import paramiko

# 实例化SSHClient
client = paramiko.SSHClient()
# 创建白名单
know_hosts = paramiko.AutoAddPolicy()
# 加载白名单
client.set_missing_host_key_policy(know_hosts)
# 连接ssh服务器，以用户密码认证

client.connect(hostname="10.10.116.70", port=22, username="root", password="123456")

# 打开一个Channel并执行命令
stdin, stdout, stderr = client.exec_command('df -h ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值


# 打印执行结果
print(type(stdout))

print(stdout.read().decode('utf-8'))

# 关闭SSHClient
client.close()
"""
"""