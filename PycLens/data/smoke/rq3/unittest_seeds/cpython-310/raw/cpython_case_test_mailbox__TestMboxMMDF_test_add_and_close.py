# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDF_test_add_and_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._box.add(_sample_message)
    for i in range(3):
        self._box.add(self._template % i)
    self._box.add(_sample_message)
    self._box._file.flush()
    self._box._file.seek(0)
    contents = self._box._file.read()
    self._box.close()
    with open(self._path, 'rb') as f:
        self.assertEqual(contents, f.read())
    self._box = self._factory(self._path)
