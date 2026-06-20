# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarReadTest_test_fileobj_seek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tar.extract('ustar/regtype', TEMPDIR, filter='data')
    with open(os.path.join(TEMPDIR, 'ustar/regtype'), 'rb') as fobj:
        data = fobj.read()
    tarinfo = self.tar.getmember('ustar/regtype')
    with self.tar.extractfile(tarinfo) as fobj:
        text = fobj.read()
        fobj.seek(0)
        self.assertEqual(0, fobj.tell(), "seek() to file's start failed")
        fobj.seek(2048, 0)
        self.assertEqual(2048, fobj.tell(), 'seek() to absolute position failed')
        fobj.seek(-1024, 1)
        self.assertEqual(1024, fobj.tell(), 'seek() to negative relative position failed')
        fobj.seek(1024, 1)
        self.assertEqual(2048, fobj.tell(), 'seek() to positive relative position failed')
        s = fobj.read(10)
        self.assertEqual(s, data[2048:2058], 'read() after seek failed')
        fobj.seek(0, 2)
        self.assertEqual(tarinfo.size, fobj.tell(), "seek() to file's end failed")
        self.assertEqual(fobj.read(), b'', "read() at file's end did not return empty string")
        fobj.seek(-tarinfo.size, 2)
        self.assertEqual(0, fobj.tell(), "relative seek() to file's end failed")
        fobj.seek(512)
        s1 = fobj.readlines()
        fobj.seek(512)
        s2 = fobj.readlines()
        self.assertEqual(s1, s2, 'readlines() after seek failed')
        fobj.seek(0)
        self.assertEqual(len(fobj.readline()), fobj.tell(), 'tell() after readline() failed')
        fobj.seek(512)
        self.assertEqual(len(fobj.readline()) + 512, fobj.tell(), 'tell() after seek() and readline() failed')
        fobj.seek(0)
        line = fobj.readline()
        self.assertEqual(fobj.read(), data[len(line):], 'read() after readline() failed')
