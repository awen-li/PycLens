# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test__sendfile_use_sendfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class File:

        def __init__(self, fd):
            self.fd = fd

        def fileno(self):
            return self.fd
    with socket.socket() as sock:
        fd = os.open(os.curdir, os.O_RDONLY)
        os.close(fd)
        with self.assertRaises(socket._GiveupOnSendfile):
            sock._sendfile_use_sendfile(File(fd))
        with self.assertRaises(OverflowError):
            sock._sendfile_use_sendfile(File(2 ** 1000))
        with self.assertRaises(TypeError):
            sock._sendfile_use_sendfile(File(None))
