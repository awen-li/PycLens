# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: StreamReadTest_test_provoke_stream_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfos = self.tar.getmembers()
    with self.tar.extractfile(tarinfos[0]) as f:
        self.assertRaises(tarfile.StreamError, f.read)
