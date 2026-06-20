# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_keys_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BaseAnimal(TypedDict):
        name: str

    class Animal(BaseAnimal, total=False):
        voice: str
        tail: bool

    class Cat(Animal):
        fur_color: str
    assert BaseAnimal.__required_keys__ == frozenset(['name'])
    assert BaseAnimal.__optional_keys__ == frozenset([])
    assert BaseAnimal.__annotations__ == {'name': str}
    assert Animal.__required_keys__ == frozenset(['name'])
    assert Animal.__optional_keys__ == frozenset(['tail', 'voice'])
    assert Animal.__annotations__ == {'name': str, 'tail': bool, 'voice': str}
    assert Cat.__required_keys__ == frozenset(['name', 'fur_color'])
    assert Cat.__optional_keys__ == frozenset(['tail', 'voice'])
    assert Cat.__annotations__ == {'fur_color': str, 'name': str, 'tail': bool, 'voice': str}
