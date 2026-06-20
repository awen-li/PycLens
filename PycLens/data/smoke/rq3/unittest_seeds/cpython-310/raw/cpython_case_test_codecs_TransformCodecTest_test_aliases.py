# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_aliases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (codec_name, aliases) in transform_aliases.items():
        expected_name = codecs.lookup(codec_name).name
        for alias in aliases:
            with self.subTest(alias=alias):
                info = codecs.lookup(alias)
                self.assertEqual(info.name, expected_name)
