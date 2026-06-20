# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_override_get_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NamespaceFormatter(string.Formatter):

        def __init__(self, namespace={}):
            string.Formatter.__init__(self)
            self.namespace = namespace

        def get_value(self, key, args, kwds):
            if isinstance(key, str):
                try:
                    return kwds[key]
                except KeyError:
                    return self.namespace[key]
            else:
                string.Formatter.get_value(key, args, kwds)
    fmt = NamespaceFormatter({'greeting': 'hello'})
    self.assertEqual(fmt.format('{greeting}, world!'), 'hello, world!')
