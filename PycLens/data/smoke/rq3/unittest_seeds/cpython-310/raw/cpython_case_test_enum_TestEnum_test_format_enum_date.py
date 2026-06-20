# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_format_enum_date

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Holiday = self.Holiday
    self.assertFormatIsValue('{}', Holiday.IDES_OF_MARCH)
    self.assertFormatIsValue('{:}', Holiday.IDES_OF_MARCH)
    self.assertFormatIsValue('{:20}', Holiday.IDES_OF_MARCH)
    self.assertFormatIsValue('{:^20}', Holiday.IDES_OF_MARCH)
    self.assertFormatIsValue('{:>20}', Holiday.IDES_OF_MARCH)
    self.assertFormatIsValue('{:<20}', Holiday.IDES_OF_MARCH)
    self.assertFormatIsValue('{:%Y %m}', Holiday.IDES_OF_MARCH)
    self.assertFormatIsValue('{:%Y %m %M:00}', Holiday.IDES_OF_MARCH)
