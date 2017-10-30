# _*_ coding:utf-8 _*_

import os, sys
import StringIO
import datetime

from Tools.Encryption.Encrypt import FoxCrypt
from Tools.Encryption.RSA import FvcRSA

class Engine:
    def __init__(self, debug=False):
        self.debug = debug

        self.plugins_path = None
        self.fxmfiles = []
        self.fxm_modules = []

        self.max_datetime = datetime.datetime(1980, 1, 1, 0, 0, 0, 0)


    def set_plugins(self, plugins_path):
        self.plugins_path = plugins_path

        pu = FvcRSA.read_key(plugins_path + os.sep  )

