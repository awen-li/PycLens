# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDF_test_open_close_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = [self._template % i for i in range(3)]
    for value in values:
        self._box.add(value)
    self._box.close()
    mtime = os.path.getmtime(self._path)
    self._box = self._factory(self._path)
    self.assertEqual(len(self._box), 3)
    for key in self._box.iterkeys():
        self.assertIn(self._box.get_string(key), values)
    self._box.close()
    self.assertEqual(mtime, os.path.getmtime(self._path))
