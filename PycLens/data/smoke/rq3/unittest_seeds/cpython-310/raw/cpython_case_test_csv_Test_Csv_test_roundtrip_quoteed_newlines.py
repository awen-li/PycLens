# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_roundtrip_quoteed_newlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.writer(fileobj)
        rows = [['a\nb', 'b'], ['c', 'x\r\nd']]
        writer.writerows(rows)
        fileobj.seek(0)
        for (i, row) in enumerate(csv.reader(fileobj)):
            self.assertEqual(row, rows[i])
