# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: TestImaplib_test_Internaldate2tuple_issue10941

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotEqual(imaplib.Internaldate2tuple(b'25 (INTERNALDATE "02-Apr-2000 02:30:00 +0000")'), imaplib.Internaldate2tuple(b'25 (INTERNALDATE "02-Apr-2000 03:30:00 +0000")'))
