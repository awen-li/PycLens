# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: AnnotationsFutureTestCase_test_infinity_numbers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inf = '1e' + repr(sys.float_info.max_10_exp + 1)
    infj = f'{inf}j'
    self.assertAnnotationEqual('1e1000', expected=inf)
    self.assertAnnotationEqual('1e1000j', expected=infj)
    self.assertAnnotationEqual('-1e1000', expected=f'-{inf}')
    self.assertAnnotationEqual('3+1e1000j', expected=f'3 + {infj}')
    self.assertAnnotationEqual('(1e1000, 1e1000j)', expected=f'({inf}, {infj})')
    self.assertAnnotationEqual("'inf'")
    self.assertAnnotationEqual("('inf', 1e1000, 'infxxx', 1e1000j)", expected=f"('inf', {inf}, 'infxxx', {infj})")
    self.assertAnnotationEqual('(1e1000, (1e1000j,))', expected=f'({inf}, ({infj},))')
