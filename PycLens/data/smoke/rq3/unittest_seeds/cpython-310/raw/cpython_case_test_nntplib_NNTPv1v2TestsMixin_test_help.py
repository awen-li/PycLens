# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, help) = self.server.help()
    self.assertEqual(resp, '100 Legal commands')
    self.assertEqual(help, ['  authinfo user Name|pass Password|generic <prog> <args>', '  date', '  help', 'Report problems to <root@example.org>'])
