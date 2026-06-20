# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(KeyError, lambda : self._box._lookup('foo'))
    key0 = self._box.add(self._template % 0)
    self.assertEqual(self._box._lookup(key0), os.path.join('new', key0))
    os.remove(os.path.join(self._path, 'new', key0))
    self.assertEqual(self._box._toc, {key0: os.path.join('new', key0)})
    self._box.flush()
    self.assertRaises(KeyError, lambda : self._box._lookup(key0))
    self.assertEqual(self._box._toc, {})
