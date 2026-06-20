# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_encoding_errors_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        encoding = 'ascii'
        logging.basicConfig(filename='test.log', encoding=encoding, format='%(message)s', level=logging.DEBUG)
        self.assertEqual(len(logging.root.handlers), 1)
        handler = logging.root.handlers[0]
        self.assertIsInstance(handler, logging.FileHandler)
        self.assertEqual(handler.encoding, encoding)
        self.assertEqual(handler.errors, 'backslashreplace')
        logging.debug('😂: ☃️: The Øresund Bridge joins Copenhagen to Malmö')
    finally:
        handler.close()
        with open('test.log', encoding='utf-8') as f:
            data = f.read().strip()
        os.remove('test.log')
        self.assertEqual(data, '\\U0001f602: \\u2603\\ufe0f: The \\xd8resund Bridge joins Copenhagen to Malm\\xf6')
