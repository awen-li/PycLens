# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3Class_test_apop_REDOS

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    evil_welcome = b'+OK' + b'<' * 1000000
    with test_support.swap_attr(self.client, 'welcome', evil_welcome):
        self.assertRaises(poplib.error_proto, self.client.apop, 'a', 'kb')
