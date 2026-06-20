# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextFlags_test_flags_irrelevant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    Inexact = self.decimal.Inexact
    Rounded = self.decimal.Rounded
    Underflow = self.decimal.Underflow
    Clamped = self.decimal.Clamped
    Subnormal = self.decimal.Subnormal

    def raise_error(context, flag):
        if self.decimal == C:
            context.flags[flag] = True
            if context.traps[flag]:
                raise flag
        else:
            context._raise_error(flag)
    context = Context(prec=9, Emin=-425000000, Emax=425000000, rounding=ROUND_HALF_EVEN, traps=[], flags=[])
    operations = [(context._apply, [Decimal('100E-425000010')]), (context.sqrt, [Decimal(2)]), (context.add, [Decimal('1.23456789'), Decimal('9.87654321')]), (context.multiply, [Decimal('1.23456789'), Decimal('9.87654321')]), (context.subtract, [Decimal('1.23456789'), Decimal('9.87654321')])]
    flagsets = [[Inexact], [Rounded], [Underflow], [Clamped], [Subnormal], [Inexact, Rounded, Underflow, Clamped, Subnormal]]
    for (fn, args) in operations:
        context.clear_flags()
        ans = fn(*args)
        flags = [k for (k, v) in context.flags.items() if v]
        for extra_flags in flagsets:
            context.clear_flags()
            for flag in extra_flags:
                raise_error(context, flag)
            new_ans = fn(*args)
            expected_flags = list(flags)
            for flag in extra_flags:
                if flag not in expected_flags:
                    expected_flags.append(flag)
            expected_flags.sort(key=id)
            new_flags = [k for (k, v) in context.flags.items() if v]
            new_flags.sort(key=id)
            self.assertEqual(ans, new_ans, 'operation produces different answers depending on flags set: ' + 'expected %s, got %s.' % (ans, new_ans))
            self.assertEqual(new_flags, expected_flags, 'operation raises different flags depending on flags set: ' + 'expected %s, got %s' % (expected_flags, new_flags))
