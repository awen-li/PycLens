# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestSingleFile_test_add_doesnt_rewrite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inode_before = os.stat(self._path).st_ino
    self._box.add(self._template % 0)
    self._box.flush()
    inode_after = os.stat(self._path).st_ino
    self.assertEqual(inode_before, inode_after)
    self._box.close()
    self._box = self._factory(self._path)
    self.assertEqual(len(self._box), 1)
