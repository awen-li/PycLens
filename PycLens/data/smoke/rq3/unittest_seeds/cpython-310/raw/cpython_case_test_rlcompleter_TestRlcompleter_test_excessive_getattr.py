# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_excessive_getattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:
        calls = 0
        bar = ''

        def __getattribute__(self, name):
            if name == 'bar':
                self.calls += 1
                return None
            return super().__getattribute__(name)
    f = Foo()
    completer = rlcompleter.Completer(dict(f=f))
    self.assertEqual(completer.complete('f.b', 0), 'f.bar')
    self.assertEqual(f.calls, 1)
