# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_comments.py
# case: TypeCommentTests_test_func_type_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def parse_func_type_input(source):
        return ast.parse(source, '<unknown>', 'func_type')
    tree = parse_func_type_input('() -> int')
    self.assertEqual(tree.argtypes, [])
    self.assertEqual(tree.returns.id, 'int')
    tree = parse_func_type_input('(int) -> List[str]')
    self.assertEqual(len(tree.argtypes), 1)
    arg = tree.argtypes[0]
    self.assertEqual(arg.id, 'int')
    self.assertEqual(tree.returns.value.id, 'List')
    self.assertEqual(tree.returns.slice.id, 'str')
    tree = parse_func_type_input('(int, *str, **Any) -> float')
    self.assertEqual(tree.argtypes[0].id, 'int')
    self.assertEqual(tree.argtypes[1].id, 'str')
    self.assertEqual(tree.argtypes[2].id, 'Any')
    self.assertEqual(tree.returns.id, 'float')
    tree = parse_func_type_input('(*int) -> None')
    self.assertEqual(tree.argtypes[0].id, 'int')
    tree = parse_func_type_input('(**int) -> None')
    self.assertEqual(tree.argtypes[0].id, 'int')
    tree = parse_func_type_input('(*int, **str) -> None')
    self.assertEqual(tree.argtypes[0].id, 'int')
    self.assertEqual(tree.argtypes[1].id, 'str')
    with self.assertRaises(SyntaxError):
        tree = parse_func_type_input('(int, *str, *Any) -> float')
    with self.assertRaises(SyntaxError):
        tree = parse_func_type_input('(int, **str, Any) -> float')
    with self.assertRaises(SyntaxError):
        tree = parse_func_type_input('(**int, **str) -> float')
