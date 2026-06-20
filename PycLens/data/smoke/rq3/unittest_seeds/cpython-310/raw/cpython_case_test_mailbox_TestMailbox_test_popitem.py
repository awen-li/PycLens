# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_popitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    keys = []
    for i in range(10):
        keys.append(self._box.add(self._template % i))
    seen = []
    for i in range(10):
        (key, msg) = self._box.popitem()
        self.assertIn(key, keys)
        self.assertNotIn(key, seen)
        seen.append(key)
        self.assertEqual(int(msg.get_payload()), keys.index(key))
    self.assertEqual(len(self._box), 0)
    for key in keys:
        self.assertRaises(KeyError, lambda : self._box[key])
