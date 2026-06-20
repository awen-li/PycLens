# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PosixPathTest_test_handling_bad_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        file_descriptors = list(pathlib.Path('/dev/fd').rglob('*'))[3:]
        if not file_descriptors:
            self.skipTest('no file descriptors - issue was not reproduced')
        for f in file_descriptors:
            f.exists()
            f.is_dir()
            f.is_file()
            f.is_symlink()
            f.is_block_device()
            f.is_char_device()
            f.is_fifo()
            f.is_socket()
    except OSError as e:
        if e.errno == errno.EBADF:
            self.fail('Bad file descriptor not handled.')
        raise
