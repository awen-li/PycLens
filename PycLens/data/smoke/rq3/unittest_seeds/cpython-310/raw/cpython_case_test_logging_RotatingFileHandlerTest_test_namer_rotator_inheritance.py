# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: RotatingFileHandlerTest_test_namer_rotator_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class HandlerWithNamerAndRotator(logging.handlers.RotatingFileHandler):

        def namer(self, name):
            return name + '.test'

        def rotator(self, source, dest):
            if os.path.exists(source):
                os.replace(source, dest + '.rotated')
    rh = HandlerWithNamerAndRotator(self.fn, encoding='utf-8', backupCount=2, maxBytes=1)
    self.assertEqual(rh.namer(self.fn), self.fn + '.test')
    rh.emit(self.next_rec())
    self.assertLogFile(self.fn)
    rh.emit(self.next_rec())
    self.assertLogFile(rh.namer(self.fn + '.1') + '.rotated')
    self.assertFalse(os.path.exists(rh.namer(self.fn + '.1')))
    rh.close()
