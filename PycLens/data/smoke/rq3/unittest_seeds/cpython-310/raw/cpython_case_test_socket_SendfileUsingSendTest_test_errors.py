# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: SendfileUsingSendTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'rb') as file:
        with socket.socket(type=socket.SOCK_DGRAM) as s:
            meth = self.meth_from_sock(s)
            self.assertRaisesRegex(ValueError, 'SOCK_STREAM', meth, file)
    with open(os_helper.TESTFN, encoding='utf-8') as file:
        with socket.socket() as s:
            meth = self.meth_from_sock(s)
            self.assertRaisesRegex(ValueError, 'binary mode', meth, file)
    with open(os_helper.TESTFN, 'rb') as file:
        with socket.socket() as s:
            meth = self.meth_from_sock(s)
            self.assertRaisesRegex(TypeError, 'positive integer', meth, file, count='2')
            self.assertRaisesRegex(TypeError, 'positive integer', meth, file, count=0.1)
            self.assertRaisesRegex(ValueError, 'positive integer', meth, file, count=0)
            self.assertRaisesRegex(ValueError, 'positive integer', meth, file, count=-1)
