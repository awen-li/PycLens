# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FwalkTests_test_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        fd = os.open('.', os.O_RDONLY)
        walk_kwargs = {'top': os_helper.TESTFN}
        fwalk_kwargs = walk_kwargs.copy()
        fwalk_kwargs['dir_fd'] = fd
        self._compare_to_walk(walk_kwargs, fwalk_kwargs)
    finally:
        os.close(fd)
