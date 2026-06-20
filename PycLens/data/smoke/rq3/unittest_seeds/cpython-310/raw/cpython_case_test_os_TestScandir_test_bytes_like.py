# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_bytes_like

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.create_file('file.txt')
    for cls in (bytearray, memoryview):
        path_bytes = cls(os.fsencode(self.path))
        with self.assertWarns(DeprecationWarning):
            entries = list(os.scandir(path_bytes))
        self.assertEqual(len(entries), 1, entries)
        entry = entries[0]
        self.assertEqual(entry.name, b'file.txt')
        self.assertEqual(entry.path, os.fsencode(os.path.join(self.path, 'file.txt')))
        self.assertIs(type(entry.name), bytes)
        self.assertIs(type(entry.path), bytes)
