from functools import partial
from random import shuffle
import re
from pprint import pprint
from typing import Callable, TypeVar
import pdb

T = TypeVar('T')

SONATA_PATTERN = r'op\.\s(?P<opus>\d+(?P<suffix>a)?)(,\sno\.\s(?P<number>\d))?'

def build_matcher(expr: str, 
                  if_true: Callable[[re.Match], T],
                  if_false: Callable[[str], T]) -> Callable[[str], T]:

    pat : re.Pattern = re.compile(expr)

    def matcher(input: str) -> T:
        m = pat.match(input)
        if m is None:
            return if_false(input)
        else:
            return if_true(m)

    return matcher

def read_lines(filename, transform=lambda s:s):
    with open(filename) as fp:
        return [transform(line) for line in fp]

match_sonata = build_matcher(SONATA_PATTERN, 
                    if_true = lambda m:print(m.groupdict()),
                    if_false = lambda s: f'No match for "{sonata}."')

sonatas = read_lines('beethoven-piano-sonatas.txt', 
                     lambda s:s.strip())

shuffle(sonatas)

for sonata in sonatas:
    match_sonata(sonata)

