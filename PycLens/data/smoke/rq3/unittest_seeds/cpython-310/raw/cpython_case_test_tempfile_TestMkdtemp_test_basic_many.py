# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkdtemp_test_basic_many

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    extant = list(range(TEST_FILES))
    try:
        for i in extant:
            extant[i] = self.do_create(pre='aa')
    finally:
        for i in extant:
            if isinstance(i, str):
                os.rmdir(i)
