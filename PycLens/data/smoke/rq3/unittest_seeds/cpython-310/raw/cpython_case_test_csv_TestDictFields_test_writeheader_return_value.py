# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_writeheader_return_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.DictWriter(fileobj, fieldnames=['f1', 'f2', 'f3'])
        writeheader_return_value = writer.writeheader()
        self.assertEqual(writeheader_return_value, 10)
