# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: RemoveDirsTests_test_remove_partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dira = os.path.join(os_helper.TESTFN, 'dira')
    os.mkdir(dira)
    dirb = os.path.join(dira, 'dirb')
    os.mkdir(dirb)
    create_file(os.path.join(dira, 'file.txt'))
    os.removedirs(dirb)
    self.assertFalse(os.path.exists(dirb))
    self.assertTrue(os.path.exists(dira))
    self.assertTrue(os.path.exists(os_helper.TESTFN))
