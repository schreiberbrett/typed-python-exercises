from typing import Callable, TypeVar, Generic, Union
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Nil(Generic[T]):
    pass # intentionally empty

@dataclass
class Cons(Generic[T]):
    first: T
    rest: 'List[T]' # In quotes to tell Python that "List[T]" is defined later in the file

List = Union[Nil[T], Cons[T]]

def an_arbitrary_list() -> List[int]:
    """Returns the list [123, 456]"""
    return Cons[int](first=123, rest=Cons[int](first=456, rest=Nil()))



def print_ints(ints: List[int]) -> None:
    if isinstance(ints, Nil[int]):
        # nothing to print
        return

    # TODO look at the error message and correct it
    if isinstance(ints, Cons[int]):
        print(f'{ints.first}, ')
        print_ints(ints.rest)


# TODO implement
def add_12_to_each(ints: List[int]) -> List[int]:
    pass


# TODO implement
def multiply_each_by_4(ints: List[int]) -> List[int]:
    pass


# TODO implement
def only_positives(ints: List[int]) -> List[int]:
    """Given a list of numbers `xs`, return a filtered list of just the numbers in that list greater than 0"""
    pass


# TODO implement
def no_empty_strings(strings: List[str]) -> List[str]:
    pass


# TODO implement
def each_to_string(ints: List[int]) -> List[str]:
    pass



A = TypeVar('A')
B = TypeVar('B')

# TODO: Implement, then name
def name_me_1(xs: List[A], f: Callable[[A], B]) -> List[B]:
    pass


# TODO: Implement, then name
def name_me_2(xs: List[T], predicate: Callable[[T], bool]) -> List[T]:
    pass

# TODO implement, then fill in the return type
def maximum(ints: List[int]):
    pass

# TODO implement, then fill in the return type
def minimum(ints: List[int]):
    pass

# TODO implement, then fill in the return type
def first_element_of_list(xs: List[T]):
    pass

# TODO implement, then fill in the return type
def last_element_of_list(xs: List[T]):
    pass

# TODO implement
def is_palindrome_list(xs: List[int]) -> bool:
    pass


@dataclass
class Pair(Generic[A, B]):
    first: A
    second: B





L = TypeVar('L')
R = TypeVar('R')