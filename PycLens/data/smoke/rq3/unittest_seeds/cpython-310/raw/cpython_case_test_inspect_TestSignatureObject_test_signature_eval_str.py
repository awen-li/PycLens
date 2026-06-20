# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_eval_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    isa = inspect_stringized_annotations
    sig = inspect.Signature
    par = inspect.Parameter
    PORK = inspect.Parameter.POSITIONAL_OR_KEYWORD
    for signature_func in (inspect.signature, inspect.Signature.from_callable):
        with self.subTest(signature_func=signature_func):
            self.assertEqual(signature_func(isa.MyClass), sig(parameters=(par('a', PORK), par('b', PORK))))
            self.assertEqual(signature_func(isa.function), sig(return_annotation='MyClass', parameters=(par('a', PORK, annotation='int'), par('b', PORK, annotation='str'))))
            self.assertEqual(signature_func(isa.function2), sig(return_annotation='MyClass', parameters=(par('a', PORK, annotation='int'), par('b', PORK, annotation="'str'"), par('c', PORK, annotation='MyClass'))))
            self.assertEqual(signature_func(isa.function3), sig(parameters=(par('a', PORK, annotation="'int'"), par('b', PORK, annotation="'str'"), par('c', PORK, annotation="'MyClass'"))))
            self.assertEqual(signature_func(isa.UnannotatedClass), sig())
            self.assertEqual(signature_func(isa.unannotated_function), sig(parameters=(par('a', PORK), par('b', PORK), par('c', PORK))))
            self.assertEqual(signature_func(isa.MyClass, eval_str=True), sig(parameters=(par('a', PORK), par('b', PORK))))
            self.assertEqual(signature_func(isa.function, eval_str=True), sig(return_annotation=isa.MyClass, parameters=(par('a', PORK, annotation=int), par('b', PORK, annotation=str))))
            self.assertEqual(signature_func(isa.function2, eval_str=True), sig(return_annotation=isa.MyClass, parameters=(par('a', PORK, annotation=int), par('b', PORK, annotation='str'), par('c', PORK, annotation=isa.MyClass))))
            self.assertEqual(signature_func(isa.function3, eval_str=True), sig(parameters=(par('a', PORK, annotation='int'), par('b', PORK, annotation='str'), par('c', PORK, annotation='MyClass'))))
            globalns = {'int': float, 'str': complex}
            localns = {'str': tuple, 'MyClass': dict}
            with self.assertRaises(NameError):
                signature_func(isa.function, eval_str=True, globals=globalns)
            self.assertEqual(signature_func(isa.function, eval_str=True, locals=localns), sig(return_annotation=dict, parameters=(par('a', PORK, annotation=int), par('b', PORK, annotation=tuple))))
            self.assertEqual(signature_func(isa.function, eval_str=True, globals=globalns, locals=localns), sig(return_annotation=dict, parameters=(par('a', PORK, annotation=float), par('b', PORK, annotation=tuple))))
