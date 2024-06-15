class RoundRobinLB:

    def __init__(self) -> None:
        self.servers = []
        self.index = 0

    def addServer(self, server): # Time Complexity: O(1)
        self.servers.append(server)
    
    def removeServer(self, server): # Time Complexity: O(n)
        self.servers.remove(server)
        # reset the index
        if self.index >= len(self.servers):
            self.index = 0
    
    def get_server(self): # Time Complexity: O(1)
        # if there are no servers available
        if not self.servers:
            return None
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

if __name__ == "__main__":
    lb = RoundRobinLB()
    lb.add_server("Server1")
    lb.add_server("Server2")
    lb.add_server("Server3")

    print(lb.get_server())  # Server1
    print(lb.get_server())  # Server2
    print(lb.get_server())  # Server3
    print(lb.get_server())  # Server1 again

    lb.remove_server("Server2")
    print(lb.get_server())  # Server3
    print(lb.get_server())  # Server1