# Copyright (c) 2008 Simplistix Ltd
# See license.txt for license details.

from logging import Handler,getLogger

class Handler(Handler):

    fired = False
    
    def __init__(self,level,logger='',install=True):
        Handler.__init__(self)
        self.level=level
        self.logger=logger
        if install:
            self.install()

    def install(self):
        self.setLevel(self.level)
        getLogger(self.logger).addHandler(self)
        
    def emit(self, record):
        self.fired=True
        self.record = record

    def reset(self):
        self.fired=False

    def remove(self):
        getLogger().removeHandler(self)
