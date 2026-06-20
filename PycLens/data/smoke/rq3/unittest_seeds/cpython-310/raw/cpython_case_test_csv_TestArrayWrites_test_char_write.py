# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestArrayWrites_test_char_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import array, string
    a = array.array('u', string.ascii_letters)
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.writer(fileobj, dialect='excel')
        writer.writerow(a)
        expected = ','.join(a) + '\r\n'
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), expected)
