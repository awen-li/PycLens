# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_config14_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as output:
        self.apply_config(self.config14)
        h = logging._handlers['hand1']
        self.assertEqual(h.foo, 'bar')
        self.assertEqual(h.terminator, '!\n')
        logging.warning('Exclamation')
        self.assertTrue(output.getvalue().endswith('Exclamation!\n'))
