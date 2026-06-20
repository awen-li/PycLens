# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: SignatureTest_test_inspect_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    POS = inspect._ParameterKind.POSITIONAL_ONLY
    POS_KWD = inspect._ParameterKind.POSITIONAL_OR_KEYWORD
    pdict = {C: {'other': C.Decimal(1), 'third': C.Decimal(1), 'x': C.Decimal(1), 'y': C.Decimal(1), 'z': C.Decimal(1), 'a': C.Decimal(1), 'b': C.Decimal(1), 'c': C.Decimal(1), 'exp': C.Decimal(1), 'modulo': C.Decimal(1), 'num': '1', 'f': 1.0, 'rounding': C.ROUND_HALF_UP, 'context': C.getcontext()}, P: {'other': P.Decimal(1), 'third': P.Decimal(1), 'a': P.Decimal(1), 'b': P.Decimal(1), 'c': P.Decimal(1), 'exp': P.Decimal(1), 'modulo': P.Decimal(1), 'num': '1', 'f': 1.0, 'rounding': P.ROUND_HALF_UP, 'context': P.getcontext()}}

    def mkargs(module, sig):
        args = []
        kwargs = {}
        for (name, param) in sig.parameters.items():
            if name == 'self':
                continue
            if param.kind == POS:
                args.append(pdict[module][name])
            elif param.kind == POS_KWD:
                kwargs[name] = pdict[module][name]
            else:
                raise TestFailed('unexpected parameter kind')
        return (args, kwargs)

    def tr(s):
        """The C Context docstrings use 'x' in order to prevent confusion
               with the article 'a' in the descriptions."""
        if s == 'x':
            return 'a'
        if s == 'y':
            return 'b'
        if s == 'z':
            return 'c'
        return s

    def doit(ty):
        p_type = getattr(P, ty)
        c_type = getattr(C, ty)
        for attr in dir(p_type):
            if attr.startswith('_'):
                continue
            p_func = getattr(p_type, attr)
            c_func = getattr(c_type, attr)
            if inspect.isfunction(p_func):
                p_sig = inspect.signature(p_func)
                c_sig = inspect.signature(c_func)
                p_names = list(p_sig.parameters.keys())
                c_names = [tr(x) for x in c_sig.parameters.keys()]
                self.assertEqual(c_names, p_names, msg='parameter name mismatch in %s' % p_func)
                p_kind = [x.kind for x in p_sig.parameters.values()]
                c_kind = [x.kind for x in c_sig.parameters.values()]
                self.assertIs(p_kind[0], POS_KWD)
                self.assertIs(c_kind[0], POS)
                if ty == 'Decimal':
                    self.assertEqual(c_kind[1:], p_kind[1:], msg='parameter kind mismatch in %s' % p_func)
                else:
                    self.assertEqual(len(c_kind), len(p_kind), msg='parameter kind mismatch in %s' % p_func)
                (args, kwds) = mkargs(C, c_sig)
                try:
                    getattr(c_type(9), attr)(*args, **kwds)
                except Exception:
                    raise TestFailed('invalid signature for %s: %s %s' % (c_func, args, kwds))
                (args, kwds) = mkargs(P, p_sig)
                try:
                    getattr(p_type(9), attr)(*args, **kwds)
                except Exception:
                    raise TestFailed('invalid signature for %s: %s %s' % (p_func, args, kwds))
    doit('Decimal')
    doit('Context')
