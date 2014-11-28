# -*- coding: utf-8 -*-


class Event(object):

    def __init__(self, *args, **kwargs):
        super(Event, self).__init__()

    def __repr__(self):
        return "<Event '{0}'>".format(self.__class__.__name__)


class EventWithTime(object):

    def __init__(self, **kwargs):
        super(EventWithTime, self).__init__(**kwargs)
        self.time = kwargs['time']


class EventWithDate(object):

    def __init__(self, **kwargs):
        super(EventWithDate, self).__init__(**kwargs)
        self.date = kwargs['date']


class EventWithDateTime(EventWithDate, EventWithTime):
    pass


class EventWithCallsign(object):

    def __init__(self, **kwargs):
        super(EventWithCallsign, self).__init__(**kwargs)
        self.callsign = kwargs['callsign']


class EventWithBelligerent(object):

    def __init__(self, **kwargs):
        super(EventWithBelligerent, self).__init__(**kwargs)
        self.belligerent = kwargs['belligerent']


class EventWithPos(object):

    def __init__(self, **kwargs):
        super(EventWithPos, self).__init__(**kwargs)
        self.pos = kwargs['pos']


class MissionIsPlaying(EventWithDateTime, Event):

    def __init__(self, **kwargs):
        super(MissionIsPlaying, self).__init__(**kwargs)
        self.mission = kwargs['mission']


class MissionHasBegun(EventWithTime, Event):
    pass


class MissionHasEnded(EventWithTime, Event):
    pass


class MissionWasWon(EventWithDateTime, EventWithBelligerent, Event):
    pass


class TargetStateHasChanged(EventWithTime, Event):

    def __init__(self, **kwargs):
        super(TargetStateHasChanged, self).__init__(**kwargs)
        self.target_index = kwargs['target_index']
        self.state = kwargs['target_end_state']


class UserHasConnected(EventWithTime, EventWithCallsign, Event):
    pass


class UserHasDisconnected(EventWithTime, EventWithCallsign, Event):
    pass


class UserHasWentToMenu(EventWithTime, EventWithCallsign, Event):
    pass


class UserHasSelectedAirfield(EventWithTime,
                              EventWithCallsign,
                              EventWithBelligerent,
                              EventWithPos,
                              Event):
    pass
