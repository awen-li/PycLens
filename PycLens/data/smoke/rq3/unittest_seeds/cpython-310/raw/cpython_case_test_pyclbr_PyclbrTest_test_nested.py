# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyclbr.py
# case: PyclbrTest_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mb = pyclbr
    (m, p, f, t, i) = ('test', '', 'test.py', {}, None)
    source = dedent('        def f0():\n            def f1(a,b,c):\n                def f2(a=1, b=2, c=3): pass\n                return f1(a,b,d)\n            class c1: pass\n        class C0:\n            "Test class."\n            def F1():\n                "Method."\n                return \'return\'\n            class C1():\n                class C2:\n                    "Class nested within nested class."\n                    def F3(): return 1+1\n\n        ')
    actual = mb._create_tree(m, p, f, source, t, i)
    f0 = mb.Function(m, 'f0', f, 1, end_lineno=5)
    f1 = mb._nest_function(f0, 'f1', 2, 4)
    f2 = mb._nest_function(f1, 'f2', 3, 3)
    c1 = mb._nest_class(f0, 'c1', 5, 5)
    C0 = mb.Class(m, 'C0', None, f, 6, end_lineno=14)
    F1 = mb._nest_function(C0, 'F1', 8, 10)
    C1 = mb._nest_class(C0, 'C1', 11, 14)
    C2 = mb._nest_class(C1, 'C2', 12, 14)
    F3 = mb._nest_function(C2, 'F3', 14, 14)
    expected = {'f0': f0, 'C0': C0}

    def compare(parent1, children1, parent2, children2):
        """Return equality of tree pairs.

            Each parent,children pair define a tree.  The parents are
            assumed equal.  Comparing the children dictionaries as such
            does not work due to comparison by identity and double
            linkage.  We separate comparing string and number attributes
            from comparing the children of input children.
            """
        self.assertEqual(children1.keys(), children2.keys())
        for ob in children1.values():
            self.assertIs(ob.parent, parent1)
        for ob in children2.values():
            self.assertIs(ob.parent, parent2)
        for key in children1.keys():
            (o1, o2) = (children1[key], children2[key])
            t1 = (type(o1), o1.name, o1.file, o1.module, o1.lineno, o1.end_lineno)
            t2 = (type(o2), o2.name, o2.file, o2.module, o2.lineno, o2.end_lineno)
            self.assertEqual(t1, t2)
            if type(o1) is mb.Class:
                self.assertEqual(o1.methods, o2.methods)
            compare(o1, o1.children, o2, o2.children)
    compare(None, actual, None, expected)
