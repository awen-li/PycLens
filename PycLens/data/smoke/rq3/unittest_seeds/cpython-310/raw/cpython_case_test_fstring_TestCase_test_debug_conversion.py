# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_debug_conversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 'A string'
    self.assertEqual(f'x={x!r}', 'x=' + repr(x))
    self.assertEqual(f'x ={x!r}', 'x =' + repr(x))
    self.assertEqual(f'x={x!s}', 'x=' + str(x))
    self.assertEqual(f'x={x!r}', 'x=' + repr(x))
    self.assertEqual(f'x={x!a}', 'x=' + ascii(x))
    x = 2.71828
    self.assertEqual(f'x={x:.2f}', 'x=' + format(x, '.2f'))
    self.assertEqual(f'x={x:}', 'x=' + format(x, ''))
    self.assertEqual(f'x={x!r:^20}', 'x=' + format(repr(x), '^20'))
    self.assertEqual(f'x={x!s:^20}', 'x=' + format(str(x), '^20'))
    self.assertEqual(f'x={x!a:^20}', 'x=' + format(ascii(x), '^20'))
    x = 9
    self.assertEqual(f'3*x+15={3 * x + 15!r}', '3*x+15=42')
    tenπ = 31.4
    self.assertEqual(f'tenπ={tenπ:.2f}', 'tenπ=31.40')
    self.assertEqual(f""""Σ"={'Σ'!r}""", '"Σ"=\'Σ\'')
    self.assertEqual(f"{f'3.1415={3.1415:.1f}':*^20}", '*****3.1415=3.1*****')
    pi = 'π'
    self.assertEqual(f'alpha α pi={pi!r} ω omega', "alpha α pi='π' ω omega")
    self.assertEqual(f'\n3\n={3!r}', '\n3\n=3')
    self.assertEqual(f'{0 == 1}', 'False')
    self.assertEqual(f'{0 != 1}', 'True')
    self.assertEqual(f'{0 <= 1}', 'True')
    self.assertEqual(f'{0 >= 1}', 'False')
    self.assertEqual(f"{(x := '5')}", '5')
    self.assertEqual(x, '5')
    self.assertEqual(f'{(x := 5)}', '5')
    self.assertEqual(x, 5)
    self.assertEqual(f"{'='}", '=')
    x = 20
    self.assertEqual(f'{x:=10}', '        20')

    def f(a):
        nonlocal x
        oldx = x
        x = a
        return oldx
    x = 0
    self.assertEqual(f"{f(a='3=')}", '0')
    self.assertEqual(x, '3=')
    self.assertEqual(f'{f(a=4)}', '3=')
    self.assertEqual(x, 4)

    class C:

        def __format__(self, s):
            return f'FORMAT-{s}'

        def __repr__(self):
            return 'REPR'
    self.assertEqual(f'C()={C()!r}', 'C()=REPR')
    self.assertEqual(f'C()={C()!r}', 'C()=REPR')
    self.assertEqual(f'C()={C():}', 'C()=FORMAT-')
    self.assertEqual(f'C()={C(): }', 'C()=FORMAT- ')
    self.assertEqual(f'C()={C():x}', 'C()=FORMAT-x')
    self.assertEqual(f'C()={C()!r:*^20}', 'C()=********REPR********')
    self.assertRaises(SyntaxError, eval, "f'{C=]'")
    x = 'foo'
    self.assertEqual(f'Xx={x!r}Y', 'Xx=' + repr(x) + 'Y')
    self.assertEqual(f'Xx  ={x!r}Y', 'Xx  =' + repr(x) + 'Y')
    self.assertEqual(f'Xx=  {x!r}Y', 'Xx=  ' + repr(x) + 'Y')
    self.assertEqual(f'Xx  =  {x!r}Y', 'Xx  =  ' + repr(x) + 'Y')
