# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectValidity_test_escapechar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class mydialect(csv.Dialect):
        delimiter = ';'
        escapechar = '\\'
        doublequote = False
        skipinitialspace = True
        lineterminator = '\r\n'
        quoting = csv.QUOTE_NONE
    d = mydialect()
    self.assertEqual(d.escapechar, '\\')
    mydialect.escapechar = '**'
    with self.assertRaisesRegex(csv.Error, '"escapechar" must be a 1-character string'):
        mydialect()
    mydialect.escapechar = b'*'
    with self.assertRaisesRegex(csv.Error, '"escapechar" must be string or None, not bytes'):
        mydialect()
    mydialect.escapechar = 4
    with self.assertRaisesRegex(csv.Error, '"escapechar" must be string or None, not int'):
        mydialect()
