# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_as_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = types.SimpleNamespace(spam='spamspamspam')
    with self.assertRaises(TypeError):
        len(ns)
    with self.assertRaises(TypeError):
        iter(ns)
    with self.assertRaises(TypeError):
        'spam' in ns
    with self.assertRaises(TypeError):
        ns['spam']
