# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotIn('foo', self._box)
    key0 = self._box.add(self._template % 0)
    self.assertIn(key0, self._box)
    self.assertNotIn('foo', self._box)
    key1 = self._box.add(self._template % 1)
    self.assertIn(key1, self._box)
    self.assertIn(key0, self._box)
    self.assertNotIn('foo', self._box)
    self._box.remove(key0)
    self.assertNotIn(key0, self._box)
    self.assertIn(key1, self._box)
    self.assertNotIn('foo', self._box)
    self._box.remove(key1)
    self.assertNotIn(key1, self._box)
    self.assertNotIn(key0, self._box)
    self.assertNotIn('foo', self._box)
