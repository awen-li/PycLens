# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_modes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for mode in range(8):
        mode <<= 6
        with self.subTest(mode=format(mode, '03o')):
            d = self.do_create(recurse=3, dirs=2, files=2)
            with d:
                for (root, dirs, files) in os.walk(d.name, topdown=False):
                    for name in files:
                        os.chmod(os.path.join(root, name), mode)
                    os.chmod(root, mode)
                d.cleanup()
            self.assertFalse(os.path.exists(d.name))
