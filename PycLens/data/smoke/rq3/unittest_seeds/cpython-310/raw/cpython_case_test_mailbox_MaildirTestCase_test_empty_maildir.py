# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: MaildirTestCase_test_empty_maildir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.mbox = mailbox.Maildir(os_helper.TESTFN)
    self.assertIsNone(self.mbox.next())
    self.assertIsNone(self.mbox.next())
