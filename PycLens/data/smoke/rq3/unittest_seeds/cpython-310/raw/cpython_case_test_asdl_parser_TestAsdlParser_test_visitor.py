# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asdl_parser.py
# case: TestAsdlParser_test_visitor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CustomVisitor(self.asdl.VisitorBase):

        def __init__(self):
            super().__init__()
            self.names_with_seq = []

        def visitModule(self, mod):
            for dfn in mod.dfns:
                self.visit(dfn)

        def visitType(self, type):
            self.visit(type.value)

        def visitSum(self, sum):
            for t in sum.types:
                self.visit(t)

        def visitConstructor(self, cons):
            for f in cons.fields:
                if f.seq:
                    self.names_with_seq.append(cons.name)
    v = CustomVisitor()
    v.visit(self.types['mod'])
    self.assertEqual(v.names_with_seq, ['Module', 'Module', 'Interactive', 'FunctionType'])
