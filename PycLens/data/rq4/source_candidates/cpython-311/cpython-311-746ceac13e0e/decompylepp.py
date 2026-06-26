# Source Generated with Decompyle++
# File: cpython-311-746ceac13e0e.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    consts = [
        None,
        True,
        False,
        124,
        2,
        (0+3j),
        'unicode',
        b'bytes',
        (1, 2, 3)]
    code = (lambda .0: [ 'x={!r}'.format(const) for const in .0 ])(consts())
    code += '\nx = ...'
    consts.extend((Ellipsis, None))
    tree = ast.parse(code)
    self.assertEqual(self.get_load_const(tree), consts)
    for assign, const in zip(tree.body, consts):
        if not isinstance(assign, ast.Assign):
            raise ast.dump(assign)()
        new_node = ast.Constant(value = const)
        ast.copy_location(new_node, assign.value)
        assign.value = new_node
    self.assertEqual(self.get_load_const(tree), consts)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
