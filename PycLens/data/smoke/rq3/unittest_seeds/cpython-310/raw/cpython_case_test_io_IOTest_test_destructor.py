# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_destructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    record = []

    class MyFileIO(self.FileIO):

        def __del__(self):
            record.append(1)
            try:
                f = super().__del__
            except AttributeError:
                pass
            else:
                f()

        def close(self):
            record.append(2)
            super().close()

        def flush(self):
            record.append(3)
            super().flush()
    with warnings_helper.check_warnings(('', ResourceWarning)):
        f = MyFileIO(os_helper.TESTFN, 'wb')
        f.write(b'xxx')
        del f
        support.gc_collect()
        self.assertEqual(record, [1, 2, 3])
        with self.open(os_helper.TESTFN, 'rb') as f:
            self.assertEqual(f.read(), b'xxx')
