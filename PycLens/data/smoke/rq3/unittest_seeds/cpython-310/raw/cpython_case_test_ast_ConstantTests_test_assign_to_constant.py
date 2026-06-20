# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_assign_to_constant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ast.parse('x = 1')
    target = tree.body[0].targets[0]
    new_target = ast.Constant(value=1)
    ast.copy_location(new_target, target)
    tree.body[0].targets[0] = new_target
    with self.assertRaises(ValueError) as cm:
        compile(tree, 'string', 'exec')
    self.assertEqual(str(cm.exception), "expression which can't be assigned to in Store context")
