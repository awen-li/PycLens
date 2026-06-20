# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMHMessage_test_sequences

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MHMessage(_sample_message)
    self.assertEqual(msg.get_sequences(), [])
    msg.set_sequences(['foobar'])
    self.assertEqual(msg.get_sequences(), ['foobar'])
    msg.set_sequences([])
    self.assertEqual(msg.get_sequences(), [])
    msg.add_sequence('unseen')
    self.assertEqual(msg.get_sequences(), ['unseen'])
    msg.add_sequence('flagged')
    self.assertEqual(msg.get_sequences(), ['unseen', 'flagged'])
    msg.add_sequence('flagged')
    self.assertEqual(msg.get_sequences(), ['unseen', 'flagged'])
    msg.remove_sequence('unseen')
    self.assertEqual(msg.get_sequences(), ['flagged'])
    msg.add_sequence('foobar')
    self.assertEqual(msg.get_sequences(), ['flagged', 'foobar'])
    msg.remove_sequence('replied')
    self.assertEqual(msg.get_sequences(), ['flagged', 'foobar'])
    msg.set_sequences(['foobar', 'replied'])
    self.assertEqual(msg.get_sequences(), ['foobar', 'replied'])
