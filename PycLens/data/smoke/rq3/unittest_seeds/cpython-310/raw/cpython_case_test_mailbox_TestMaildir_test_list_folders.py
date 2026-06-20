# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_list_folders

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._box.add_folder('one')
    self._box.add_folder('two')
    self._box.add_folder('three')
    self.assertEqual(len(self._box.list_folders()), 3)
    self.assertEqual(set(self._box.list_folders()), set(('one', 'two', 'three')))
