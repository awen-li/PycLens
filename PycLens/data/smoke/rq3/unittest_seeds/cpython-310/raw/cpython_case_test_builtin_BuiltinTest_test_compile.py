# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_compile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compile('print(1)\n', '', 'exec')
    bom = b'\xef\xbb\xbf'
    compile(bom + b'print(1)\n', '', 'exec')
    compile(source='pass', filename='?', mode='exec')
    compile(dont_inherit=False, filename='tmp', source='0', mode='eval')
    compile('pass', '?', dont_inherit=True, mode='exec')
    compile(memoryview(b'text'), 'name', 'exec')
    self.assertRaises(TypeError, compile)
    self.assertRaises(ValueError, compile, 'print(42)\n', '<string>', 'badmode')
    self.assertRaises(ValueError, compile, 'print(42)\n', '<string>', 'single', 255)
    self.assertRaises(ValueError, compile, chr(0), 'f', 'exec')
    self.assertRaises(TypeError, compile, 'pass', '?', 'exec', mode='eval', source='0', filename='tmp')
    compile('print("å")\n', '', 'exec')
    self.assertRaises(ValueError, compile, chr(0), 'f', 'exec')
    self.assertRaises(ValueError, compile, str('a = 1'), 'f', 'bad')
    codestr = 'def f():\n        """doc"""\n        debug_enabled = False\n        if __debug__:\n            debug_enabled = True\n        try:\n            assert False\n        except AssertionError:\n            return (True, f.__doc__, debug_enabled, __debug__)\n        else:\n            return (False, f.__doc__, debug_enabled, __debug__)\n        '

    def f():
        """doc"""
    values = [(-1, __debug__, f.__doc__, __debug__, __debug__), (0, True, 'doc', True, True), (1, False, 'doc', False, False), (2, False, None, False, False)]
    for (optval, *expected) in values:
        codeobjs = []
        codeobjs.append(compile(codestr, '<test>', 'exec', optimize=optval))
        tree = ast.parse(codestr)
        codeobjs.append(compile(tree, '<test>', 'exec', optimize=optval))
        for code in codeobjs:
            ns = {}
            exec(code, ns)
            rv = ns['f']()
            self.assertEqual(rv, tuple(expected))
