# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_writerows

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BrokenFile:

        def write(self, buf):
            raise OSError
    writer = csv.writer(BrokenFile())
    self.assertRaises(OSError, writer.writerows, [['a']])
    with TemporaryFile('w+', encoding='utf-8', newline='') as fileobj:
        writer = csv.writer(fileobj)
        self.assertRaises(TypeError, writer.writerows, None)
        writer.writerows([['a', 'b'], ['c', 'd']])
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), 'a,b\r\nc,d\r\n')
