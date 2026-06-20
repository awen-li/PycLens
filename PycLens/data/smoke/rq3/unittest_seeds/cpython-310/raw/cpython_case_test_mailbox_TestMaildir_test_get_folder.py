# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_get_folder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._box.add_folder('foo.bar')
    folder0 = self._box.get_folder('foo.bar')
    folder0.add(self._template % 'bar')
    self.assertTrue(os.path.isdir(os.path.join(self._path, '.foo.bar')))
    folder1 = self._box.get_folder('foo.bar')
    self.assertEqual(folder1.get_string(folder1.keys()[0]), self._template % 'bar')
