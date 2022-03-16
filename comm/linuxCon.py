# -*- coding: utf-8 -*-
# File : linuxCon.py
# Author: Off
# Date : 2022/3/15
# Desc :

import paramiko

from comm.logs import Logging

log = Logging().logger


class LinuxBase(object):

    def __init__(self, params: dict):
        """
        self.key = params.get('keyPath')
        keyPath： 密钥地址

        """
        self.hostname = params.get('hostname')
        self.port = params.get('port')
        self.username = params.get('username')
        self.password = params.get('password')
        self.key = params.get('keyPath')

    def connection(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if self.key is not None:
                try:
                    private_key = paramiko.RSAKey.from_private_key_file(self.key)
                    ssh_client.connect(allow_agent=False, hostname=self.hostname, port=self.port,
                                       username=self.username, pkey=private_key)
                    return ssh_client

                except Exception as e:
                    log.info("linux connect for private_key error:{}".format(e))
                    print("linux connect for private_key error:{}".format(e))

            ssh_client.connect(allow_agent=False, hostname=self.hostname, port=self.port, username=self.username,
                               password=self.password)
            return ssh_client
        except Exception as e:
            log.info("linux connect error:{}".format(e))
            print("linux connect error:{}".format(e))
            return None

    def exec_command(self, command, ssh_client=None):
        """

        :param command: 执行命令
        :param ssh_client:
        :return:
        """
        try:
            if not ssh_client:
                ssh_client = self.connection()
            std_in, std_out, std_err = ssh_client.exec_command(command)
            return std_out
        except Exception as e:
            log.info(e)
            print(e)

    def upload(self, outPath, intoPath):
        """
        上传文件
        :param outPath: 传出文件
        :param intoPath: 接受文件
        :return:
        """
        ssh_client = self.connection()
        tran = ssh_client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(tran)
        sftp.put(localpath=outPath, remotepath=intoPath)
        print("文件上传成功！")
        log.info("文件上传成功！")
        ssh_client.close()

    def download(self, localPath, remotePath):
        """
        下载文件
        :param localPath:
        :param remotePath:
        :return:
        """

        ssh_client = self.connection()
        tran = ssh_client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(tran)
        sftp.get(localpath=localPath, remotepath=remotePath)
        print("文件下载成功！")
        log.info("文件下载成功！")
        ssh_client.close()


# if __name__ == '__main__':
#     a = {"hostname": "120.76.40.173", "port": "61900", "username": "bigdata", "password": "412082020@a"}
#     LinuxBase(a).upload('D:\GITHUB\ctripApp\data\ctrip20220216134243.txt', '/home/bigdata/ctrip20220216134243.txt')
