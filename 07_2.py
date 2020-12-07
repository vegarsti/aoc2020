from typing import Set, Tuple


def bag_node(line: str) -> Tuple[str, Set[Tuple[str, int]]]:
    bag_kind, contains = [
        i.strip() for i in line.replace("bags", "bag").replace("bag", "").replace(".", "").split("contain")
    ]
    if contains == "no other":
        return bag_kind, set()
    contains_bags = set((" ".join(c.split()[1:]), int(c.split()[0])) for c in contains.split(","))
    return bag_kind, contains_bags


def bag_contains(bag_kind: str) -> int:
    return sum(count * (bag_contains(kind) + 1) for kind, count in graph[bag_kind])


with open("input/07.txt", "r") as f:
    lines = f.readlines()

nodes = (bag_node(line) for line in lines)
graph = {node: neighbor for node, neighbor in nodes}


print(bag_contains("shiny gold"))
