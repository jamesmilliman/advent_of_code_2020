class Graph:
    def __init__(self, V):
        self.V = V
        self.map = {}
        self.inv_map = {}
        self.last = 0
        self.data = [[] for _ in range(self.V)]
        self.E = 0

    def _lookup(self, key):
        try:
            return self.map[key]
        except KeyError:
            ret = self.last
            self.map[key] = ret
            self.inv_map[ret] = key
            self.last += 1
            return ret

    def addEdge(self, s, d, weight=0):
        sv = self._lookup(s)
        dv = self._lookup(d)

        self.data[sv].append((dv, weight))
        self.E += 1

    def _dfs(self, s, visited):
        if visited[s]:
            return

        visited[s] = True
        for each, _ in self.data[s]:
            self._dfs(each, visited)

    def dfs(self, s):
        visited = [False for _ in range(self.V)]
        sv = self._lookup(s)

        self._dfs(sv, visited)

        return visited

    def bag_count(self, s):
        if isinstance(s, str):
            s = self._lookup(s)

        return sum(map(lambda x: self.bag_count(x[0]) * x[1] + x[1], self.data[s]))


def parse_bag_with_num(s):
    temp = s.strip().split(" ")
    try:
        return " ".join(temp[1:3]), int(temp[0])
    except ValueError:
        return None


# I'm not proud of this one
def parse_bags(line):
    line = line.split(" ")
    outer = " ".join(line[:2])
    inner = list(
        filter(
            lambda x: x is not None,
            map(parse_bag_with_num, " ".join(line[4:]).split(",")),
        )
    )

    return outer, inner


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        data = list(map(parse_bags, lines))

    g1 = Graph(len(data))
    for outer, inner in data:
        for each, _ in inner:
            g1.addEdge(each, outer)

    g2 = Graph(len(data))
    for outer, inner in data:
        for each, weight in inner:
            g2.addEdge(outer, each, weight)

    # p1
    visited = g1.dfs("shiny gold")
    print(sum(visited) - 1)

    # p2
    print(g2.bag_count("shiny gold"))
