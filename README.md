# elevator-simulator
- Provide code that simulates an elevator. You are free to use any language.
- Document all assumptions and any features that weren't implemented.
- The result should be an executable, or script, that can be run with the following inputs and generate the following outputs.
        Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
        Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32)
        Program Constants: Single floor travel time: 10


## Assumptions
1. Starting floor `--start` is required and at least one floor `--floor` is also required.
2. Although it may take 10 seconds to travel to a different floor, this simulator will not wait the ten seconds for calculating total travel time.
3. There is no upper or lower floor limit. For example, the elevator may need to travel to a underground bunker deep within Cheyenne Mountain (floor < 0), or to the top of the future space elevator into LEO.
4. Numbers such as `e` or in scientific notation are not allowed. Must be whole numbers (integers)


## Features that were not implemented
- Visual representation of elevator moving between floors. Would have been cool to do in HTML Canvas but was out of scope for this project.
- Any optimizations for reducing elevator travel time. For example given the starting floor 12 and traveling to 2,9,1,32, the elevator could be optimized to stop at 9 on its way to 2, then go to 1, before finishing at 32. 


## Running the simulator
To run the simulator simply call your python executable and point to .\src\elevator.py, on Windows, or ./src/elevator.py on Linux. Example: `py .\src\elevator.py --start=12 --floor=2,9,1,32`. Run `py .\src\elevator.py --help` for additional information.


## Tests
To run the tests: `py .\src\test_elevator.py`
