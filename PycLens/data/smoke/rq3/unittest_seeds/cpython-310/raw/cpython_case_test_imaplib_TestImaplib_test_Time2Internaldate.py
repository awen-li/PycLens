# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: TestImaplib_test_Time2Internaldate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = '"18-May-2033 05:33:20 +0200"'
    for t in self.timevalues():
        internal = imaplib.Time2Internaldate(t)
        self.assertEqual(internal, expected)
