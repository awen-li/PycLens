# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectValidity_test_invalid_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def create_invalid(field_name, value):

        class mydialect(csv.Dialect):
            pass
        setattr(mydialect, field_name, value)
        d = mydialect()
    for field_name in ('delimiter', 'escapechar', 'quotechar'):
        with self.subTest(field_name=field_name):
            self.assertRaises(csv.Error, create_invalid, field_name, '')
            self.assertRaises(csv.Error, create_invalid, field_name, 'abc')
            self.assertRaises(csv.Error, create_invalid, field_name, b'x')
            self.assertRaises(csv.Error, create_invalid, field_name, 5)
