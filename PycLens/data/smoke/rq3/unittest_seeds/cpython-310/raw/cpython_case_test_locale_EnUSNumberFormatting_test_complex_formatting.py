# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: EnUSNumberFormatting_test_complex_formatting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_format_string('One million is %i', 1000000, grouping=1, out='One million is 1%s000%s000' % (self.sep, self.sep))
    self._test_format_string('One  million is %i', 1000000, grouping=1, out='One  million is 1%s000%s000' % (self.sep, self.sep))
    self._test_format_string('.%f.', 1000.0, out='.1000.000000.')
    if self.sep:
        self._test_format_string('-->  %10.2f', 4200, grouping=1, out='-->  ' + ('4%s200.00' % self.sep).rjust(10))
    self._test_format_string('%10.*f', (2, 1000), grouping=0, out='1000.00'.rjust(10))
    if self.sep:
        self._test_format_string('%*.*f', (10, 2, 1000), grouping=1, out=('1%s000.00' % self.sep).rjust(10))
    if self.sep:
        self._test_format_string('int %i float %.2f str %s', (1000, 1000.0, 'str'), grouping=1, out='int 1%s000 float 1%s000.00 str str' % (self.sep, self.sep))
