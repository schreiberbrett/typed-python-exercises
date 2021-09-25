from typing import TypeVar, Callable, Generic, Union
from dataclasses import dataclass

A = TypeVar('A')
B = TypeVar('B')


# Equivalent to Pair[A, B], and equivalent to Tuple[A, B], but named And here to match the wikipedia article below
@dataclass
class And(Generic[A, B]):
    first: A
    second: B

@dataclass
class Left(Generic[A, B]):
    left: A

@dataclass
class Right(Generic[A, B]):
    right: B


# Equivalent to Either[L, R], but named Or here to match the wikipedia article below
Or = Union[Left[A, B], Right[A, B]]

Implies = Callable[[A], B]

# Adapted from https://en.wikipedia.org/wiki/Propositional_calculus#Basic_and_derived_argument_forms

P = TypeVar('P')
Q = TypeVar('Q')
R = TypeVar('R')
S = TypeVar('S')

def modus_ponens(x: Implies[P, Q], y: P) -> Q:
    pass


def hypothetical_syllogism(x: Implies[P, Q], y: Implies[Q, R]) -> Implies[P, R]:
    pass


def constructive_dilemma(x: Implies[P, Q], y: Implies[R, S], z: Or[P, R]) -> Or[Q, S]:
    pass


def simplification(x: And[P, Q]) -> P:
    pass


def conjunction(x: P, y: Q) -> And[P, Q]:
    pass


def addition(x: P) -> Or[P, Q]:
    pass


def composition(x: Implies[P, Q], y: Implies[P, R]) -> Implies[P, And[Q, R]]:
    pass


def commutation_1(x: Or[P, Q]) -> Or[Q, P]:
    pass


def commutation_2(x: And[P, Q]) -> And[Q, P]:
    pass


def association_1(x: Or[P, Or[Q, R]]) -> Or[Or[P, Q], R]:
    pass


def association_2(x: And[P, And[Q, R]]) -> And[And[P, Q], R]:
    pass


def distribution_1(x: And[P, Or[Q, R]]) -> Or[And[P, Q], And[P, R]]:
    pass


def distribution_2(x: Or[P, And[Q, R]]) -> And[Or[P, Q], Or[P, R]]:
    pass


def exportation(x: Implies[And[P, Q], R]) -> Implies[P, Implies[Q, R]]:
    pass


def importation(x: Implies[P, Implies[Q, R]]) -> Implies[[And[P, Q]], R]:
    pass


def tautology_1(x: P) -> Or[P, P]:
    pass


def tautology_2(x: P) -> And[P, P]:
    pass