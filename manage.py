import os
from pathlib import Path
import shutil


PARTICIPANTS = ["kairat", "mj", "doohoon", "hyun", "hyunjin", "dongchang", "beoms"]


def touch(cur, participants):
    for top in ('bitcoin', 'cookbook'):
        dname = f'{top}/'
        for p in participants:
            path = f'{dname}/{p}'
            os.makedirs(path, exist_ok=True)
            Path(f'{path}/i_didnt_study_chapter_{cur}').touch()


if __name__ == '__main__':
    touch('7_second', PARTICIPANTS)


def get_all_files(dname):
    for name in os.listdir(dname):
        path = os.path.join(dname, name)
        if os.path.isdir(path):
            yield from get_all_files(path)
        else:
            yield path

def migrate(root):
    for path in list(get_all_files(root)):
        for p in PARTICIPANTS:
            if p + '/' in path:
                break
        else:
            print('skip', path)
            continue

        new_path = path.replace('/', '_')
        new_former, chap, name, new_latter = new_path.split('_', 3)
        new_path = new_former + f'/{p}/{chap}_{new_latter}'

        print(path, new_path)
        shutil.move(path, new_path)


# if __name__ == '__main__':
#     migrate('bitcoin')
#     migrate('cookbook')
