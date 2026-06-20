# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMH_test_sequences

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self._box.get_sequences(), {})
    msg0 = mailbox.MHMessage(self._template % 0)
    msg0.add_sequence('foo')
    key0 = self._box.add(msg0)
    self.assertEqual(self._box.get_sequences(), {'foo': [key0]})
    msg1 = mailbox.MHMessage(self._template % 1)
    msg1.set_sequences(['bar', 'replied', 'foo'])
    key1 = self._box.add(msg1)
    self.assertEqual(self._box.get_sequences(), {'foo': [key0, key1], 'bar': [key1], 'replied': [key1]})
    msg0.set_sequences(['flagged'])
    self._box[key0] = msg0
    self.assertEqual(self._box.get_sequences(), {'foo': [key1], 'bar': [key1], 'replied': [key1], 'flagged': [key0]})
    self._box.remove(key1)
    self.assertEqual(self._box.get_sequences(), {'flagged': [key0]})
