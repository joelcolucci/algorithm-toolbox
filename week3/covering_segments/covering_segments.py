# Uses python2

import sys
from operator import attrgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments = sorted(segments, key=attrgetter('end') )

    points = []
    covered_segments = []

    for i in range(0, len(segments)):
        if segments[i] in covered_segments:
            pass
        else:
            points.append(segments[i].end)
            for j in range(i, len(segments)):
                if segments[i].end <= segments[j].end and segments[i].end >= segments[j].start:
                    covered_segments.append(segments[j])
                else:
                    break

    return points

"""Post-mortem
Key thought: Identified a data structure was needed to keep track of covered segments.

Practice: Thinking through the first case, easiest case first to ensure you're on the right track

"""


if __name__ == '__main__':
    data = [int(i) for i in sys.stdin.read().split()]

    data.pop(0)
    n = len(data)
    segments = [Segment(start=data[i], end=data[i + 1]) for i in range(0, n - 1, 2)]

    points = optimal_points(segments)
    print len(points)
    for p in points:
        print str(p) + ' '
