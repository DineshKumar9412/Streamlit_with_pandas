
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser
# from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException

home = expanduser('~')
mypkey = paramiko.RSAKey.from_private_key_file('/Users/harikumar/.ssh/id_rsa')
# if you want to use ssh password use - ssh_password='your ssh password', bellow

sql_hostname = '10.2.1.140'
sql_username = 'ashoktroondx'
sql_password = '@#ooKtroonDX22'
sql_main_database = 'trackandtrace_10_04_2022'
sql_port = 3306
ssh_host = '15.207.73.179'
ssh_user = 'ashoktroondx'
ssh_port = 2205
sql_ip = '1.1.1.1.1'

with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=mypkey,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
    conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            passwd=sql_password, db=sql_main_database,
            port=tunnel.local_bind_port)
    query = '''SELECT VERSION();'''
    data = pd.read_sql_query(query, conn)
    conn.close()

#
# import sshtunnel
# import numpy as np
#
# with sshtunnel.SSHTunnelForwarder(ssh_address_or_host='ssh_host',
#                                   ssh_username="ssh_username",
#                                   ssh_pkey='/home/userName/.ssh/id_ed25519',
#                                   remote_bind_address=('localhost', 3306),
#                                   ) as tunnel:
#     cnx = mysql.connector.MySQLConnection(user='sql_username',
#                                           password='sql_password',
#                                           host='127.0.0.1',
#                                           database='db_name',
#                                           port=tunnel.local_bind_port)
#     cursor = cnx.cursor()
#     cursor.execute('SELECT * FROM db_name.tableName;')
#     arr = np.array(cursor.fetchall())
#     cursor.close()
#     cnx.close()

# from sshtunnel import SSHTunnelForwarder
# import pymysql
# import pandas as pd
#
#
# tunnel = SSHTunnelForwarder(('15.207.73.179', 2205), ssh_password='@#ooKtroonDX22', ssh_username='ashoktroondx',
#      remote_bind_address=('10.2.1.140 ', 3306))
# tunnel.start()
# conn = pymysql.connect(host='127.0.0.1', user='ashoktroondx', passwd='@#ooKtroonDX22', port=tunnel.local_bind_port)
# data = pd.read_sql_query("SHOW DATABASES;", conn)

# from os.path import expanduser
# import paramiko
#
# pkeyfilepath = '/html/fbads/phpmyadmin-ec2.pem'
# home = expanduser('~')
# print(pkeyfilepath)
# print("hello")
# print(home)
# mypkey = paramiko.RSAKey.from_private_key_file(home + pkeyfilepath)
# print(mypkey)