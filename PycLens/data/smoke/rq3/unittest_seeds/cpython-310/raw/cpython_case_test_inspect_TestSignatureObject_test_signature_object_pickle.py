# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_object_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a, b, *, c: 1={}, **kw) -> {42: 'ham'}:
        pass
    foo_partial = functools.partial(foo, a=1)
    sig = inspect.signature(foo_partial)
    for ver in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(pickle_ver=ver, subclass=False):
            sig_pickled = pickle.loads(pickle.dumps(sig, ver))
            self.assertEqual(sig, sig_pickled)
    sig = inspect.signature(foo)
    myparam = MyParameter(name='z', kind=inspect.Parameter.POSITIONAL_ONLY)
    myparams = collections.OrderedDict(sig.parameters, a=myparam)
    mysig = MySignature().replace(parameters=myparams.values(), return_annotation=sig.return_annotation)
    self.assertTrue(isinstance(mysig, MySignature))
    self.assertTrue(isinstance(mysig.parameters['z'], MyParameter))
    for ver in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(pickle_ver=ver, subclass=True):
            sig_pickled = pickle.loads(pickle.dumps(mysig, ver))
            self.assertEqual(mysig, sig_pickled)
            self.assertTrue(isinstance(sig_pickled, MySignature))
            self.assertTrue(isinstance(sig_pickled.parameters['z'], MyParameter))
