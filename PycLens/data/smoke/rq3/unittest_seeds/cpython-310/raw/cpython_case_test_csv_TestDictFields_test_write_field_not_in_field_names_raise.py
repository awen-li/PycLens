# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_write_field_not_in_field_names_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fileobj = StringIO()
    writer = csv.DictWriter(fileobj, ['f1', 'f2'], extrasaction='raise')
    dictrow = {'f0': 0, 'f1': 1, 'f2': 2, 'f3': 3}
    self.assertRaises(ValueError, csv.DictWriter.writerow, writer, dictrow)
