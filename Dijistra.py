from settings import blocksize


class Node:
    def __init__(self, point):
        self.adjacents = []

        self.visited = False
        self.distance = float('inf')
        self.point = point

    def add_adjacent(self, adjacent):
        self.adjacents.append(adjacent)

        if self not in adjacent.adjacents:
            adjacent.add_adjacent(self)


def shortest_distance(first, last, graph):
    for lineN in graph:
        for elemN in lineN:
            elemN.visited = False
            elemN.distance = float('inf')

    first.distance = 0
    queue = [first]

    while len(queue) != 0:
        current = queue.pop(0)

        for adjacent in current.adjacents:
            if not adjacent.visited:
                if current.distance + 1 < adjacent.distance:
                    adjacent.distance = current.distance + 1
                if adjacent not in queue:queue.append(adjacent)
        current.visited = True

    return last.distance


def get_right_path(path):
    res = []

    for node in path:
        res.append([node.point[0]*blocksize[0], node.point[1]*blocksize[1]])

    return res

def find_path(first, last):
    queue = [last]
    path = [last]

    while len(queue) != 0:
        current = queue.pop(0)

        aim = current
        for adjacent in current.adjacents:
            if adjacent.distance + 1 == current.distance:
                aim = adjacent
        if aim==current:break
        path.append(aim)
        queue.append(aim)

        if aim == first:
            break

    path.reverse()
    return get_right_path(path)


def create_graph(labirynt, ghosts):
    graph = [[]]
    planche = labirynt.planche

    y = 0
    for line in planche:
        for elem in line:
            graph[y].append(Node(elem))
        graph.append([])
        y += 1
    graph.pop(-1)

    y = 0
    for lineG in graph:
        x=0
        for elemG in lineG:

            if elemG.point == [-1, -1] or [blocksize[0]*e for e in elemG.point] in [g.pos for g in ghosts]:
                x+=1
                continue
            if x==0 and [blocksize[0]*e for e in lineG[len(lineG)-1].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(lineG[len(lineG)-1])
            elif x==len(lineG)-1 and [blocksize[0]*e for e in lineG[0].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(lineG[0])
            elif y==0 and [blocksize[0]*e for e in graph[len(graph)-2][x].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(graph[len(graph)-2][x])
            elif y==len(graph)-1 and [blocksize[0]*e for e in graph[0][x].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(graph[0][x])

            if x > 0 and lineG[x - 1].point != [-1, -1] and [blocksize[0]*e for e in lineG[x - 1].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(lineG[x - 1])
            if x < len(lineG) - 1 and lineG[x + 1].point != [-1, -1] and [blocksize[0]*e for e in lineG[x + 1].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(lineG[x + 1])
            if y > 0 and graph[y - 1][x].point != [-1, -1] and [blocksize[0]*e for e in graph[y - 1][x].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(graph[y-1][x])
            if y < len(graph) - 2 and graph[y + 1][x].point != [-1, -1] and [blocksize[0]*e for e in graph[y + 1][x].point] not in [g.pos for g in ghosts]:
                elemG.add_adjacent(graph[y+1][x])
            x += 1
        y += 1

    return graph


def shortest_path(source, aim, graph):

    sourceN = Node((0, 0))
    aimN = Node((0, 0))

    source = [v // bs for v, bs in zip(source, blocksize)]
    aim = [v // bs for v, bs in zip(aim, blocksize)]

    for lineG in graph:
        for elemG in lineG:
            if elemG.point == source: sourceN = elemG
            if elemG.point == aim: aimN = elemG

    shortest_distance(sourceN, aimN, graph)
    return find_path(sourceN, aimN)