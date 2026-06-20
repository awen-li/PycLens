# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_read_short

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', encoding='utf-8') as fileobj:
        fileobj.write('1,2,abc,4,5,6\r\n1,2,abc\r\n')
        fileobj.seek(0)
        reader = csv.DictReader(fileobj, fieldnames='1 2 3 4 5 6'.split(), restval='DEFAULT')
        self.assertEqual(next(reader), {'1': '1', '2': '2', '3': 'abc', '4': '4', '5': '5', '6': '6'})
        self.assertEqual(next(reader), {'1': '1', '2': '2', '3': 'abc', '4': 'DEFAULT', '5': 'DEFAULT', '6': 'DEFAULT'})
