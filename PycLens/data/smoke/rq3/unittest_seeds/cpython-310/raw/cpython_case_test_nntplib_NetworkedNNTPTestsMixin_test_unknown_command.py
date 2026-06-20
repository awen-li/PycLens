# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_unknown_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(nntplib.NNTPPermanentError) as cm:
        self.server._shortcmd('XYZZY')
    resp = cm.exception.response
    self.assertTrue(resp.startswith('500 '), resp)
