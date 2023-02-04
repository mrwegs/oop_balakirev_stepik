from typing import Union


class TrackLine:
    to_x: Union[int, float]
    to_y: Union[int, float]
    max_speed: int

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    start_x: Union[int, float]
    start_y: Union[int, float]
    tracks_list: list

    def __init__(self, x=0, y=0):
        self.start_x = x
        self.start_y = y
        self.tracks_list = [TrackLine(self.start_x, self.start_y, 0)]

    def add_track(self, tr: TrackLine):
        self.tracks_list.append(tr)

    def get_tracks(self):
        return tuple(self.tracks_list)

    def __len__(self):
        result = 0
        for i in range(1, len(self.tracks_list)):
            x2, y2 = self.tracks_list[i].to_x, self.tracks_list[i].to_y
            x1, y1 = self.tracks_list[i - 1].to_x, self.tracks_list[i - 1].to_y
            result += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        return int(result)

    @classmethod
    def verify_value(cls, other):
        if not isinstance(other, Track):
            raise TypeError('Объект должен принадлежать классу Track')

        return len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

assert track1 != track2, "оператор != дает False для неравных маршрутов"
