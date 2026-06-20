# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_writerows_legacy_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    c = _testcapi.unicode_legacy_string('a')
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([[c]])
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), 'a\r\n')
