# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_strftime_format_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in ['', 'A', '%A', '%AA']:
        for y in range(0, 16):
            for z in ['%', 'A%', 'AA%', '%A%', 'A%A%', '%#']:
                try:
                    time.strftime(x * y + z)
                except ValueError:
                    pass
