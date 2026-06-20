# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_flush_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_flush_error_on_close(os_helper.TESTFN, 'wb', buffering=0)
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_CREAT)
    self.check_flush_error_on_close(fd, 'wb', buffering=0)
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_CREAT)
    self.check_flush_error_on_close(fd, 'wb', buffering=0, closefd=False)
    os.close(fd)
    self.check_flush_error_on_close(os_helper.TESTFN, 'wb')
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_CREAT)
    self.check_flush_error_on_close(fd, 'wb')
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_CREAT)
    self.check_flush_error_on_close(fd, 'wb', closefd=False)
    os.close(fd)
    self.check_flush_error_on_close(os_helper.TESTFN, 'w', encoding='utf-8')
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_CREAT)
    self.check_flush_error_on_close(fd, 'w', encoding='utf-8')
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_CREAT)
    self.check_flush_error_on_close(fd, 'w', encoding='utf-8', closefd=False)
    os.close(fd)
