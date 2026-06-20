# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: FileWrapperTest_test_resource_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    f = asyncore.file_wrapper(fd)
    os.close(fd)
    with warnings_helper.check_warnings(('', ResourceWarning)):
        f = None
        support.gc_collect()
