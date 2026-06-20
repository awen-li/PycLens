# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: MaildirTestCase_test_nonempty_maildir_both

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.createMessage('cur')
    self.createMessage('new')
    self.mbox = mailbox.Maildir(os_helper.TESTFN)
    self.assertIsNotNone(self.mbox.next())
    self.assertIsNotNone(self.mbox.next())
    self.assertIsNone(self.mbox.next())
    self.assertIsNone(self.mbox.next())
