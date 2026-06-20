# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_add_file_after_2107

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = 4386268800
    try:
        time.localtime(ts)
    except OverflowError:
        self.skipTest(f'time.localtime({ts}) raises OverflowError')
    try:
        os.utime(TESTFN, (ts, ts))
    except OverflowError:
        self.skipTest('Host fs cannot set timestamp to required value.')
    mtime_ns = os.stat(TESTFN).st_mtime_ns
    if mtime_ns != 4386268800 * 10 ** 9:
        self.skipTest(f'Linux VFS/XFS kernel bug detected: mtime_ns={mtime_ns!r}')
    with zipfile.ZipFile(TESTFN2, 'w') as zipfp:
        self.assertRaises(struct.error, zipfp.write, TESTFN)
    with zipfile.ZipFile(TESTFN2, 'w', strict_timestamps=False) as zipfp:
        zipfp.write(TESTFN)
        zinfo = zipfp.getinfo(TESTFN)
        self.assertEqual(zinfo.date_time, (2107, 12, 31, 23, 59, 59))
