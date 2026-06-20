# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_strftime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tt = time.gmtime(self.t)
    for directive in ('a', 'A', 'b', 'B', 'c', 'd', 'H', 'I', 'j', 'm', 'M', 'p', 'S', 'U', 'w', 'W', 'x', 'X', 'y', 'Y', 'Z', '%'):
        format = ' %' + directive
        try:
            time.strftime(format, tt)
        except ValueError:
            self.fail('conversion specifier: %r failed.' % format)
    self.assertRaises(TypeError, time.strftime, b'%S', tt)
    self.assertRaises(ValueError, time.strftime, '%S\x00', tt)
