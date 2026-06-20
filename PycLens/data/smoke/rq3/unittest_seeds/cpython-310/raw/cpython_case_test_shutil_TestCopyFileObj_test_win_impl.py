# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyFileObj_test_win_impl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with unittest.mock.patch('shutil._copyfileobj_readinto') as m:
        shutil.copyfile(TESTFN, TESTFN2)
    assert m.called
    self.assertEqual(m.call_args[0][2], 1 * 1024 * 1024)
    with tempfile.NamedTemporaryFile(dir=os.getcwd(), delete=False) as f:
        f.write(b'foo')
    fname = f.name
    self.addCleanup(os_helper.unlink, fname)
    with unittest.mock.patch('shutil._copyfileobj_readinto') as m:
        shutil.copyfile(fname, TESTFN2)
    self.assertEqual(m.call_args[0][2], 3)
    with tempfile.NamedTemporaryFile(dir=os.getcwd(), delete=False) as f:
        pass
    fname = f.name
    self.addCleanup(os_helper.unlink, fname)
    with unittest.mock.patch('shutil._copyfileobj_readinto') as m:
        shutil.copyfile(fname, TESTFN2)
    assert not m.called
    self.assert_files_eq(fname, TESTFN2)
