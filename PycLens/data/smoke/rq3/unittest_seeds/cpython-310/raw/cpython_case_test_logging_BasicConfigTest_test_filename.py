# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cleanup(h1, h2, fn):
        h1.close()
        h2.close()
        os.remove(fn)
    logging.basicConfig(filename='test.log', encoding='utf-8')
    self.assertEqual(len(logging.root.handlers), 1)
    handler = logging.root.handlers[0]
    self.assertIsInstance(handler, logging.FileHandler)
    expected = logging.FileHandler('test.log', 'a', encoding='utf-8')
    self.assertEqual(handler.stream.mode, expected.stream.mode)
    self.assertEqual(handler.stream.name, expected.stream.name)
    self.addCleanup(cleanup, handler, expected, 'test.log')
