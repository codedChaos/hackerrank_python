#! python3

##  @package runnerup_in_list
#   Documentation for this program
#
#   More Details.

from more_itertools import locate

10
"Barry"
37.21
"Tina"
39
"Jerry"
37.21
"Tim"
44
"William"
99
"Jersey"
37.2
"Sally"
72
"Mike"
72
"Emma"
99
"Isaac"
37.23


t = type(s)
for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    print any(method(c) for c in s)
