# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectValidity_test_quoting

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
    self.assertEqual(d.quoting, csv.QUOTE_NONE)
    mydialect.quoting = None
    self.assertRaises(csv.Error, mydialect)
    mydialect.doublequote = True
    mydialect.quoting = csv.QUOTE_ALL
    mydialect.quotechar = '"'
    d = mydialect()
    self.assertEqual(d.quoting, csv.QUOTE_ALL)
    self.assertEqual(d.quotechar, '"')
    self.assertTrue(d.doublequote)
    mydialect.quotechar = "''"
    with self.assertRaises(csv.Error) as cm:
        mydialect()
    self.assertEqual(str(cm.exception), '"quotechar" must be a 1-character string')
    mydialect.quotechar = 4
    with self.assertRaises(csv.Error) as cm:
        mydialect()
    self.assertEqual(str(cm.exception), '"quotechar" must be string or None, not int')
