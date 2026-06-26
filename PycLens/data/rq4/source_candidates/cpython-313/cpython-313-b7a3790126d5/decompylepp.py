# Source Generated with Decompyle++
# File: cpython-313-b7a3790126d5.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    logger = logging.getLogger('slh')
    self.sl_hdlr.close()
    self.handled.clear()
    logger.error('späm')
    self.handled.wait(support.LONG_TIMEOUT)
    self.assertEqual(self.log_output, b'<11>sp\xc3\xa4m\x00')

if __name__ == '__main__':
    None()
return None
