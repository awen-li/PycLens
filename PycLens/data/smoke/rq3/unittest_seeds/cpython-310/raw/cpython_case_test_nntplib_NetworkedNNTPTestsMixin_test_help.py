# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, lines) = self.server.help()
    self.assertTrue(resp.startswith('100 '), resp)
    for line in lines:
        self.assertEqual(str, type(line))
