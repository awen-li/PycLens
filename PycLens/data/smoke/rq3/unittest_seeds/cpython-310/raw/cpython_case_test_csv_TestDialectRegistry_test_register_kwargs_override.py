# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_register_kwargs_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class mydialect(csv.Dialect):
        delimiter = '\t'
        quotechar = '"'
        doublequote = True
        skipinitialspace = False
        lineterminator = '\r\n'
        quoting = csv.QUOTE_MINIMAL
    name = 'test_dialect'
    csv.register_dialect(name, mydialect, delimiter=';', quotechar="'", doublequote=False, skipinitialspace=True, lineterminator='\n', quoting=csv.QUOTE_ALL)
    self.addCleanup(csv.unregister_dialect, name)
    dialect = csv.get_dialect(name)
    self.assertEqual(dialect.delimiter, ';')
    self.assertEqual(dialect.quotechar, "'")
    self.assertEqual(dialect.doublequote, False)
    self.assertEqual(dialect.skipinitialspace, True)
    self.assertEqual(dialect.lineterminator, '\n')
    self.assertEqual(dialect.quoting, csv.QUOTE_ALL)
