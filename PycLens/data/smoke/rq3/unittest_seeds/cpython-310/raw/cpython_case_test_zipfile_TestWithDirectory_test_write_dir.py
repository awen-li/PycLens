# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestWithDirectory_test_write_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirpath = os.path.join(TESTFN2, 'x')
    os.mkdir(dirpath)
    mode = os.stat(dirpath).st_mode & 65535
    with zipfile.ZipFile(TESTFN, 'w') as zipf:
        zipf.write(dirpath)
        zinfo = zipf.filelist[0]
        self.assertTrue(zinfo.filename.endswith('/x/'))
        self.assertEqual(zinfo.external_attr, mode << 16 | 16)
        zipf.write(dirpath, 'y')
        zinfo = zipf.filelist[1]
        self.assertTrue(zinfo.filename, 'y/')
        self.assertEqual(zinfo.external_attr, mode << 16 | 16)
    with zipfile.ZipFile(TESTFN, 'r') as zipf:
        zinfo = zipf.filelist[0]
        self.assertTrue(zinfo.filename.endswith('/x/'))
        self.assertEqual(zinfo.external_attr, mode << 16 | 16)
        zinfo = zipf.filelist[1]
        self.assertTrue(zinfo.filename, 'y/')
        self.assertEqual(zinfo.external_attr, mode << 16 | 16)
        target = os.path.join(TESTFN2, 'target')
        os.mkdir(target)
        zipf.extractall(target)
        self.assertTrue(os.path.isdir(os.path.join(target, 'y')))
        self.assertEqual(len(os.listdir(target)), 2)
