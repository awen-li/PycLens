# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: NodeVisitorTests_test_old_constant_nodes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Visitor(ast.NodeVisitor):

        def visit_Num(self, node):
            log.append((node.lineno, 'Num', node.n))

        def visit_Str(self, node):
            log.append((node.lineno, 'Str', node.s))

        def visit_Bytes(self, node):
            log.append((node.lineno, 'Bytes', node.s))

        def visit_NameConstant(self, node):
            log.append((node.lineno, 'NameConstant', node.value))

        def visit_Ellipsis(self, node):
            log.append((node.lineno, 'Ellipsis', ...))
    mod = ast.parse(dedent("            i = 42\n            f = 4.25\n            c = 4.25j\n            s = 'string'\n            b = b'bytes'\n            t = True\n            n = None\n            e = ...\n            "))
    visitor = Visitor()
    log = []
    with warnings.catch_warnings(record=True) as wlog:
        warnings.filterwarnings('always', '', DeprecationWarning)
        visitor.visit(mod)
    self.assertEqual(log, [(1, 'Num', 42), (2, 'Num', 4.25), (3, 'Num', 4.25j), (4, 'Str', 'string'), (5, 'Bytes', b'bytes'), (6, 'NameConstant', True), (7, 'NameConstant', None), (8, 'Ellipsis', ...)])
    self.assertEqual([str(w.message) for w in wlog], ['visit_Num is deprecated; add visit_Constant', 'visit_Num is deprecated; add visit_Constant', 'visit_Num is deprecated; add visit_Constant', 'visit_Str is deprecated; add visit_Constant', 'visit_Bytes is deprecated; add visit_Constant', 'visit_NameConstant is deprecated; add visit_Constant', 'visit_NameConstant is deprecated; add visit_Constant', 'visit_Ellipsis is deprecated; add visit_Constant'])
