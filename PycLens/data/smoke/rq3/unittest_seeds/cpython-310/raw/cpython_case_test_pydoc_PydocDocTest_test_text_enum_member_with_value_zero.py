# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_text_enum_member_with_value_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import enum

    class BinaryInteger(enum.IntEnum):
        zero = 0
        one = 1
    doc = pydoc.render_doc(BinaryInteger)
    self.assertIn('<BinaryInteger.zero: 0>', doc)
