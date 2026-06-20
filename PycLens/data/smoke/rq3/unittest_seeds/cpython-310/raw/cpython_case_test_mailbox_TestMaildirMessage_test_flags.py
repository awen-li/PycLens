# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildirMessage_test_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(_sample_message)
    self.assertEqual(msg.get_flags(), '')
    self.assertEqual(msg.get_subdir(), 'new')
    msg.set_flags('F')
    self.assertEqual(msg.get_subdir(), 'new')
    self.assertEqual(msg.get_flags(), 'F')
    msg.set_flags('SDTP')
    self.assertEqual(msg.get_flags(), 'DPST')
    msg.add_flag('FT')
    self.assertEqual(msg.get_flags(), 'DFPST')
    msg.remove_flag('TDRP')
    self.assertEqual(msg.get_flags(), 'FS')
    self.assertEqual(msg.get_subdir(), 'new')
    self._check_sample(msg)
