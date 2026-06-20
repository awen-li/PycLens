# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_break_in_finally

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    count = 0
    while count < 2:
        count += 1
        try:
            pass
        finally:
            break
    self.assertEqual(count, 1)
    count = 0
    while count < 2:
        count += 1
        try:
            continue
        finally:
            break
    self.assertEqual(count, 1)
    count = 0
    while count < 2:
        count += 1
        try:
            1 / 0
        finally:
            break
    self.assertEqual(count, 1)
    for count in [0, 1]:
        self.assertEqual(count, 0)
        try:
            pass
        finally:
            break
    self.assertEqual(count, 0)
    for count in [0, 1]:
        self.assertEqual(count, 0)
        try:
            continue
        finally:
            break
    self.assertEqual(count, 0)
    for count in [0, 1]:
        self.assertEqual(count, 0)
        try:
            1 / 0
        finally:
            break
    self.assertEqual(count, 0)
