from typing import Set, Tuple


def bag_node(line: str) -> Tuple[str, Set[str]]:
    bag_kind, contains = [
        i.strip() for i in line.replace("bags", "bag").replace("bag", "").replace(".", "").split("contain")
    ]
    if contains == "no other":
        return bag_kind, set()
    contains_bags = set(" ".join(c.split()[1:]) for c in contains.split(","))
    return bag_kind, contains_bags


def depth_first_search(starting_node: str, current_node: str, can_visit: Set[str]) -> None:
    for neighbor in graph[current_node]:
        if neighbor == "shiny gold":
            can_visit.add(starting_node)
        depth_first_search(starting_node=starting_node, current_node=neighbor, can_visit=can_visit)


with open("input/07.txt", "r") as f:
    lines = f.readlines()


nodes = [bag_node(line) for line in lines]
graph = {node: neighbor for node, neighbor in nodes}


can_contain_shiny_gold: Set[str] = set()
for node in graph.keys():
    depth_first_search(starting_node=node, current_node=node, can_visit=can_contain_shiny_gold)
print(len(can_contain_shiny_gold))
