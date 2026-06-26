# Source Generated with Decompyle++
# File: cpython-38-9556344e34d4.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = None(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, object)
    __pybcsec_self__ = self
    msg = 'testing exception: %r'
    exc = None
    
    try:
        1 / 0
    finally:
        pass
    except ZeroDivisionError:
        e = None
        
        try:
            exc = e
            self.logger.exception(msg, self.recording)
        finally:
            if None:
                e = None
                del e
            
            self.assertEqual(len(self.recording.records), 1)
            record = self.recording.records[0]
            self.assertEqual(record.levelno, logging.ERROR)
            self.assertEqual(record.msg, msg)
            self.assertEqual(record.args, (self.recording,))
            self.assertEqual(record.exc_info, (exc.__class__, exc, exc.__traceback__))
            return None



if __name__ == '__main__':
    __pybcsec_seed__()
