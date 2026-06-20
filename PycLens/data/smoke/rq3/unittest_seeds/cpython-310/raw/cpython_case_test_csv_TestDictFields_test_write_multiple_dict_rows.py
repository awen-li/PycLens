# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_write_multiple_dict_rows

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fileobj = StringIO()
    writer = csv.DictWriter(fileobj, fieldnames=['f1', 'f2', 'f3'])
    writer.writeheader()
    self.assertEqual(fileobj.getvalue(), 'f1,f2,f3\r\n')
    writer.writerows([{'f1': 1, 'f2': 'abc', 'f3': 'f'}, {'f1': 2, 'f2': 5, 'f3': 'xyz'}])
    self.assertEqual(fileobj.getvalue(), 'f1,f2,f3\r\n1,abc,f\r\n2,5,xyz\r\n')
