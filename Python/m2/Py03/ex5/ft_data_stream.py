#!/usr/bin/env python3
import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    player = ['Martin', 'Bernard', 'Thomas',
              'Robert', 'Lopez', 'Guillot', 'Berger']
    action = ['eat', 'run', 'sleep', 'grab',
              'move', 'climb', 'swim', 'release']
    while (1):
        yield (random.choice(player), random.choice(action))


def consume_event(event:
                  list[tuple[str, str]]) -> typing.Generator[
                       tuple[str, ...], None, None]:
    while (event):
        the_event = random.randint(0, (len(event) - 1))
        e = tuple(event[the_event])
        del event[the_event]
        yield e


if __name__ == "__main__":
    moves = gen_event()
    for i in range(1000):
        move = next(moves)
        print(f"Event {i}: Player {move[0]} did action {move[1]}")

    event_list: list[tuple[str, str]] = [('', '')] * 10
    gen = gen_event()
    for i in range(10):
        event_list[i] = next(gen)

    print(f"Built list of 10 events: {event_list}")
    try:
        consumer = consume_event(event_list)
        for e in consumer:
            print(f"Got event from list: {e}")
            print(f"Remains in list: {event_list}")
    except Exception as e:
        print(e)
