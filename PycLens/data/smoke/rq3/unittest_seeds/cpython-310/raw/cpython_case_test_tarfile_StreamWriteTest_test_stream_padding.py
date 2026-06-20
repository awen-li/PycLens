# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: StreamWriteTest_test_stream_padding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tmpname, self.mode)
    tar.close()
    if self.decompressor:
        dec = self.decompressor()
        with open(tmpname, 'rb') as fobj:
            data = fobj.read()
        data = dec.decompress(data)
        self.assertFalse(dec.unused_data, 'found trailing data')
    else:
        with self.open(tmpname) as fobj:
            data = fobj.read()
    self.assertEqual(data.count(b'\x00'), tarfile.RECORDSIZE, 'incorrect zero padding')
