# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_add_and_remove_folders

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._box.add_folder('one')
    self._box.add_folder('two')
    self.assertEqual(len(self._box.list_folders()), 2)
    self.assertEqual(set(self._box.list_folders()), set(('one', 'two')))
    self._box.remove_folder('one')
    self.assertEqual(len(self._box.list_folders()), 1)
    self.assertEqual(set(self._box.list_folders()), set(('two',)))
    self._box.add_folder('three')
    self.assertEqual(len(self._box.list_folders()), 2)
    self.assertEqual(set(self._box.list_folders()), set(('two', 'three')))
    self._box.remove_folder('three')
    self.assertEqual(len(self._box.list_folders()), 1)
    self.assertEqual(set(self._box.list_folders()), set(('two',)))
    self._box.remove_folder('two')
    self.assertEqual(len(self._box.list_folders()), 0)
    self.assertEqual(self._box.list_folders(), [])
