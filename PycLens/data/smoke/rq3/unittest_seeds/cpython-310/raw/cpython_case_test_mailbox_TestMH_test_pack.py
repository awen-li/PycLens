# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMH_test_pack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg0 = mailbox.MHMessage(self._template % 0)
    msg1 = mailbox.MHMessage(self._template % 1)
    msg2 = mailbox.MHMessage(self._template % 2)
    msg3 = mailbox.MHMessage(self._template % 3)
    msg0.set_sequences(['foo', 'unseen'])
    msg1.set_sequences(['foo'])
    msg2.set_sequences(['foo', 'flagged'])
    msg3.set_sequences(['foo', 'bar', 'replied'])
    key0 = self._box.add(msg0)
    key1 = self._box.add(msg1)
    key2 = self._box.add(msg2)
    key3 = self._box.add(msg3)
    self.assertEqual(self._box.get_sequences(), {'foo': [key0, key1, key2, key3], 'unseen': [key0], 'flagged': [key2], 'bar': [key3], 'replied': [key3]})
    self._box.remove(key2)
    self.assertEqual(self._box.get_sequences(), {'foo': [key0, key1, key3], 'unseen': [key0], 'bar': [key3], 'replied': [key3]})
    self._box.pack()
    self.assertEqual(self._box.keys(), [1, 2, 3])
    key0 = key0
    key1 = key0 + 1
    key2 = key1 + 1
    self.assertEqual(self._box.get_sequences(), {'foo': [1, 2, 3], 'unseen': [1], 'bar': [3], 'replied': [3]})
    key0 = self._box.add(msg1)
    key1 = self._box.add(msg1)
    key2 = self._box.add(msg1)
    key3 = self._box.add(msg1)
    self._box.remove(key0)
    self._box.remove(key2)
    self._box.lock()
    self._box.pack()
    self._box.unlock()
    self.assertEqual(self._box.get_sequences(), {'foo': [1, 2, 3, 4, 5], 'unseen': [1], 'bar': [3], 'replied': [3]})
