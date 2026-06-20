# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: BasicUnicodeTest_test_encoding_map_type_initialized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from encodings import cp1140
    table_type = type(cp1140.encoding_table)
    self.assertEqual(table_type, table_type)
