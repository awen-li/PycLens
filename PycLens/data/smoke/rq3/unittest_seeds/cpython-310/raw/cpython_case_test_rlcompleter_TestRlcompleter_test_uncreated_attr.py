# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_uncreated_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:
        __slots__ = ('bar',)
    completer = rlcompleter.Completer(dict(f=Foo()))
    self.assertEqual(completer.complete('f.', 0), 'f.bar')
