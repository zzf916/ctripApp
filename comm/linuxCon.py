# -*- coding: utf-8 -*-
# File : linuxCon.py
# Author: Off
# Date : 2022/3/15
# Desc :

import paramiko


class LinuxBase(object):

    def __init__(self, params: dict):
        self.hostname = params['hostname']
        self.port = params['port']
        self.username = params['username']
        self.password = params['password']

    def connection(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh_client.connect(allow_agent=False, hostname=self.hostname, port=self.port, username=self.username,
                               password=self.password)
            return ssh_client
        except Exception as e:
            print("linux connect error:{}".format(e))
            return None

    def exec_command(self, command, ssh_client=None):
        try:
            if not ssh_client:
                ssh_client = self.connection()
            std_in, std_out, std_err = ssh_client.exec_command(command)
            return std_out
        except Exception as e:
            print(e)