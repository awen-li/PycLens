# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildirMessage_test_date

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(_sample_message)
    self.assertLess(abs(msg.get_date() - time.time()), 60)
    msg.set_date(0.0)
    self.assertEqual(msg.get_date(), 0.0)
