# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextWithStatement_test_with_statements_gc3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = self.decimal.Context
    localcontext = self.decimal.localcontext
    getcontext = self.decimal.getcontext
    setcontext = self.decimal.setcontext
    with localcontext() as c1:
        del c1
        n1 = Context(prec=1)
        setcontext(n1)
        with localcontext(n1) as c2:
            del n1
            self.assertEqual(c2.prec, 1)
            del c2
            n2 = Context(prec=2)
            setcontext(n2)
            del n2
            self.assertEqual(getcontext().prec, 2)
            n3 = Context(prec=3)
            setcontext(n3)
            self.assertEqual(getcontext().prec, 3)
            with localcontext(n3) as c3:
                del n3
                self.assertEqual(c3.prec, 3)
                del c3
                n4 = Context(prec=4)
                setcontext(n4)
                del n4
                self.assertEqual(getcontext().prec, 4)
                with localcontext() as c4:
                    self.assertEqual(c4.prec, 4)
                    del c4
