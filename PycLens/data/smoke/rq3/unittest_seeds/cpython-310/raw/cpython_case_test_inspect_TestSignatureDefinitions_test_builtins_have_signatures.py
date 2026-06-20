# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureDefinitions_test_builtins_have_signatures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    no_signature = set()
    needs_groups = {'range', 'slice', 'dir', 'getattr', 'next', 'iter', 'vars'}
    no_signature |= needs_groups
    needs_null = {'anext'}
    no_signature |= needs_null
    needs_semantic_update = {'round'}
    no_signature |= needs_semantic_update
    needs_varargs = {'breakpoint', 'min', 'max', 'print', '__build_class__'}
    no_signature |= needs_varargs
    not_converted_yet = {'open', '__import__'}
    no_signature |= not_converted_yet
    types_with_signatures = set()
    ns = vars(builtins)
    for (name, obj) in sorted(ns.items()):
        if not callable(obj):
            continue
        if isinstance(obj, type) and name not in types_with_signatures:
            no_signature.add(name)
        if name in no_signature:
            continue
        with self.subTest(builtin=name):
            self.assertIsNotNone(inspect.signature(obj))
    for name in no_signature:
        with self.subTest(builtin=name):
            self.assertIsNone(obj.__text_signature__)
