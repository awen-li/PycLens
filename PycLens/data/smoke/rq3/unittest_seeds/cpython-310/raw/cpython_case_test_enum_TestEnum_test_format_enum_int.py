# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_format_enum_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Grades = self.Grades
    self.assertFormatIsValue('{}', Grades.C)
    self.assertFormatIsValue('{:}', Grades.C)
    self.assertFormatIsValue('{:20}', Grades.C)
    self.assertFormatIsValue('{:^20}', Grades.C)
    self.assertFormatIsValue('{:>20}', Grades.C)
    self.assertFormatIsValue('{:<20}', Grades.C)
    self.assertFormatIsValue('{:+}', Grades.C)
    self.assertFormatIsValue('{:08X}', Grades.C)
    self.assertFormatIsValue('{:b}', Grades.C)
