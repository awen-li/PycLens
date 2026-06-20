# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectValidity_test_lineterminator

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
    self.assertEqual(d.lineterminator, '\r\n')
    mydialect.lineterminator = ':::'
    d = mydialect()
    self.assertEqual(d.lineterminator, ':::')
    mydialect.lineterminator = 4
    with self.assertRaises(csv.Error) as cm:
        mydialect()
    self.assertEqual(str(cm.exception), '"lineterminator" must be a string')
