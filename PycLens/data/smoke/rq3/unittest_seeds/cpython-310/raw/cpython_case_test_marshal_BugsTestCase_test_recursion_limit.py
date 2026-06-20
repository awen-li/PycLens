# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_recursion_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    head = last = []
    if os.name == 'nt':
        MAX_MARSHAL_STACK_DEPTH = 1000
    else:
        MAX_MARSHAL_STACK_DEPTH = 2000
    for i in range(MAX_MARSHAL_STACK_DEPTH - 2):
        last.append([0])
        last = last[-1]
    data = marshal.dumps(head)
    new_head = marshal.loads(data)
    self.assertEqual(len(new_head), len(head))
    self.assertEqual(len(new_head[0]), len(head[0]))
    self.assertEqual(len(new_head[-1]), len(head[-1]))
    last.append([0])
    self.assertRaises(ValueError, marshal.dumps, head)
