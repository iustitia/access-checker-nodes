import logging
logger = logging.getLogger(__name__)


class AccessChecker:

    def __init__(self, peer_connections, online_statuses):

        if not peer_connections:
            logger.exception("Peer connection info is empty. Check if you passed a proper value")
        if online_statuses is None:
            logger.exception("Data about online statuses is missing.")

        self.graph = peer_connections
        self.online = online_statuses

    def is_connected(self, start, end, recursive=False):
        if start not in self.online or end not in self.online:
            return False

        if recursive:
            self.visited = []
            self.stack = []
            return self.dfs_recursive(start, end)

        return self.dfs(start, end)

    def dfs_recursive(self, start, end):

        if end in self.graph[start]:
            return True

        for node in self.graph[start]:
            if node in self.online and node not in self.visited:
                self.visited.append(node)
                x = self.dfs_recursive(node, end)
                if x:
                    return True

        return False

    def dfs(self, start, end):

        if end in self.graph[start]:
            return True

        stack = []
        stack.append(start)
        visited = {start: True}

        while stack:

            current = stack.pop()

            for node in self.graph[current]:
                if node not in visited and node in self.online:
                    if node == end:
                        return True
                    stack.append(node)
                    visited[node] = True

        return False
