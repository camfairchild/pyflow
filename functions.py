import sys
from os.path import abspath
from pathlib import Path
from typing import List, Set, Tuple

from plantuml import PlantUML


def file_to_list(filename: str) -> Tuple[Set[str], List[str]]:
    with open(filename) as f:
        lines = f.read().splitlines()
        lst = set([])
        conn = []
        for line in lines:
            parse(line, lst, conn)
        return lst, conn
    raise "File error. Maybe name is wrong?"

def parse(line: str, lst: Set[str], conn: List[str]) -> None:
    blk1, blk2 = line.split(' to ')
    n1 = fix_name(blk1)
    n2 = fix_name(blk2)
    lst.add(f"agent \"{blk1}\" as {n1}\n")
    lst.add(f"agent \"{blk2}\" as {n2}\n")
    conn.append(f"{n1} --> {n2}\n")

def fix_name(s: str) -> str:
    return s.replace(" ", "_")

def write(filename: str, lst: Set[str], conn: List[str]) -> str:
    new_name: str
    new_name = "plant-" + filename
    with open(new_name, 'w') as f:
        f.write("@startuml\n")
        f.writelines(lst)
        f.writelines(conn)
        f.write("@enduml")
    return new_name

def create_pic(filename: str) -> None:
    server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                          basic_auth={},
                          form_auth={}, http_opts={}, request_opts={})

    # Send and compile your diagram files to/with the PlantUML server
    server.processes_file(abspath(f'./{filename}'))

def do_thing(filename: str) -> None:
        lst, conn = file_to_list(filename)
        new_filename = write(filename, lst, conn)
        create_pic(new_filename)

def read_file(filename_str: str):
    filename = Path(filename_str)
    filename.touch()
    with open(filename, 'r+') as file:
        return file.read()

def save(filename: str, content: str) -> None:
    with open(filename, "w+") as file:
        file.write(content)