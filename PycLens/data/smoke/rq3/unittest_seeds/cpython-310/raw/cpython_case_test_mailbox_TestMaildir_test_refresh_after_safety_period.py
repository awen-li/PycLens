# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_refresh_after_safety_period

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    key1 = self._box.add(self._template % 1)
    self._box = self._factory(self._path)
    self.assertEqual(self._box._toc, {})
    self._box._skewfactor = -3
    self._box._refresh()
    self.assertEqual(sorted(self._box._toc.keys()), sorted([key0, key1]))
