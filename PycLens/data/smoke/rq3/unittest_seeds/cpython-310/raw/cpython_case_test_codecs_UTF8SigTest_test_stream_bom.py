# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8SigTest_test_stream_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unistring = 'ABC¡∀XYZ'
    bytestring = codecs.BOM_UTF8 + b'ABC\xc2\xa1\xe2\x88\x80XYZ'
    reader = codecs.getreader('utf-8-sig')
    for sizehint in [None] + list(range(1, 11)) + [64, 128, 256, 512, 1024]:
        istream = reader(io.BytesIO(bytestring))
        ostream = io.StringIO()
        while 1:
            if sizehint is not None:
                data = istream.read(sizehint)
            else:
                data = istream.read()
            if not data:
                break
            ostream.write(data)
        got = ostream.getvalue()
        self.assertEqual(got, unistring)
