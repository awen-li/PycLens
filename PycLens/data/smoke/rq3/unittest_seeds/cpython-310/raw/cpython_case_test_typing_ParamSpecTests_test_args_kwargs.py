# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_args_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = ParamSpec('P')
    P_2 = ParamSpec('P_2')
    self.assertIn('args', dir(P))
    self.assertIn('kwargs', dir(P))
    self.assertIsInstance(P.args, ParamSpecArgs)
    self.assertIsInstance(P.kwargs, ParamSpecKwargs)
    self.assertIs(P.args.__origin__, P)
    self.assertIs(P.kwargs.__origin__, P)
    self.assertEqual(P.args, P.args)
    self.assertEqual(P.kwargs, P.kwargs)
    self.assertNotEqual(P.args, P_2.args)
    self.assertNotEqual(P.kwargs, P_2.kwargs)
    self.assertNotEqual(P.args, P.kwargs)
    self.assertNotEqual(P.kwargs, P.args)
    self.assertNotEqual(P.args, P_2.kwargs)
    self.assertEqual(repr(P.args), 'P.args')
    self.assertEqual(repr(P.kwargs), 'P.kwargs')
