#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from io import StringIO

esst_text = """
>0 0 LOG_ODDS
#  G  A  V  L   M  I   F   Y   W  S  T   C  P  N  Q  K  R   H  D  E
G  5 -2 -6 -7  -5 -7  -8  -7  -8 -2 -4  -7 -4 -2 -4 -4 -4  -4 -3 -4
A  1  6  1 -1  -1  0  -3  -2  -3  1  0  -1  0 -1  0  0 -1  -1 -2 -1
V -4  0  7  2   0  4  -1  -2  -3 -3  0  -2 -3 -4 -2 -3 -3  -4 -5 -3
L -4 -2  2  8   4  4   3   0  -1 -3 -2  -3 -4 -4 -2 -3 -3  -3 -6 -3
M -4 -1  1  4  11  2   1  -1  -1 -3 -2  -3 -5 -3 -1 -2 -2  -2 -5 -3
I -5 -2  5  3   2  8   0  -1  -2 -4 -1  -2 -4 -5 -4 -3 -4  -4 -6 -4
F -5 -3 -1  2   3  0  11   5   4 -4 -3  -2 -5 -4 -3 -5 -5   0 -7 -5
Y -5 -2 -2 -1  -1 -1   5  11   4 -3 -4  -2 -5 -2 -3 -4 -3   3 -5 -4
W -5 -3 -4  0  -2 -3   4   3  16 -5 -5  -3 -4 -4 -3 -5 -4  -2 -6 -5
S  0  1 -2 -4  -3 -3  -5  -3  -5  5  2  -2 -1  0  0  0 -2  -2 -1 -1
T -2  0  0 -2  -2 -1  -4  -2  -5  2  7  -3 -2  0  0  0 -1  -1 -2 -1
C -4 -1 -1 -3  -2 -1  -2  -3  -6 -1 -2  15 -5 -4 -5 -5 -5  -4 -6 -6
P -3 -1 -4 -5  -5 -4  -6  -5  -7 -1 -2  -4  8 -3 -2 -1 -3  -4 -3 -1
N -1 -2 -4 -5  -4 -4  -5  -2  -5  1  0  -3 -3  7  0  0 -1   0  1 -1
Q -1  0 -2 -2   0 -3  -4  -3  -2  0 -1  -3 -1  1  7  2  1   1  0  2
K -1  0 -2 -3  -2 -4  -6  -3  -5  0  0  -6 -1  0  2  6  3   0 -1  1
R -2 -2 -2 -2   0 -3  -5  -2  -4 -1 -1  -4 -2  0  1  3  8   0 -3 -1
H -2 -2 -3 -3  -2 -2   0   2  -2 -2 -2  -2 -3  0  0 -1  0  11 -2 -1
D -1 -1 -5 -6  -5 -6  -7  -4  -7  0 -1  -7 -2  1  0 -1 -3  -1  7  2
E  0  0 -3 -3  -2 -4  -5  -3  -5  0 -1  -5  0  0  2  1  0  -1  2  7

>1 1 LOG_ODDS
#  G  A  V  L   M  I   F   Y   W  S  T   C  P  N  Q  K  R   H  D  E
G  6 -3 -7 -8  -8 -8  -7  -8  -8 -2 -5  -6 -5 -4 -5 -5 -6  -6 -5 -4
A  0  6  0 -2  -2 -2  -3  -3  -5  1  0   0  0 -1 -1 -1 -2  -3 -2 -1
V -4  1  8  2   3  5   0  -2  -2 -3  0  -1 -2 -3 -1 -2 -2  -3 -5 -2
L -5 -3  2  8   5  4   2  -1  -1 -4 -2  -4 -4 -4 -2 -2 -3  -2 -5 -3
M -5 -1  1  4  11  2   1  -1  -1 -3 -2  -3 -4 -4 -1 -2 -3  -4 -5 -2
I -5 -1  6  4   4  9   2  -1  -2 -4 -1  -3 -4 -4 -2 -3 -4  -3 -6 -3
F -6 -4 -1  1   1  1  11   5   3 -5 -4  -5 -5 -5 -4 -4 -4  -2 -7 -5
Y -5 -3 -1 -2  -2 -2   5  11   5 -4 -4  -5 -5 -3 -3 -4 -2   1 -5 -4
W -5 -5 -3 -2  -2 -3   4   3  16 -4 -6  -5 -5 -4 -4 -6 -4  -3 -7 -5
S  0  1 -3 -4  -4 -5  -4  -3  -6  6  3  -2 -1  1 -1 -1 -2  -2  0 -1
T -3  0  0 -2  -2 -2  -3  -4  -4  2  7  -2 -2  0 -1  0 -2  -3 -1 -1
C -6  1  0 -3  -3 -3  -3  -2  -6 -2 -3  15 -5 -4 -4 -4 -5  -4 -6 -6
P -2  1 -2 -3  -3 -4  -4  -4  -6 -1 -2  -3  8 -3 -1  0 -1  -2 -1  0
N -3 -3 -5 -6  -6 -6  -6  -3  -5  0 -1  -5 -4  7 -1 -1 -2   0  1 -2
Q -3 -1 -2 -2  -1 -4  -4  -3  -5 -2 -1  -4 -2  0  8  1  1   0 -1  2
K -3 -2 -3 -4  -3 -4  -5  -4  -5 -2 -1  -5 -2  0  1  7  3  -1 -2  1
R -3 -3 -3 -3  -3 -4  -5  -3  -4 -3 -1  -5 -3 -1  1  3  9  -1 -3 -1
H -4 -3 -3 -3  -4 -5  -2   1  -3 -2 -3  -5 -3  0  0 -2 -1  12 -1 -1
D -3 -3 -5 -7  -6 -7  -7  -5  -8 -1 -2  -6 -3  2 -1 -2 -3  -2  7  1
E -2 -1 -3 -5  -4 -4  -6  -3  -6 -2 -1  -6 -2 -1  2  1 -1  -2  1  7

>2 2 LOG_ODDS
#  G  A  V  L   M  I   F   Y   W  S  T   C  P  N  Q  K  R   H  D  E
G  6 -1 -6 -7  -7 -6  -6  -6  -9 -2 -4  -5 -4 -4 -4 -5 -5  -5 -4 -3
A  0  6  0 -3  -2 -2  -3  -4  -6  0 -1  -1  0 -3 -1 -1 -3  -3 -2 -1
V -5  2  8  3   3  6   0  -1  -1 -2  0   1  0 -3 -1 -1 -1  -2 -4 -2
L -6 -2  1  8   4  3   0  -2  -1 -3 -3  -2 -2 -5 -2 -3 -3  -4 -5 -3
M -2 -1  1  4  11  3   0  -2  -1 -3 -1  -1 -1 -4  0 -2 -2   0 -6 -2
I -6  0  5  5   5  9   2   0  -1 -3 -1   0 -1 -4 -2 -2 -3  -3 -6 -2
F -4 -3  0  2   3  1  10   7   5 -4 -4  -2 -2 -4 -4 -4 -5   0 -7 -6
Y -6 -3 -1 -1  -1 -2   6  11   4 -2 -3  -3 -1 -3 -3 -3 -2   1 -3 -3
W -5 -4 -2 -1  -1 -4   4   4  16 -4 -5  -6 -3 -6 -3 -6 -5  -3 -5 -7
S  0  1 -3 -5  -3 -4  -4  -4  -7  6  2   0  0  1  0 -1 -2  -2  1 -1
T -2  1  0 -2  -2 -2  -3  -3  -7  3  7  -3  0  1  1  0  0  -2  0 -1
C -3  1  1 -1  -2 -2  -2  -2  -5  1  1  15 -4  1 -5 -4 -3  -1 -3 -5
P -5 -3 -5 -5  -6 -6  -6  -5 -10 -4 -5  -5  5 -4 -4 -4 -4  -6 -6 -3
N -3 -3 -6 -6  -4 -6  -5  -4  -9  0 -1  -6 -2  8  0 -1 -2  -1  2 -1
Q -2 -2 -3 -3  -2 -4  -3  -3  -4 -1 -1  -5  1 -1  8  2  2  -1 -1  2
K -3 -2 -4 -4  -2 -5  -4  -4  -6 -2 -1  -6  1 -2  1  7  3  -2 -2  0
R -2 -2 -3 -3  -2 -5  -3  -4  -2 -2 -1  -6  0 -3  1  4  9   0 -3  0
H -4 -3 -5 -3  -2 -5   0   2  -2 -2 -2  -4 -3  0  0  0  0  12  0 -1
D -3 -3 -7 -7  -8 -8  -5  -6 -10 -1 -1  -6 -1  2 -1 -2 -4  -2  7  1
E -2 -2 -3 -4  -6 -5  -3  -5  -7 -2 -2  -6  1 -2  1  0 -1  -2  1  7

>3 3 LOG_ODDS
#  G  A  V  L   M  I   F   Y   W  S  T   C  P  N  Q  K  R   H  D  E
G  6 -2 -7 -9  -8 -6  -7  -7 -11 -3 -3  -9 -4 -4 -4 -3 -7  -6 -4 -3
A  1  6 -1 -2  -3 -1  -4  -3  -1  1  1   1  0 -2  0 -1 -2  -4 -2 -1
V -4  0  7  2   2  6  -2  -1  -2 -3  2  -1 -4 -3 -2 -1 -4  -3 -5 -3
L -4 -1  2  8   5  4   2   0  -1 -3 -1  -1 -4 -4 -3 -3 -3  -5 -6 -4
M -5 -1  3  4  11  1   2   0  -1 -3  0  -2 -3 -1 -2 -1 -3  -2 -4 -3
I -4 -2  6  3   4  9   2   1  -3 -5  0   0 -4 -4 -3 -2 -3  -5 -5 -4
F -3 -2  1  4   1  2  11   6   4 -3 -2   1 -5 -3 -2 -4 -4   0 -6 -4
Y -3 -3  0  0  -2 -2   6  10   5 -3 -3   0 -5 -2 -2 -3 -2   2 -3 -3
W -5 -4 -2  1   0 -3   4   1  16 -3 -4  -3 -5 -2 -4 -5 -6  -1 -7 -4
S -2  1 -3 -4  -5 -5  -4  -5  -6  6  1  -4 -3 -1 -1 -1 -3  -3 -2 -1
T -2  0 -2 -2  -3 -3  -6  -5  -8  2  5  -7 -1 -2 -1 -1 -3  -5 -4 -1
C -3  4  0  0  -2 -1  -2  -1   1 -1 -1  15 -4 -5 -3 -3 -4   0 -5 -6
P -5 -3 -5 -4  -3 -5  -7  -9  -8 -4 -3  -7  8 -3 -2 -2 -3  -4 -4 -4
N -1 -1 -5 -5  -4 -6  -4  -1  -3  1  0  -2 -2  7  1  2  0   2  2  0
Q -2 -1 -1 -3   2 -4  -5  -4  -7  0  0  -6 -1  0  8  3  1   1 -1  3
K -2 -2 -3 -5  -5 -5  -5  -3  -5 -1  0  -9 -2  0  1  6  2  -1 -2  0
R -3 -1 -3 -5  -6 -6  -5  -1  -8 -2 -1  -6 -2  0  1  3  9   1 -3 -1
H -3 -3 -4 -3  -5 -4  -1   3  -2 -2 -1  -4 -3  2  1  0  2  12 -2 -1
D -1 -2 -5 -4  -7 -9  -6  -4  -7  0 -2  -7 -1  2  0  0 -2  -2  8  2
E -2 -2 -4 -4  -5 -7  -7  -4  -8  0 -1  -7 -1 -1  1  0 -2  -3  1  7

>4 4 LOG_ODDS
#   G  A  V  L   M  I   F   Y   W  S   T   C  P  N  Q  K  R   H  D  E
G   7  4 -1 -1   0 -2   0  -1  -3  4   2   0  2  3  3  3  2   2  2  2
A  -3  5  0 -2  -2  0  -3  -3  -3 -1  -1  -4 -1 -3 -2 -3 -4  -4 -4 -3
V  -8 -4  5 -1  -4  2  -3  -5  -6 -6  -2  -6 -5 -6 -6 -7 -7  -7 -7 -5
L  -8 -4  2  7   3  4   1  -2  -3 -6  -4  -2 -5 -6 -4 -6 -4  -3 -8 -5
M  -7 -4  2  6  11  3   2  -1  -3 -3  -4  -3 -1 -5  0 -2 -1  -3 -6 -5
I -10 -5  2  1  -1  5  -3  -6  -5 -7  -3  -8 -6 -7 -5 -8 -8  -8 -8 -7
F  -8 -4  1  2   1  3  10   5   4 -4  -3  -4 -3 -5 -6 -4 -3  -2 -5 -6
Y  -7 -4 -1 -1   1  0   4  10   3 -4  -5  -3 -4 -3 -4 -4 -2   0 -4 -3
W  -6 -2 -2 -3  -3 -3   3   5  16 -1 -10  -7 -5 -7 -7 -8 -2  -6 -5 -7
S  -4  0 -3 -4  -4 -3  -5  -3  -5  5   1  -5  0 -2 -2 -3 -3  -4 -2 -2
T  -6 -3 -2 -4  -5 -2  -4  -6  -5 -3   4  -6 -2 -4 -3 -5 -5  -6 -4 -3
C  -7  0  2 -1   2 -1  -1  -1  -6 -1  -1  15 -8 -5 -4 -6 -2  -4 -6 -6
P  -7 -4 -2 -5 -10 -4  -2  -7  -4 -5  -4  -9  4 -5 -4 -6 -7  -5 -6 -5
N   0  0 -1 -1   1  2  -1   0  -3  2   1  -2  0  7  2  2  1   2  3  1
Q  -3  0  0  0  -1 -1  -3  -2  -6 -1   0  -2  1  0  7  2  2   0 -1  2
K  -3 -2  0 -3   0 -2  -6  -3  -8 -1  -1  -4  1  0  2  7  3   0 -1  1
R  -4 -3  1 -2  -1 -1  -5  -3  -6 -3  -2  -4  0 -1  1  2  8  -1 -2 -1
H  -4 -2 -1 -2   1 -1  -1   2  -3 -2  -2  -3  0  0  0  0  1  11 -2 -2
D  -2 -3 -5 -4  -4 -5  -3  -4  -6  0   0  -6 -1  1  0 -2 -4  -2  6  2
E  -3 -2 -2 -3  -2 -3  -4  -4  -8 -2   1  -7  1 -1  0 -1 -3  -2  1  7

>5 5 LOG_ODDS
#  G  A  V  L   M  I   F   Y   W  S  T   C  P  N  Q  K  R   H  D  E
G  7  1 -1 -5  -1 -8  -3  -2  -6  0  1   1  0  0 -2  1 -1  -3  1  0
A -2  6 -1 -3   0 -4  -2  -3  -9 -1 -2   0  0 -2 -2 -1 -2  -3 -2 -2
V -6 -2  6  2   1  4  -2   1  -8 -3 -1  -2 -2 -3 -3 -3 -3  -4 -2 -1
L -8 -3  1  6   2  5   3  -2   0 -3 -4  -7 -4 -5 -3 -3  0  -5 -5 -4
M -6  1  2  4  10  1   3   0  -4  0 -1  -7 -6 -1  1 -4 -1  -5 -5 -4
I -7 -5  2  3   0  9   0  -1  -9 -4 -2   1 -2 -6 -3 -4 -3  -4 -5 -3
F -6 -4  2  3  -1 -1  10   6  -1 -6  0  -8 -4 -4 -3 -4 -2  -3 -7 -5
Y -5 -3 -1  1  -2 -4   6  11   8 -6 -5 -11 -3 -3 -4 -4 -1   0 -6 -3
W -6 -7 -3 -3  -4 -1  -3   1  11 -5 -5  -8  0 -4 -3 -6 -3 -15 -8 -4
S -3  0 -3 -3  -3 -6  -6  -5  -7  7  2   2 -1 -1 -2 -2 -3  -1 -2  0
T -4 -1 -2  0  -1 -2  -5  -3  -3  0  6  -2  1 -1 -2 -2 -3   0 -3  0
C -6 -4 -2 -2  -2 -7  -1  -2 -12 -5 -4  14 -6 -3 -4 -5 -5  -3 -6 -6
P -5 -1 -3 -3   0 -4  -3  -6   5 -1 -2  -9  6 -5 -3 -3 -4  -2 -3 -1
N -3 -3 -2 -3  -4 -5  -8  -3  -6 -2 -2  -4 -2  7  1  0  1  -1  1  0
Q -4 -1 -1 -2  -1  0  -3  -5  -2 -1  0  -6  0  0  7  2 -1  -1 -1  1
K -3  0 -3 -1   1 -3  -4  -5  -2 -2  0  -4 -1  0  4  7  3   1  0  2
R -4 -1 -2 -2   0 -4  -4  -5  -3 -2 -2  -3 -2 -2  3  2  8   0 -2 -1
H -5 -2  3 -1  -2 -1  -2  -1  -2 -3 -3  -2 -2 -1  2 -1 -1  11 -3 -2
D -4 -3 -3 -4  -3 -6  -8  -2  -1 -1 -3  -5 -1  2 -2 -1 -4  -3  6  1
E -4 -1  0 -1  -2 -2  -5  -3   1 -2 -1  -5  1  0  1  0 -3   0  2  6

>? 6 LOG_ODDS
#  G  A  V  L   M  I   F   Y   W  S  T   C  P  N  Q  K  R   H  D  E
G  6 -2 -6 -6  -7 -8  -7  -6  -7 -2 -4  -6 -5 -3 -3 -3 -4  -6 -2 -4
A  0  5  1 -1  -1 -1  -3  -2  -4  1  0  -1 -1 -1  0  0 -1  -2 -1 -1
V -4  1  7  3   1  4  -1  -2  -1 -2  0  -2 -2 -2 -2 -2 -3  -3 -4 -2
L -4 -1  2  7   3  3   2  -1  -1 -3 -1  -4 -4 -2 -1 -2 -1  -3 -4 -3
M -2  1  2  4  12  3   2  -1  -1  1  1  -2 -3  0  2  1  1   0 -2  0
I -5  0  5  4   2  8   1  -2  -1 -2  0  -2 -3 -3 -2 -2 -3  -3 -4 -3
F -4 -3  0  2   1  1  11   5   3 -4 -3  -2 -4 -3 -3 -3 -4   0 -5 -4
Y -4 -3 -2 -2   0 -2   5  12   4 -4 -2  -5 -5 -1 -2 -3 -5   2 -5 -5
W -5 -3 -3  1  -2 -3   5   3  16 -2 -5  -3 -6 -4 -3 -6 -5  -3 -1 -5
S -1  1 -2 -3  -2 -4  -4  -4  -4  4  2  -2 -2  0  0 -1 -1  -2  0 -1
T -3  0  0 -2  -1 -2  -4  -4  -3  2  5  -3 -3  0 -1 -1 -2  -1 -1 -1
C -4  1 -2 -3  -4 -4  -4  -3  -3 -2 -2  16 -5 -2 -4 -5 -4  -5 -4 -5
P -3  0 -2 -3  -3 -3  -6  -5  -8 -1 -2  -4  8 -3  0 -2 -1  -3 -3 -2
N -1 -2 -3 -4  -3 -5  -5  -3  -4  0  0  -5 -3  6 -1 -1 -3   0  1 -1
Q -1  0 -2 -1   0 -2  -4  -2  -4  1  1  -4 -2  0  6  2  1   2  0  2
K -1  0 -2 -2  -1 -1  -5  -4  -6  0  0  -4 -2  1  2  7  3   0 -1  2
R -2 -1 -2 -3  -2 -2  -5  -5  -5 -1 -1  -4 -2 -1  1  3  8   0 -2 -1
H -3 -2 -4 -2  -4 -5  -2   1  -4 -2 -2  -4 -4  1 -1  0 -1  11  0 -1
D -2 -3 -5 -6  -4 -6  -5  -6  -7  0 -2  -6 -3  1 -2 -2 -4  -3  6  1
E -1  0 -1 -3  -1 -3  -2  -4  -6  1  0  -5 -1  1  2  1  0  -1  2  7

>TOTAL LOG_ODDS
#  G  A  V  L   M  I   F   Y   W  S  T   C  P  N  Q  K  R   H  D  E
G  7 -2 -6 -7  -6 -7  -6  -6  -8 -2 -4  -5 -5 -1 -3 -3 -4  -4 -3 -3
A -1  6  0 -2  -1 -2  -3  -3  -4  1  0  -1  0 -2  0 -1 -2  -2 -2 -1
V -6  1  8  2   1  5  -1  -1  -2 -3  0  -1 -3 -4 -2 -2 -3  -3 -5 -2
L -6 -2  2  8   4  4   2  -1  -1 -3 -2  -3 -4 -4 -2 -3 -3  -3 -6 -3
M -5 -1  1  4  11  2   1  -1  -1 -3 -1  -2 -4 -3  0 -2 -2  -2 -5 -2
I -7 -2  5  4   3  9   1  -1  -2 -4 -1  -2 -4 -5 -3 -3 -4  -4 -6 -3
F -6 -3  0  2   2  1  11   6   4 -4 -3  -2 -5 -4 -4 -4 -4  -1 -6 -5
Y -5 -3 -1 -1  -1 -2   5  11   4 -3 -3  -3 -5 -2 -3 -4 -3   2 -4 -4
W -6 -4 -3 -1  -2 -3   4   3  16 -4 -5  -4 -5 -4 -4 -6 -4  -3 -5 -5
S -2  1 -3 -4  -3 -4  -4  -4  -5  6  2  -2 -1  0 -1 -1 -2  -2 -1 -1
T -4  0  0 -2  -2 -2  -4  -3  -5  2  7  -3 -2 -1  0 -1 -1  -2 -2 -1
C -5  0  0 -3  -2 -2  -2  -2  -5 -1 -2  15 -5 -3 -4 -5 -4  -3 -5 -6
P -5 -1 -3 -4  -4 -4  -5  -5  -6 -2 -2  -4  8 -3 -2 -2 -2  -4 -3 -1
N -1 -2 -5 -5  -4 -5  -5  -2  -5  0 -1  -4 -4  7  0  0 -1   0  2 -1
Q -3  0 -2 -2   0 -4  -4  -3  -4 -1 -1  -4 -2  0  8  2  1   0 -1  2
K -3 -1 -3 -3  -2 -4  -5  -4  -5 -1 -1  -6 -1  0  2  7  3  -1 -1  1
R -3 -2 -2 -3  -2 -4  -5  -3  -4 -2 -1  -5 -2 -1  1  3  8   0 -3 -1
H -4 -2 -3 -3  -3 -4  -1   2  -3 -2 -2  -4 -3  0  0 -1  0  11 -1 -1
D -2 -2 -5 -6  -5 -7  -6  -5  -8 -1 -2  -6 -3  2 -1 -1 -3  -2  7  2
E -2 -1 -3 -4  -3 -4  -4  -4  -6 -1 -1  -6 -1 -1  2  1 -1  -2  2  7
"""


class SubstTableSet(object):
  def __init__(self, filename):
    self.tables = []
    self.header = []
    tab=None
    try:
      f = open(filename)
    except TypeError:
      f = filename
    try:
      for line in f:
        line = line.rstrip() #.encode("ascii")
        if not line or line.startswith('#'):
          continue
        if line.startswith('>'):
          tab = []
          self.tables.append(tab)
          self.header = []
          continue
        fields = line.split()
        self.header.append(fields.pop(0))
        for i,x in enumerate(fields):
          fields[i] = int(x)
        tab.append(fields)
    finally:
      f.close()
    
    if "X" not in self.header:
      UNKNOWN_SCORE = -1 # score assigned to any substitution involving an unknown residue
      self.header.append("X")
      for tab in self.tables:
        for row in tab:
          row.append(UNKNOWN_SCORE)
        tab.append([UNKNOWN_SCORE] * len(row))
    
    
    self.ascii2index=[None]*256
    for i,x in enumerate(self.header):
      self.ascii2index[ord(x.upper())] = i
      self.ascii2index[ord(x.lower())] = i
    
    # Remap weird residues
    #
    # 'SEC' = 'U' = Selenocysteine
    # 'ASX' = 'B' = ASP or ASN
    # 'XLE' = 'J' = LEU or ILE
    # 'GLX' = 'Z' = GLU or GLN
    # 'XXX' = 'X' = Unknown amino acid   <-- these should have been filtered out by build_db.py
    for x,y in zip("UBJZ", "CNLQ"):
      self.ascii2index[ord(x.upper())] = self.ascii2index[ord(y)]
      self.ascii2index[ord(x.lower())] = self.ascii2index[ord(y)]
    
    self.header = tuple(self.header)
    self.ascii2index = tuple(self.ascii2index)
    
    self.diagonal = [1000]*min(len(self.tables[0]), len(self.tables[0][0]))
    tab = self.tables[-1] # Assume total table is the last one
    for i,v in enumerate(self.diagonal):
      self.diagonal[i] = tab[i][i] - 1
    #print self.diagonal
        
  
  def get_perfect_score(self, seq):
    score=0
    for aa in seq:
      try:
        score += self.diagonal[self.ascii2index[ord(aa)]]
      except TypeError:
        print("Trying and failing to get score for amino acid:", aa)
        raise
    return score
  
  
  def get_subst_vector(self, tablenum, aa):
    "Get vector of substitution scores for a particular dihedral class and a particular amino acid type. Tables are symmetric, so no worries about which protein the amino acid is from."
    return self.tables[tablenum][self.ascii2index[ord(aa)]]




def load_esst(filepath=None):
  if filepath is None:
    return SubstTableSet(StringIO(esst_text))
  return SubstTableSet(filepath)
