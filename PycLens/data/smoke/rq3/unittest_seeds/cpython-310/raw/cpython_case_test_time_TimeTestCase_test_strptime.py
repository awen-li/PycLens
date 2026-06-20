# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_strptime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tt = time.gmtime(self.t)
    for directive in ('a', 'A', 'b', 'B', 'c', 'd', 'H', 'I', 'j', 'm', 'M', 'p', 'S', 'U', 'w', 'W', 'x', 'X', 'y', 'Y', 'Z', '%'):
        format = '%' + directive
        strf_output = time.strftime(format, tt)
        try:
            time.strptime(strf_output, format)
        except ValueError:
            self.fail("conversion specifier %r failed with '%s' input." % (format, strf_output))
