# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestUnicode_test_unicode_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', newline='', encoding='utf-8') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerow(self.names)
        expected = ','.join(self.names) + '\r\n'
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), expected)
