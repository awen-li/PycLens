# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildirMessage_test_subdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(_sample_message)
    self.assertEqual(msg.get_subdir(), 'new')
    msg.set_subdir('cur')
    self.assertEqual(msg.get_subdir(), 'cur')
    msg.set_subdir('new')
    self.assertEqual(msg.get_subdir(), 'new')
    self.assertRaises(ValueError, lambda : msg.set_subdir('tmp'))
    self.assertEqual(msg.get_subdir(), 'new')
    msg.set_subdir('new')
    self.assertEqual(msg.get_subdir(), 'new')
    self._check_sample(msg)
