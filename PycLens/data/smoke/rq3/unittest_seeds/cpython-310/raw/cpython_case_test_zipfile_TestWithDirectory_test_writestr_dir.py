# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestWithDirectory_test_writestr_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(os.path.join(TESTFN2, 'x'))
    with zipfile.ZipFile(TESTFN, 'w') as zipf:
        zipf.writestr('x/', b'')
        zinfo = zipf.filelist[0]
        self.assertEqual(zinfo.filename, 'x/')
        self.assertEqual(zinfo.external_attr, 16893 << 16 | 16)
    with zipfile.ZipFile(TESTFN, 'r') as zipf:
        zinfo = zipf.filelist[0]
        self.assertTrue(zinfo.filename.endswith('x/'))
        self.assertEqual(zinfo.external_attr, 16893 << 16 | 16)
        target = os.path.join(TESTFN2, 'target')
        os.mkdir(target)
        zipf.extractall(target)
        self.assertTrue(os.path.isdir(os.path.join(target, 'x')))
        self.assertEqual(os.listdir(target), ['x'])
