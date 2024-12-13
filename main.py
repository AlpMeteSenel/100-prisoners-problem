import random
import tqdm
prisoner_count = 100 # Make sure prisoner count is even or it wouldn't be fair
try_amount = 100000

def create_room(prisoner_count):
    room = {}
    numbers = [x for x in range(1, prisoner_count + 1)]
    for x in range(len(numbers)):
        room[x+1] = random.choice(numbers)
        numbers.remove(room[x+1])
    return room

def handle_prisoner_loop(room, prisoner_id):
    box_to_open = prisoner_id
    for x in range(len(room)//2):
        paper = room[box_to_open]
        if paper == prisoner_id:
            return True
        box_to_open = paper
    return False

def handle_prisoner_random(room, prisoner_id):
    for x in range(len(room)//2):
        box_to_open = random.choice(list(room.keys()))
        paper = room[box_to_open]
        if paper == prisoner_id:
            return True
    return False

def cycle_prisoners(room, prisoner_count):
    stat = {"loop": True, "random": True}
    for x in range(1, prisoner_count + 1):
        if stat["loop"] and not handle_prisoner_loop(room, x):
            stat["loop"] = False
        if stat["random"] and not handle_prisoner_random(room, x):
            stat["random"] = False
    return stat

if __name__ == "__main__":
    stats = {"loop_success": 0, "loop_fail": 0, "random_success": 0, "random_fail": 0}
    with tqdm.tqdm(total=try_amount) as pbar:
        for x in range(try_amount):
            room = create_room(prisoner_count)
            result = cycle_prisoners(room, prisoner_count)
            if result["loop"]:
                stats["loop_success"] += 1
            else:
                stats["loop_fail"] += 1

            if result["random"]:
                stats["random_success"] += 1
            else:
                stats["random_fail"] += 1

            pbar.update(1)

    print(f"Loop success: {stats['loop_success'] / try_amount * 100}% ({stats['loop_success']}), fail: {stats['loop_fail'] / try_amount * 100}% ({stats['loop_fail']})")
    print(f"Random success: {stats['random_success'] / try_amount * 100}% ({stats['random_success']}), fail: {stats['random_fail'] / try_amount * 100}% ({stats['random_fail']})")