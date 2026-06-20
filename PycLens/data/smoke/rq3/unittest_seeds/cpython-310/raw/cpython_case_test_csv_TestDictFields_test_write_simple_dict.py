# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_write_simple_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.DictWriter(fileobj, fieldnames=['f1', 'f2', 'f3'])
        writer.writeheader()
        fileobj.seek(0)
        self.assertEqual(fileobj.readline(), 'f1,f2,f3\r\n')
        writer.writerow({'f1': 10, 'f3': 'abc'})
        fileobj.seek(0)
        fileobj.readline()
        self.assertEqual(fileobj.read(), '10,,abc\r\n')
