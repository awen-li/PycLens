# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_literal_eval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ast.parse('1 + 2')
    binop = tree.body[0].value
    new_left = ast.Constant(value=10)
    ast.copy_location(new_left, binop.left)
    binop.left = new_left
    new_right = ast.Constant(value=20j)
    ast.copy_location(new_right, binop.right)
    binop.right = new_right
    self.assertEqual(ast.literal_eval(binop), 10 + 20j)
