# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_writerows_with_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([['a', None], [None, 'd']])
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), 'a,\r\n,d\r\n')
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([[None], ['a']])
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), '""\r\na\r\n')
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([['a'], [None]])
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), 'a\r\n""\r\n')
