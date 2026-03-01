import argparse

# Function for parsing the input --floor arguments 
# inputs a string
# outputs a list of floors
def list_floors(s: str) -> list[int]:
    try:
        if s.strip() == "":
            raise "Invalid argument"
        
        floors = s.split(',')
        return [int(x) for x in floors if x != ""]
    except Exception as e:
        raise argparse.ArgumentTypeError(
            f"Invalid --floor value {s!r}. Expected comma-separated integers like 2,9,1,32"
        ) from e



# Time to travel from one floor to another
timeToFloor = 10


# Function to calculate the total floors the elevator traverses
# input a list of all floors in order
# output total floors int
def num_traversed_floors(floors: list[int]) -> int:
    total = 0
    if len(floors) > 1:
        # Need abs because you cannot travel negative floors
        total = abs(floors[0] - floors[1])
        floors.pop(0)
        if (len(floors) > 1):
            total += num_traversed_floors(floors)
    
    return total



# This function takes the list of floors to traverse
# and calculates the total time to traverse all floors
def run_time(allFloors: list[int]) -> int:
    totalTraversed = num_traversed_floors(allFloors)
    return totalTraversed * timeToFloor



# Helper function for printing floors
def convert_ints_to_strs(li: list[int]) -> list[str]:
    strList: list[str] = []
    for x in li:
        strList.append(str(x))

    return strList



def main(start: int, floor: list[int]) -> list[str]:
    allFloors = [start, *floor]
    time = run_time([*allFloors]) # Use * here because pop above removes items in place

    allFloorsStr = ','.join(convert_ints_to_strs(allFloors))
    # print(f"It takes the elevator {time}t to traverse these floors {allFloorsStr}")
    
    return [time, allFloorsStr]



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that simulates an elevator moving between floors and returns the time it takes."
    )
    parser.add_argument("--start", required=True, type=int, help="Where the elevator starts")
    parser.add_argument("--floor", type=list_floors, required=True, help="Comma-separated ints")

    args = parser.parse_args()

    start = args.start
    floor = args.floor
    
    [time, allFloorsStr] = main(start, floor)

    print(f"{time} {allFloorsStr}")