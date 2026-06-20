# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: TestImaplib_test_Internaldate2tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t0 = calendar.timegm((2000, 1, 1, 0, 0, 0, -1, -1, -1))
    tt = imaplib.Internaldate2tuple(b'25 (INTERNALDATE "01-Jan-2000 00:00:00 +0000")')
    self.assertEqual(time.mktime(tt), t0)
    tt = imaplib.Internaldate2tuple(b'25 (INTERNALDATE "01-Jan-2000 11:30:00 +1130")')
    self.assertEqual(time.mktime(tt), t0)
    tt = imaplib.Internaldate2tuple(b'25 (INTERNALDATE "31-Dec-1999 12:30:00 -1130")')
    self.assertEqual(time.mktime(tt), t0)
