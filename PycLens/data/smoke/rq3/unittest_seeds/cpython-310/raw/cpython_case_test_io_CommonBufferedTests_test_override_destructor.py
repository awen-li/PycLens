# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_override_destructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tp = self.tp
    record = []

    class MyBufferedIO(tp):

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
    rawio = self.MockRawIO()
    bufio = MyBufferedIO(rawio)
    del bufio
    support.gc_collect()
    self.assertEqual(record, [1, 2, 3])
