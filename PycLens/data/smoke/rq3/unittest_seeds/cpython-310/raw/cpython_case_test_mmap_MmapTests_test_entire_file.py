# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_entire_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb+') as f:
        f.write(2 ** 16 * b'm')
    with open(TESTFN, 'rb+') as f, mmap.mmap(f.fileno(), 0) as mf:
        self.assertEqual(len(mf), 2 ** 16, 'Map size should equal file size.')
        self.assertEqual(mf.read(2 ** 16), 2 ** 16 * b'm')
