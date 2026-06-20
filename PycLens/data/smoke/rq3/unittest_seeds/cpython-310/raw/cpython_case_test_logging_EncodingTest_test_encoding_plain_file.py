# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: EncodingTest_test_encoding_plain_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    log = logging.getLogger('test')
    (fd, fn) = tempfile.mkstemp('.log', 'test_logging-1-')
    os.close(fd)
    data = 'foo\x80'
    try:
        handler = logging.FileHandler(fn, encoding='utf-8')
        log.addHandler(handler)
        try:
            log.warning(data)
        finally:
            log.removeHandler(handler)
            handler.close()
        f = open(fn, encoding='utf-8')
        try:
            self.assertEqual(f.read().rstrip(), data)
        finally:
            f.close()
    finally:
        if os.path.isfile(fn):
            os.remove(fn)
