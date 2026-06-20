# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDFMessage_test_from

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.mboxMessage(_sample_message)
    self._check_from(msg)
    msg.set_from('foo bar')
    self.assertEqual(msg.get_from(), 'foo bar')
    msg.set_from('foo@bar', True)
    self._check_from(msg, 'foo@bar')
    msg.set_from('blah@temp', time.localtime())
    self._check_from(msg, 'blah@temp')
