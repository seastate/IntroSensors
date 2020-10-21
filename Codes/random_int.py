#  This code is based on a post on the Micropython forum, at
#  https://forum.micropython.org/viewtopic.php?t=6158
#  Modified by D. Grunbaum on 2020-03-29 to include
#  the option of specifying a random seed.
#  Released under the MIT license (https://opensource.org/licenses/MIT)
#
import urandom

def randint(min, max,seed=None):
    if seed is not None:
        urandom.seed(seed)
    span = max - min + 1
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val
