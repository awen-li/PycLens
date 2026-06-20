# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildirMessage_test_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(_sample_message)
    self.assertEqual(msg.get_info(), '')
    msg.set_info('1,foo=bar')
    self.assertEqual(msg.get_info(), '1,foo=bar')
    self.assertRaises(TypeError, lambda : msg.set_info(None))
    self._check_sample(msg)
