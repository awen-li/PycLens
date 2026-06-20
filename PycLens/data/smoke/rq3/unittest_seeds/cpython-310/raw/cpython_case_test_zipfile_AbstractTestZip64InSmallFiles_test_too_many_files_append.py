# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestZip64InSmallFiles_test_too_many_files_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipf = zipfile.ZipFile(TESTFN, 'w', self.compression, allowZip64=False)
    zipf.debug = 100
    numfiles = 9
    for i in range(numfiles):
        zipf.writestr('foo%08d' % i, '%d' % (i ** 3 % 57))
    self.assertEqual(len(zipf.namelist()), numfiles)
    with self.assertRaises(zipfile.LargeZipFile):
        zipf.writestr('foo%08d' % numfiles, b'')
    self.assertEqual(len(zipf.namelist()), numfiles)
    zipf.close()
    zipf = zipfile.ZipFile(TESTFN, 'a', self.compression, allowZip64=False)
    zipf.debug = 100
    self.assertEqual(len(zipf.namelist()), numfiles)
    with self.assertRaises(zipfile.LargeZipFile):
        zipf.writestr('foo%08d' % numfiles, b'')
    self.assertEqual(len(zipf.namelist()), numfiles)
    zipf.close()
    zipf = zipfile.ZipFile(TESTFN, 'a', self.compression, allowZip64=True)
    zipf.debug = 100
    self.assertEqual(len(zipf.namelist()), numfiles)
    numfiles2 = 15
    for i in range(numfiles, numfiles2):
        zipf.writestr('foo%08d' % i, '%d' % (i ** 3 % 57))
    self.assertEqual(len(zipf.namelist()), numfiles2)
    zipf.close()
    zipf2 = zipfile.ZipFile(TESTFN, 'r', self.compression)
    self.assertEqual(len(zipf2.namelist()), numfiles2)
    for i in range(numfiles2):
        content = zipf2.read('foo%08d' % i).decode('ascii')
        self.assertEqual(content, '%d' % (i ** 3 % 57))
    zipf2.close()
