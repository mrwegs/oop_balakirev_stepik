import math


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.lines = list(args)

    def get_path(self):
        return self.lines

    def get_length(self):
        # L = sqrt((x1 - x0) ^ 2 + (y1 - y0) ^ 2) - формула
        path_len = x0 = y0 = 0
        for line in self.lines:
            x1, y1 = line.x, line.y
            path_len += math.sqrt(math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2))
            x0, y0 = x1, y1

        return path_len

    def add_line(self, line):
        self.lines.append(line)
