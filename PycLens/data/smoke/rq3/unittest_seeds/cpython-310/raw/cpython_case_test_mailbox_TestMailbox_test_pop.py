# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    self.assertIn(key0, self._box)
    key1 = self._box.add(self._template % 1)
    self.assertIn(key1, self._box)
    self.assertEqual(self._box.pop(key0).get_payload(), '0\n')
    self.assertNotIn(key0, self._box)
    self.assertIn(key1, self._box)
    key2 = self._box.add(self._template % 2)
    self.assertIn(key2, self._box)
    self.assertEqual(self._box.pop(key2).get_payload(), '2\n')
    self.assertNotIn(key2, self._box)
    self.assertIn(key1, self._box)
    self.assertEqual(self._box.pop(key1).get_payload(), '1\n')
    self.assertNotIn(key1, self._box)
    self.assertEqual(len(self._box), 0)
