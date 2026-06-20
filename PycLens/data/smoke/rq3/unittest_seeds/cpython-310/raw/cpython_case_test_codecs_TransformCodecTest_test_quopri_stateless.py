# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_quopri_stateless

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoded = codecs.encode(b'space tab\teol \n', 'quopri-codec')
    self.assertEqual(encoded, b'space=20tab=09eol=20\n')
    unescaped = b'space tab eol\n'
    self.assertEqual(codecs.decode(unescaped, 'quopri-codec'), unescaped)
