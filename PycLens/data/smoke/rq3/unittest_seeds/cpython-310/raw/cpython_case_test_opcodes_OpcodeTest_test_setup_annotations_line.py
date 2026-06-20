# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_opcodes.py
# case: OpcodeTest_test_setup_annotations_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with open(ann_module.__file__, encoding='utf-8') as f:
            txt = f.read()
        co = compile(txt, ann_module.__file__, 'exec')
        self.assertEqual(co.co_firstlineno, 1)
    except OSError:
        pass
