Extremely simple utility app that ignores any garbage and sums all numbers
from stdin. For example:

    $ echo "1 2 3 hey that's not a number 4 5 6" | smart_sum
    21

It's smart about maintaining precision, too.

    $ echo '$12.43 $100.42 $2,200.10' | smart_sum
    2312.95

See `test_smart_sum.py` for more examples. The golden rule is that numbers
must be whitespace delimited.

### Motivation

I find myself wanting to add numbers together in vim *a lot*. This utility
makes that as easy as selecting a range and `:!smart_sum`. I use the mapping

    vmap <c-d>s :!smart_sum<cr>

### Installation

I did this, but you can do whatever floats your boat.

    $ cd
    $ git clone https://github.com/thanthese/smart_sum
    $ cd /usr/bin
    $ ln -s ~/smart_sum/smart_sum.py smart_sum