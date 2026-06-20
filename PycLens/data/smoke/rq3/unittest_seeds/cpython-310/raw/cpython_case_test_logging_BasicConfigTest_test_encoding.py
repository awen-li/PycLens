# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        encoding = 'utf-8'
        logging.basicConfig(filename='test.log', encoding=encoding, errors='strict', format='%(message)s', level=logging.DEBUG)
        self.assertEqual(len(logging.root.handlers), 1)
        handler = logging.root.handlers[0]
        self.assertIsInstance(handler, logging.FileHandler)
        self.assertEqual(handler.encoding, encoding)
        logging.debug('The Øresund Bridge joins Copenhagen to Malmö')
    finally:
        handler.close()
        with open('test.log', encoding='utf-8') as f:
            data = f.read().strip()
        os.remove('test.log')
        self.assertEqual(data, 'The Øresund Bridge joins Copenhagen to Malmö')
