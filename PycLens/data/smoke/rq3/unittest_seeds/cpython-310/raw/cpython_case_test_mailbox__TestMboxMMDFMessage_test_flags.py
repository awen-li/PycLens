# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDFMessage_test_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.mboxMessage(_sample_message)
    self.assertEqual(msg.get_flags(), '')
    msg.set_flags('F')
    self.assertEqual(msg.get_flags(), 'F')
    msg.set_flags('XODR')
    self.assertEqual(msg.get_flags(), 'RODX')
    msg.add_flag('FA')
    self.assertEqual(msg.get_flags(), 'RODFAX')
    msg.remove_flag('FDXA')
    self.assertEqual(msg.get_flags(), 'RO')
    self._check_sample(msg)
