# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_mkdir_concurrent_parent_creation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for pattern_num in range(32):
        p = self.cls(BASE, 'dirCPC%d' % pattern_num)
        self.assertFalse(p.exists())

        def my_mkdir(path, mode=511):
            path = str(path)
            if pattern.pop():
                os.mkdir(path, mode)
                concurrently_created.add(path)
            os.mkdir(path, mode)
        pattern = [bool(pattern_num & 1 << n) for n in range(5)]
        concurrently_created = set()
        p12 = p / 'dir1' / 'dir2'
        try:
            with mock.patch('pathlib._normal_accessor.mkdir', my_mkdir):
                p12.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            self.assertIn(str(p12), concurrently_created)
        else:
            self.assertNotIn(str(p12), concurrently_created)
        self.assertTrue(p.exists())
