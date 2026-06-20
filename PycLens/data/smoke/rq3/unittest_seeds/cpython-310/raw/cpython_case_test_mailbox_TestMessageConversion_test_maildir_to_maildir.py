# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_maildir_to_maildir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg_maildir = mailbox.MaildirMessage(_sample_message)
    msg_maildir.set_flags('DFPRST')
    msg_maildir.set_subdir('cur')
    date = msg_maildir.get_date()
    msg = mailbox.MaildirMessage(msg_maildir)
    self._check_sample(msg)
    self.assertEqual(msg.get_flags(), 'DFPRST')
    self.assertEqual(msg.get_subdir(), 'cur')
    self.assertEqual(msg.get_date(), date)
