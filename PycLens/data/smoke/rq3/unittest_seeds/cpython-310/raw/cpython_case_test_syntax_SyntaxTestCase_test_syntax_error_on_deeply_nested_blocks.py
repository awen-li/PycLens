# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_syntax_error_on_deeply_nested_blocks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = '\nwhile 1:\n while 2:\n  while 3:\n   while 4:\n    while 5:\n     while 6:\n      while 8:\n       while 9:\n        while 10:\n         while 11:\n          while 12:\n           while 13:\n            while 14:\n             while 15:\n              while 16:\n               while 17:\n                while 18:\n                 while 19:\n                  while 20:\n                   while 21:\n                    while 22:\n                     break\n'
    self._check_error(source, 'too many statically nested blocks')
