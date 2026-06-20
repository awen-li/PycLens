# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_makefile_invalid_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for mode in ('rt', 'x', '+', 'a'):
        with self.subTest(mode=mode):
            with socket.socket() as sock:
                with self.assertRaisesRegex(ValueError, 'invalid mode'):
                    sock.makefile(mode)
