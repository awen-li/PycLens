# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestSingleFile_test_permissions_after_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mode = os.stat(self._path).st_mode | 438
    os.chmod(self._path, mode)
    self._box.add(self._template % 0)
    i = self._box.add(self._template % 1)
    self._box.remove(i)
    self._box.flush()
    self.assertEqual(os.stat(self._path).st_mode, mode)
