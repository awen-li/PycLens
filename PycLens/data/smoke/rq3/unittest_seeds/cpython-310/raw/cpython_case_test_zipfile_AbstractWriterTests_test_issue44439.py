# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractWriterTests_test_issue44439

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = array.array('Q', [1, 2, 3, 4, 5])
    LENGTH = len(q) * q.itemsize
    with zipfile.ZipFile(io.BytesIO(), 'w', self.compression) as zip:
        with zip.open('data', 'w') as data:
            self.assertEqual(data.write(q), LENGTH)
        self.assertEqual(zip.getinfo('data').file_size, LENGTH)
