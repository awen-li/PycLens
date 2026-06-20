# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_write_fields_not_in_fieldnames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.DictWriter(fileobj, fieldnames=['f1', 'f2', 'f3'])
        with self.assertRaises(ValueError) as cx:
            writer.writerow({'f4': 10, 'f2': 'spam', 1: 'abc'})
        exception = str(cx.exception)
        self.assertIn('fieldnames', exception)
        self.assertIn("'f4'", exception)
        self.assertNotIn("'f2'", exception)
        self.assertIn('1', exception)
