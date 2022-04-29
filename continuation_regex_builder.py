import re
from typing import Callable, TypeVar

T = TypeVar('T')

def get_match(pat: re.Pattern,
              input: str,
              if_true: Callable[[re.Match], T],
              if_false: Callable[[str], T]) -> T:

    m = pat.match(input)
    if m is None:
        return if_false(input)
    else:
        return if_true(m)

# This is equivalent to 
# 
#     functools.partial(get_match, pat=re.compile(expr))
#
def build_matcher(expr: str, flags: re.RegexFlag|int = 0) \
        -> Callable[[str, Callable[[re.Match], T], Callable[[str], T]], T]:
    pat : re.Pattern = re.compile(expr, flags)

    def matcher(input: str, 
                if_true: Callable[[re.Match], T],
                if_false: Callable[[str], T]) -> T:
        m = pat.match(input)
        if m is None:
            return if_false(input)
        else:
            return if_true(m)

    return matcher
