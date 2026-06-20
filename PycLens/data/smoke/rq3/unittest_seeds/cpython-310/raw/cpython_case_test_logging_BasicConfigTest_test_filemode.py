# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_filemode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cleanup(h1, h2, fn):
        h1.close()
        h2.close()
        os.remove(fn)
    logging.basicConfig(filename='test.log', filemode='wb')
    handler = logging.root.handlers[0]
    expected = logging.FileHandler('test.log', 'wb')
    self.assertEqual(handler.stream.mode, expected.stream.mode)
    self.addCleanup(cleanup, handler, expected, 'test.log')
