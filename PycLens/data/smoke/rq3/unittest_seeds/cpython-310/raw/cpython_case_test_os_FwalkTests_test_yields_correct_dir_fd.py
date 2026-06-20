# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FwalkTests_test_yields_correct_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (topdown, follow_symlinks) in itertools.product((True, False), repeat=2):
        args = (os_helper.TESTFN, topdown, None)
        for (root, dirs, files, rootfd) in self.fwalk(*args, follow_symlinks=follow_symlinks):
            os.fstat(rootfd)
            os.stat(rootfd)
            self.assertEqual(set(os.listdir(rootfd)), set(dirs) | set(files))
