# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_discard

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    key1 = self._box.add(self._template % 1)
    self.assertEqual(len(self._box), 2)
    self._box.discard(key0)
    self.assertEqual(len(self._box), 1)
    self.assertRaises(KeyError, lambda : self._box[key0])
    self._box.discard(key0)
    self.assertEqual(len(self._box), 1)
    self.assertRaises(KeyError, lambda : self._box[key0])
