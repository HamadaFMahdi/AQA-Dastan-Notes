## Notes

### The Board
* The conceptual board is a 2D array.
* Whereas in `self._Board` it is a 1D array.
* To convert between the two we need to use the `__GetIndexOfSquare` method found in the `Dastan` class.

#### Explaining the `__GetIndexOfSquare` method
* What is `SquareReference`?
* `SquareReference` is an 2 digit integer where the row is the first digit and the coloumn is the second digit.
* E.g. 23 -> 2 is the row and 3 is the coloumn.
* How do we get the row and coloumn:

```python
Row = SquareReference // 10
Col = SquareReference % 10
```

Method 1:
```python
sr = 23
sr_str = str(23)
row = sr_str[0]
col = sr_str[1]
```

Method 2: Mathematical way
```python
23 / 10 => 2.3
# now round it down
# We get 2
# Using // with 10 ALWAYS returns the first digit.

23 % 10 => 3
# Using % with 10 ALWAYS returns the last digit.
```

The formula:
```python
(Row - 1) * self._NoOfColumns + (Col - 1)
# Row & Col start from 1 in the conceptual board.
# The resultant index is zero based
```
Example: 
```python
# CONCEPTUAL: [
#     [' ', ' ', '!'], R = 0, C = 2
#     [' ', ' ', '!'],
#     ['?', ' ', '!'],
#     [' ', '?', '!'], R = 3, C = 2
# ]

# ACTUAL: [' ', ' ', '!', ' ', ' ', '!', '?', ' ', '!', ' ', '?', '!']
```
23 which is the '!' on the second row (not zero based)
Row = 2
Col = 3
Index = (2-1) * 3 + (3-1) => 5 (which IS zero based in the actual list)

### Adding a move

#### Generic steps:
* Create a method for it e.g. `__CreateChowkidarMoveOption`.
* Define moves and add to possible moves using `AddToPossibleMoves`.
* Add to `__CreateMoveOption`.
* Add to `__CreateMoveOptions`.

### Adding a piece

#### Generic steps:
* Add to `__CreatePieces`.
* Add it as a move using steps above.

### Adding a piece that gives points for occupancy
#### Generic steps:
* Create class like the `Kotla` class which inherits from `Square`.
* Use `super` in constructor.
* Then we **override** the `GetPointsForOccupancy` method.
