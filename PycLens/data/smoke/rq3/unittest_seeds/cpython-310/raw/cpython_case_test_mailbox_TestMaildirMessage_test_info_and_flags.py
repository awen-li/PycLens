# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildirMessage_test_info_and_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(_sample_message)
    self.assertEqual(msg.get_info(), '')
    msg.set_flags('SF')
    self.assertEqual(msg.get_flags(), 'FS')
    self.assertEqual(msg.get_info(), '2,FS')
    msg.set_info('1,')
    self.assertEqual(msg.get_flags(), '')
    self.assertEqual(msg.get_info(), '1,')
    msg.remove_flag('RPT')
    self.assertEqual(msg.get_flags(), '')
    self.assertEqual(msg.get_info(), '1,')
    msg.add_flag('D')
    self.assertEqual(msg.get_flags(), 'D')
    self.assertEqual(msg.get_info(), '2,D')
    self._check_sample(msg)
