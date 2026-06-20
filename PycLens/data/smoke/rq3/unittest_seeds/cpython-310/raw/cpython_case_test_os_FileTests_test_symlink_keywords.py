# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_symlink_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    symlink = support.get_attribute(os, 'symlink')
    try:
        symlink(src='target', dst=os_helper.TESTFN, target_is_directory=False, dir_fd=None)
    except (NotImplementedError, OSError):
        pass
