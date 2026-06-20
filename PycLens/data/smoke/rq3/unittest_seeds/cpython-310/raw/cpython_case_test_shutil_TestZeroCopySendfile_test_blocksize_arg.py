# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestZeroCopySendfile_test_blocksize_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with unittest.mock.patch('os.sendfile', side_effect=ZeroDivisionError) as m:
        self.assertRaises(ZeroDivisionError, shutil.copyfile, TESTFN, TESTFN2)
        blocksize = m.call_args[0][3]
        self.assertEqual(blocksize, os.path.getsize(TESTFN))
        os_helper.unlink(TESTFN2)
        write_file(TESTFN2, b'hello', binary=True)
        self.addCleanup(os_helper.unlink, TESTFN2 + '3')
        self.assertRaises(ZeroDivisionError, shutil.copyfile, TESTFN2, TESTFN2 + '3')
        blocksize = m.call_args[0][3]
        self.assertEqual(blocksize, 2 ** 23)
