# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestFormatAnnotation_test_typing_replacement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test.typinganndata.ann_module9 import ann, ann1
    self.assertEqual(inspect.formatannotation(ann), 'Union[List[str], int]')
    self.assertEqual(inspect.formatannotation(ann1), 'Union[List[testModule.typing.A], int]')
