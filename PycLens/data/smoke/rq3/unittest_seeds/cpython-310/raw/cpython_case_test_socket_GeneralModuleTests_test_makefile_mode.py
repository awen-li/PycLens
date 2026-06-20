# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_makefile_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for mode in ('r', 'rb', 'rw', 'w', 'wb'):
        with self.subTest(mode=mode):
            with socket.socket() as sock:
                encoding = None if 'b' in mode else 'utf-8'
                with sock.makefile(mode, encoding=encoding) as fp:
                    self.assertEqual(fp.mode, mode)
