# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_read_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', encoding='utf-8') as fileobj:
        fileobj.write('1,2,abc,4,5,6\r\n')
        fileobj.seek(0)
        reader = csv.DictReader(fileobj, fieldnames=['f1', 'f2'])
        self.assertEqual(next(reader), {'f1': '1', 'f2': '2', None: ['abc', '4', '5', '6']})
