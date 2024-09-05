import heapq
from typing import Dict, List, Tuple

class ParkingLot:
    def __init__(self):
        self.graph: Dict[str, Dict[str, int]] = {}
        self.parking_spots: Dict[str, bool] = {}
        self.directions: Dict[Tuple[str, str], str] = {}
    
    def add_node(self, node: str):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, from_node: str, to_node: str, distance: int, direction: str):
        self.add_node(from_node)
        self.add_node(to_node)
        self.graph[from_node][to_node] = distance
        self.graph[to_node][from_node] = distance  # Assuming bidirectional
        self.directions[(from_node, to_node)] = direction
        self.directions[(to_node, from_node)] = self.opposite_direction(direction)

    def opposite_direction(self, direction: str) -> str:
        opposites = {"Left": "Right", "Right": "Left", "Straight": "Straight"}
        return opposites.get(direction, direction)

    def add_parking_spot(self, spot: str, available: bool = True):
        self.add_node(spot)
        self.parking_spots[spot] = available

    def set_spot_availability(self, spot: str, available: bool):
        if spot in self.parking_spots:
            self.parking_spots[spot] = available

    def dijkstra(self, start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0
        previous = {node: None for node in self.graph}
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, previous

    def find_nearest_parking_spot(self, start: str) -> Tuple[str, int, List[str]]:
        distances, previous = self.dijkstra(start)
        nearest_spot = min(
            (spot for spot, available in self.parking_spots.items() if available),
            key=lambda spot: distances[spot]
        )
        
        # Reconstruct the path
        path = []
        current = nearest_spot
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        return nearest_spot, distances[nearest_spot], path

    def Give_directions(self, path: List[str]) -> List[str]:
        directions = []
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            direction = self.directions.get((current_node, next_node), "")
            
            if i == 0:
                directions.append(f"Start at {current_node}")
            
            if direction:
                directions.append(f"Go {direction} to {next_node}")
            else:
                directions.append(f"Move to {next_node}")
            
            if next_node in self.parking_spots:
                directions.append(f"Park at {next_node}")
        
        return directions

# Example usage
parking_lot = ParkingLot()

# Add nodes and edges (simplified parking lot layout)
parking_lot.add_edge("Entrance", "A", 5, "Straight")
parking_lot.add_edge("A", "H", 10, "Straight")
parking_lot.add_edge("A", "B", 5, "Left")
parking_lot.add_edge("B", "P1", 1, "Right")
parking_lot.add_edge("B", "C", 5, "Straight")
parking_lot.add_edge("C", "P2", 1, "Right")
parking_lot.add_edge("C", "D", 5, "Straight")
parking_lot.add_edge("D", "E", 10, "Right")
parking_lot.add_edge("E", "F", 5, "Right")
parking_lot.add_edge("F", "P4", 1, "Right")
parking_lot.add_edge("F", "G", 5, "Straight")
parking_lot.add_edge("G", "P3", 1, "Right")
parking_lot.add_edge("G", "H", 5, "Straight")
parking_lot.add_edge("H", "A", 10, "Straight")
parking_lot.add_edge("H", "G", 5, "Right")

# Add parking spots
parking_lot.add_parking_spot("P1")
parking_lot.add_parking_spot("P2")
parking_lot.add_parking_spot("P3")
parking_lot.add_parking_spot("P4")

# Find nearest parking spot and path
nearest_spot, distance, path = parking_lot.find_nearest_parking_spot("Entrance")
print(f"Nearest available parking spot: {nearest_spot}")
print(f"Distance: {distance}")
print(f"Path to the spot: {' -> '.join(path)}")

# Get directions
directions = parking_lot.Give_directions(path)
print("\nDirections:")
for step in directions:
    print(step)

# Update spot availability
parking_lot.set_spot_availability("P1", False)
parking_lot.set_spot_availability("P2", False)
parking_lot.set_spot_availability("P4", False)

# Find nearest parking spot and path again
nearest_spot, distance, path = parking_lot.find_nearest_parking_spot("Entrance")
print(f"\nNew nearest available parking spot: {nearest_spot}")
print(f"Distance: {distance}")
print(f"Path to the spot: {' -> '.join(path)}")

# Get new directions
directions = parking_lot.Give_directions(path)
print("\nNew Directions:")
for step in directions:
    print(step)