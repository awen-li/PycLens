# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    keys = []
    for i in range(iterations):
        self._box.add(self._template % i)
    for (i, key) in enumerate(keys):
        self.assertEqual(self._box.get_string(key), self._template % i)
    self._box.clear()
    self.assertEqual(len(self._box), 0)
    for (i, key) in enumerate(keys):
        self.assertRaises(KeyError, lambda : self._box.get_string(key))
