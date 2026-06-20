# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    keys = []
    for i in range(repetitions):
        self.assertEqual(len(self._box), i)
        keys.append(self._box.add(self._template % i))
        self.assertEqual(len(self._box), i + 1)
    for i in range(repetitions):
        self.assertEqual(len(self._box), repetitions - i)
        self._box.remove(keys[i])
        self.assertEqual(len(self._box), repetitions - i - 1)
