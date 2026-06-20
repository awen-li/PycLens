# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_property_method_not_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:
        _bar = 0
        property_called = False

        @property
        def bar(self):
            self.property_called = True
            return self._bar
    f = Foo()
    completer = rlcompleter.Completer(dict(f=f))
    self.assertEqual(completer.complete('f.b', 0), 'f.bar')
    self.assertFalse(f.property_called)
