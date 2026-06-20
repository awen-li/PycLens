# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCheck_test_when_no_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = 'no_file.py'
    err = f'{path!r}: I/O Error: [Errno {errno.ENOENT}] {os.strerror(errno.ENOENT)}: {path!r}\n'
    self.verify_tabnanny_check(path, err=err)
