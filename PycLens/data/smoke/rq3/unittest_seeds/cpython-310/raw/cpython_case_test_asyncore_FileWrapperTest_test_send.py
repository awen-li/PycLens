# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: FileWrapperTest_test_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = b'Come again?'
    d2 = b'I want to buy some cheese.'
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_APPEND)
    w = asyncore.file_wrapper(fd)
    os.close(fd)
    w.write(d1)
    w.send(d2)
    w.close()
    with open(os_helper.TESTFN, 'rb') as file:
        self.assertEqual(file.read(), self.d + d1 + d2)
