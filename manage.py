import os
from pathlib import Path


PARTICIPANTS = ["kairat", "mj", "doohoon", "hyun", "hyunjin", "dongchang", "beoms"]


def touch(chapter_num, participants):
    for top in ('bitcoin', 'cookbook'):
        dname = f'{top}/ch{chapter_num:02d}'
        for p in participants:
            path = f'{dname}/{p}'
            os.makedirs(path)
            Path(f'{path}/remove_this').touch()


if __name__ == '__main__':
    touch(7, PARTICIPANTS)
