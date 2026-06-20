# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_mh_to_mh

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MHMessage(_sample_message)
    msg.add_sequence('unseen')
    msg.add_sequence('replied')
    msg.add_sequence('flagged')
    self.assertEqual(mailbox.MHMessage(msg).get_sequences(), ['unseen', 'replied', 'flagged'])
