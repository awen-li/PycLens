# Source Generated with Decompyle++
# File: cpython-312-a121b010b70b.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class Done(Exception):
        pass

    
    class AIter(StopIteration):
        i = 0
        
        def __aiter__(self):
            return self

        
        async def __anext__(self):
            if None:
                pass
            if self.i:
                raise StopAsyncIteration
            return self.value


    result = []
    
    async def foo():
        if None:
            pass
        if None or None:
            continue
        i = None
        result.append(i)
        continue
        continue
        raise Done

    self.assertRaises(Done)
    foo().send(None)
    None(None, None)
    self.assertEqual(result, [
        42])
    return None
    if None:
        pass
    with None:
        if not None:
            pass
    continue

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
