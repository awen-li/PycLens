# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestUnicode_test_unicode_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', newline='', encoding='utf-8') as fileobj:
        fileobj.write(','.join(self.names) + '\r\n')
        fileobj.seek(0)
        reader = csv.reader(fileobj)
        self.assertEqual(list(reader), [self.names])
