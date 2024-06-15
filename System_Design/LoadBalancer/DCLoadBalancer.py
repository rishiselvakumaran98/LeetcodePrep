
import heapq
from collections import defaultdict

class DCLoadBalancer:

    def __init__(self):
        # A dictionary that maps machineIds to their current avaible capacities
        self.machineStorage = defaultdict(int)
        # A max-heap (implemented with minheap with neg values) to quicly acess the machine with the highest available capacity
        self.machineHeap = []
        # A dictionary that maps application ids to tuples of (machineIds, loaduse)
        self.appToMachineAndLoad = defaultdict(tuple)
        # A dict mapping the machine Ids to list of apps running in that machine
        self.machineToApp = defaultdict(list)

    def addMachine(self, machineId, capacity): # Time: O(log(n))
        """Adds a new machine with the given capacity to the load balancer"""
        # update the machineStorage with new machine capacity

        # push the machine into "machineHeap" with its capacity (neg for max-heap)

    def addApplication(self, appId, loaduse): # Time: O(log(n))
        """Adds a new application with a specified load to a machine."""
        # Pops the machine with the highest available capacity from machineHeap.

        # If the machine cannot accommodate the application's load, it is pushed back into the heap, and the method returns -1.

        # Otherwise, the application's load is subtracted from the machine's capacity.

        # Updates machineStorage, appToMachineAndLoad, and machineToApp accordingly.

        # Returns the machine ID where the application is deployed.

    def stopApplication(self, appId): # Time: O(N)
        """Stops the specified application and frees up its load from the machine."""

    
    def getApplications(self, machineId): # Time: O(1)
        """Returns a list of up to 10 application IDs currently running on the specified machine."""

    
    def updateHeap(self): # Time: O(N)
        """Rebuilds the machineHeap from the current state of machineStorage"""
        # Creates a new heap list from the machine capacities and IDs.
        # Heapifies the list to maintain the max-heap property.

    
    def removeMachine(self, machineId): # Time: O(N)
        # Removes the machine from machineStorage.
        # Updates machineHeap to reflect the removal.
        # Reassigns all applications running on the removed machine to other machines using addApplication.
