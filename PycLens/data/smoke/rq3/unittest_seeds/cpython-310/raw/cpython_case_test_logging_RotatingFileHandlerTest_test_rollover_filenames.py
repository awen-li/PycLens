# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: RotatingFileHandlerTest_test_rollover_filenames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def namer(name):
        return name + '.test'
    rh = logging.handlers.RotatingFileHandler(self.fn, encoding='utf-8', backupCount=2, maxBytes=1)
    rh.namer = namer
    rh.emit(self.next_rec())
    self.assertLogFile(self.fn)
    rh.emit(self.next_rec())
    self.assertLogFile(namer(self.fn + '.1'))
    rh.emit(self.next_rec())
    self.assertLogFile(namer(self.fn + '.2'))
    self.assertFalse(os.path.exists(namer(self.fn + '.3')))
    rh.close()
