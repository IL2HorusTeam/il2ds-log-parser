# coding: utf-8
"""
Regex primitives.

"""

import re

from .constants import TOGGLE_VALUES, TARGET_STATES


def matcher(s):
    return re.compile(s, re.VERBOSE).match


def group(expression):
    return "({0})".format(expression)


def named_group(group_name, expression):
    return "(?P<{0}>{1})".format(group_name, expression)


def choices(values):
    return "|".join(values)


WHITESPACE = "\s"
NON_WHITESPACES = "\S+"
NUMBER = "\d+"
FLOAT = "{0}.{0}".format(NUMBER)


TIME = """
\d{1,2}  # 1 or 2 digits for hours (e.g. 8, 08 or 18)
:        # hours-minutes separator
\d{2}    # 2 digits for minutes
:        # minutes-seconds separator
\d{2}    # 2 digits for seconds
\s       # single whitespace
[AP]M    # day period (e.g. AM or PM)
"""

TIME_GROUP = named_group('time', TIME)

TIME_GROUP_PREFIX = """
# Capture event's time stamp prefix. E.g.:
#
# "[8:33:05 PM] foo"
#
# "8:33:05 PM" will be captured into 'time' group.
^             # beginning of a string
\[            # left time wrapper
{time_group}  # 'time_group' regex placeholder
\]            # right time wrapper
\s+           # one or more whitespaces
              # any ending of a string
""".format(
    time_group=TIME_GROUP,
)

DATE = """
\D{3}    # 3 non-digits for month abbreviation (e.g. Jan, Feb, Sep, etc)
\s       # single whitespace
\d{1,2}  # 1 or 2 digits for day number (e.g. 8, 08 or 18)
,        # single comma
\s       # single whitespace
\d{4}    # 4 digits for year (e.g. 2013)
"""

DATE_GROUP = named_group('date', DATE)

DATE_TIME_GROUP_PREFIX = """
# Capture event's datetime stamp prefix. E.g.:
#
# "[Sep 15, 2013 8:33:05 PM] foo"
#
# "Sep 15, 2013" will be captured into 'date' group,
# "8:33:05 PM" will be captured into 'time' group.
^               # beginning of a string
\[              # opening brackets
{date_group}    # 'date' group regex placeholder
\s              # single whitespace
{time_group}    # 'time' group regex placeholder
\]              # closing brackets
\s+             # one or more whitespaces
                # any ending of a string
""".format(
    date_group=DATE_GROUP,
    time_group=TIME_GROUP,
)

BELLIGERENT_GROUP = named_group('belligerent', NON_WHITESPACES)

CALLSIGN = NON_WHITESPACES
HIMSELF = group(choices(['landscape', 'NONAME']))

HUMAN_ACTOR_GROUP = named_group('actor_callsign', CALLSIGN)

AIRCRAFT = NON_WHITESPACES
AIRCRAFT_ACTOR_GROUP = named_group('actor_aircraft', AIRCRAFT)

HUMAN_AIRCRAFT_GROUP_TEMPLATE = "{callsign}:{aircraft}"
HUMAN_AIRCRAFT_ACTOR_GROUP = HUMAN_AIRCRAFT_GROUP_TEMPLATE.format(
    callsign=HUMAN_ACTOR_GROUP,
    aircraft=AIRCRAFT_ACTOR_GROUP,
)
HUMAN_AIRCRAFT_ATTACKER_GROUP = HUMAN_AIRCRAFT_GROUP_TEMPLATE.format(
    callsign=named_group('attacker_callsign', CALLSIGN),
    aircraft=named_group('attacker_aircraft', AIRCRAFT),
)

SEAT_NUMBER = NUMBER
SEAT_NUMBER_ACTOR_GROUP = named_group('actor_seat_number', SEAT_NUMBER)

HUMAN_AIRCRAFT_CREW_MEMBER_GROUP_TEMPlATE = "{callsign}:{aircraft}\({seat_number}\)"
HUMAN_AIRCRAFT_CREW_MEMBER_ACTOR_GROUP = HUMAN_AIRCRAFT_CREW_MEMBER_GROUP_TEMPlATE.format(
    callsign=HUMAN_ACTOR_GROUP,
    aircraft=AIRCRAFT_ACTOR_GROUP,
    seat_number=SEAT_NUMBER_ACTOR_GROUP,
)

POS_GROUP_SUFFIX = """
# Capture map position of an event. E.g.:
#
# "Something has happened at 100.0 200.99"
#
# "100.0" will be captured into 'pos_x' group,
# "200.99" will be captured into 'pos_y' group.
         # any beginning of a string
\s       # single whitespace
at       #
\s       # single whitespace
{pos_x}  # 'pos_x' regex placeholder
\s       # single whitespace
{pos_y}  # 'pos_y' regex placeholder
$        # end of a string
""".format(
    pos_x=named_group('pos_x', FLOAT),
    pos_y=named_group('pos_y', FLOAT),
)

TARGET_STATE_GROUP = named_group('state', choices(TARGET_STATES))
TOGGLE_VALUE_GROUP = named_group('value', choices(TOGGLE_VALUES))