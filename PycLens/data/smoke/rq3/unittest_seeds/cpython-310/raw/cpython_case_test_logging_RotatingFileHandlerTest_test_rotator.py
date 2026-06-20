# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: RotatingFileHandlerTest_test_rotator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def namer(name):
        return name + '.gz'

    def rotator(source, dest):
        with open(source, 'rb') as sf:
            data = sf.read()
            compressed = zlib.compress(data, 9)
            with open(dest, 'wb') as df:
                df.write(compressed)
        os.remove(source)
    rh = logging.handlers.RotatingFileHandler(self.fn, encoding='utf-8', backupCount=2, maxBytes=1)
    rh.rotator = rotator
    rh.namer = namer
    m1 = self.next_rec()
    rh.emit(m1)
    self.assertLogFile(self.fn)
    m2 = self.next_rec()
    rh.emit(m2)
    fn = namer(self.fn + '.1')
    self.assertLogFile(fn)
    newline = os.linesep
    with open(fn, 'rb') as f:
        compressed = f.read()
        data = zlib.decompress(compressed)
        self.assertEqual(data.decode('ascii'), m1.msg + newline)
    rh.emit(self.next_rec())
    fn = namer(self.fn + '.2')
    self.assertLogFile(fn)
    with open(fn, 'rb') as f:
        compressed = f.read()
        data = zlib.decompress(compressed)
        self.assertEqual(data.decode('ascii'), m1.msg + newline)
    rh.emit(self.next_rec())
    fn = namer(self.fn + '.2')
    with open(fn, 'rb') as f:
        compressed = f.read()
        data = zlib.decompress(compressed)
        self.assertEqual(data.decode('ascii'), m2.msg + newline)
    self.assertFalse(os.path.exists(namer(self.fn + '.3')))
    rh.close()
