# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDFMessage_test_initialize_with_unixfrom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.Message(_sample_message)
    msg.set_unixfrom('From foo@bar blah')
    msg = mailbox.mboxMessage(msg)
    self.assertEqual(msg.get_from(), 'foo@bar blah', msg.get_from())
