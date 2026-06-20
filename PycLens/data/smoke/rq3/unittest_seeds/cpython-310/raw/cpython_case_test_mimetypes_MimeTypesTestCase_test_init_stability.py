# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_init_stability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mimetypes.init()
    suffix_map = mimetypes.suffix_map
    encodings_map = mimetypes.encodings_map
    types_map = mimetypes.types_map
    common_types = mimetypes.common_types
    mimetypes.init()
    self.assertIsNot(suffix_map, mimetypes.suffix_map)
    self.assertIsNot(encodings_map, mimetypes.encodings_map)
    self.assertIsNot(types_map, mimetypes.types_map)
    self.assertIsNot(common_types, mimetypes.common_types)
    self.assertEqual(suffix_map, mimetypes.suffix_map)
    self.assertEqual(encodings_map, mimetypes.encodings_map)
    self.assertEqual(types_map, mimetypes.types_map)
    self.assertEqual(common_types, mimetypes.common_types)
