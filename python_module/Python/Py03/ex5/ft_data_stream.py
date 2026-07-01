import typing
import random

def gen_event() -> typing.Generator[tuple, None, None]:
    player = ['Martin', 'Bernard', 'Thomas', 'Robert', 'Lopez', 'Guillot', 'Berger']
    action = ['eat', 'run', 'sleep', 'grab', 'move', 'climb', 'swim', 'release']
    while(1):
        yield tuple({random.choice(player) , random.choice(action)})


def consume_event(event: list) -> typing.Generator[list, None, None]:
    while(1):
        the_event = random.choice(event)
        if the_event in event:
            event.remove(the_event)
        yield the_event


if __name__ == "__main__":
    for i in range(1000):
        iter = next(gen_event())
        print(f"Event {i}: Player {iter[0]} did action {iter[1]}")
    event_list = [('')] * 10
    for i in range(10):
        event_list[i] = next(gen_event(), "end")
    print(f"Built list of 10 events: {event_list}")
    while event_list:
        print(f"Got event from list: {next(consume_event(event_list))}")
        print(f"Remains in list: {event_list}")