# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestDirEntry_test_unpickable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = create_file(os.path.join(self.path, 'file.txt'), b'python')
    entry = [entry for entry in os.scandir(self.path)].pop()
    self.assertIsInstance(entry, os.DirEntry)
    self.assertEqual(entry.name, 'file.txt')
    import pickle
    self.assertRaises(TypeError, pickle.dumps, entry, filename)
