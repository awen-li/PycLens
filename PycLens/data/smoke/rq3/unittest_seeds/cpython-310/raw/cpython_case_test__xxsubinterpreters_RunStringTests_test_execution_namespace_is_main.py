# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_execution_namespace_is_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    script = dedent(f"\n            spam = 42\n\n            ns = dict(vars())\n            ns['__builtins__'] = str(ns['__builtins__'])\n            import pickle\n            with open({w}, 'wb') as chan:\n                pickle.dump(ns, chan)\n            ")
    interpreters.run_string(self.id, script)
    with open(r, 'rb') as chan:
        ns = pickle.load(chan)
    ns.pop('__builtins__')
    ns.pop('__loader__')
    self.assertEqual(ns, {'__name__': '__main__', '__annotations__': {}, '__doc__': None, '__package__': None, '__spec__': None, 'spam': 42})
