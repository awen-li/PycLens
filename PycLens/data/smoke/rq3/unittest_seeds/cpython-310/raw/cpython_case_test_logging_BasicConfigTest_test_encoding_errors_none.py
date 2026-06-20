# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_encoding_errors_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        encoding = 'ascii'
        logging.basicConfig(filename='test.log', encoding=encoding, errors=None, format='%(message)s', level=logging.DEBUG)
        self.assertEqual(len(logging.root.handlers), 1)
        handler = logging.root.handlers[0]
        self.assertIsInstance(handler, logging.FileHandler)
        self.assertEqual(handler.encoding, encoding)
        self.assertIsNone(handler.errors)
        message = []

        def dummy_handle_error(record):
            (_, v, _) = sys.exc_info()
            message.append(str(v))
        handler.handleError = dummy_handle_error
        logging.debug('The Øresund Bridge joins Copenhagen to Malmö')
        self.assertTrue(message)
        self.assertIn("'ascii' codec can't encode character '\\xd8' in position 4:", message[0])
    finally:
        handler.close()
        with open('test.log', encoding='utf-8') as f:
            data = f.read().strip()
        os.remove('test.log')
        self.assertEqual(data, '')
