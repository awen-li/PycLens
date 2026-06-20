# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_refresh

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self._box._toc, {})
    key0 = self._box.add(self._template % 0)
    key1 = self._box.add(self._template % 1)
    self.assertEqual(self._box._toc, {})
    self._box._refresh()
    self.assertEqual(self._box._toc, {key0: os.path.join('new', key0), key1: os.path.join('new', key1)})
    key2 = self._box.add(self._template % 2)
    self.assertEqual(self._box._toc, {key0: os.path.join('new', key0), key1: os.path.join('new', key1)})
    self._box._refresh()
    self.assertEqual(self._box._toc, {key0: os.path.join('new', key0), key1: os.path.join('new', key1), key2: os.path.join('new', key2)})
