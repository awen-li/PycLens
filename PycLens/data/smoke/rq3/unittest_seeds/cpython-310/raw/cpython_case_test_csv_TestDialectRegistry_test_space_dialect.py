# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_space_dialect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class space(csv.excel):
        delimiter = ' '
        quoting = csv.QUOTE_NONE
        escapechar = '\\'
    with TemporaryFile('w+', encoding='utf-8') as fileobj:
        fileobj.write('abc def\nc1ccccc1 benzene\n')
        fileobj.seek(0)
        reader = csv.reader(fileobj, dialect=space())
        self.assertEqual(next(reader), ['abc', 'def'])
        self.assertEqual(next(reader), ['c1ccccc1', 'benzene'])
