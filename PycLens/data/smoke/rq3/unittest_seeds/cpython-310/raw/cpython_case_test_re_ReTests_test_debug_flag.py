# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_debug_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pat = '(\\.)(?:[ch]|py)(?(1)$|: )'
    with captured_stdout() as out:
        re.compile(pat, re.DEBUG)
    self.maxDiff = None
    dump = "SUBPATTERN 1 0 0\n  LITERAL 46\nBRANCH\n  IN\n    LITERAL 99\n    LITERAL 104\nOR\n  LITERAL 112\n  LITERAL 121\nGROUPREF_EXISTS 1\n  AT AT_END\nELSE\n  LITERAL 58\n  LITERAL 32\n\n 0. INFO 8 0b1 2 5 (to 9)\n      prefix_skip 0\n      prefix [0x2e] ('.')\n      overlap [0]\n 9: MARK 0\n11. LITERAL 0x2e ('.')\n13. MARK 1\n15. BRANCH 10 (to 26)\n17.   IN 6 (to 24)\n19.     LITERAL 0x63 ('c')\n21.     LITERAL 0x68 ('h')\n23.     FAILURE\n24:   JUMP 9 (to 34)\n26: branch 7 (to 33)\n27.   LITERAL 0x70 ('p')\n29.   LITERAL 0x79 ('y')\n31.   JUMP 2 (to 34)\n33: FAILURE\n34: GROUPREF_EXISTS 0 6 (to 41)\n37. AT END\n39. JUMP 5 (to 45)\n41: LITERAL 0x3a (':')\n43. LITERAL 0x20 (' ')\n45: SUCCESS\n"
    self.assertEqual(out.getvalue(), dump)
    with captured_stdout() as out:
        re.compile(pat, re.DEBUG)
    self.assertEqual(out.getvalue(), dump)
