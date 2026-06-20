# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestStringAnnotations_test_text_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test import dataclass_textanno
    self.assertEqual(get_type_hints(dataclass_textanno.Bar), {'foo': dataclass_textanno.Foo})
    self.assertEqual(get_type_hints(dataclass_textanno.Bar.__init__), {'foo': dataclass_textanno.Foo, 'return': type(None)})
