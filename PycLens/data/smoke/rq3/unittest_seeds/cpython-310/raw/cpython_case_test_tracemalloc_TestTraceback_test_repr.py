# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTraceback_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def get_repr(*args) -> str:
        return repr(tracemalloc.Traceback(*args))
    self.assertEqual(get_repr(()), '<Traceback ()>')
    self.assertEqual(get_repr((), 0), '<Traceback () total_nframe=0>')
    frames = (('f1', 1), ('f2', 2))
    exp_repr_frames = "(<Frame filename='f2' lineno=2>, <Frame filename='f1' lineno=1>)"
    self.assertEqual(get_repr(frames), f'<Traceback {exp_repr_frames}>')
    self.assertEqual(get_repr(frames, 2), f'<Traceback {exp_repr_frames} total_nframe=2>')
