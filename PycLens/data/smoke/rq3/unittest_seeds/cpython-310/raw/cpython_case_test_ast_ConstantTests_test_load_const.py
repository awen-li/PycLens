# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_load_const

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    consts = [None, True, False, 124, 2.0, 3j, 'unicode', b'bytes', (1, 2, 3)]
    code = '\n'.join(['x={!r}'.format(const) for const in consts])
    code += '\nx = ...'
    consts.extend((Ellipsis, None))
    tree = ast.parse(code)
    self.assertEqual(self.get_load_const(tree), consts)
    for (assign, const) in zip(tree.body, consts):
        assert isinstance(assign, ast.Assign), ast.dump(assign)
        new_node = ast.Constant(value=const)
        ast.copy_location(new_node, assign.value)
        assign.value = new_node
    self.assertEqual(self.get_load_const(tree), consts)
