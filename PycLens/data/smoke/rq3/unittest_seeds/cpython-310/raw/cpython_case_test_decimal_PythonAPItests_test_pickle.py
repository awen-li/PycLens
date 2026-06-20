# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        Decimal = self.decimal.Decimal
        savedecimal = sys.modules['decimal']
        sys.modules['decimal'] = self.decimal
        d = Decimal('-3.141590000')
        p = pickle.dumps(d, proto)
        e = pickle.loads(p)
        self.assertEqual(d, e)
        if C:
            x = C.Decimal('-3.123e81723')
            y = P.Decimal('-3.123e81723')
            sys.modules['decimal'] = C
            sx = pickle.dumps(x, proto)
            sys.modules['decimal'] = P
            r = pickle.loads(sx)
            self.assertIsInstance(r, P.Decimal)
            self.assertEqual(r, y)
            sys.modules['decimal'] = P
            sy = pickle.dumps(y, proto)
            sys.modules['decimal'] = C
            r = pickle.loads(sy)
            self.assertIsInstance(r, C.Decimal)
            self.assertEqual(r, x)
            x = C.Decimal('-3.123e81723').as_tuple()
            y = P.Decimal('-3.123e81723').as_tuple()
            sys.modules['decimal'] = C
            sx = pickle.dumps(x, proto)
            sys.modules['decimal'] = P
            r = pickle.loads(sx)
            self.assertIsInstance(r, P.DecimalTuple)
            self.assertEqual(r, y)
            sys.modules['decimal'] = P
            sy = pickle.dumps(y, proto)
            sys.modules['decimal'] = C
            r = pickle.loads(sy)
            self.assertIsInstance(r, C.DecimalTuple)
            self.assertEqual(r, x)
        sys.modules['decimal'] = savedecimal
