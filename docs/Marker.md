<!-- markdownlint-disable -->

<a href="../src/Marker.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Marker`




**Global Variables**
---------------
- **FILE_DIR**


---

<a href="../src/Marker.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Marker`




<a href="../src/Marker.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(x: float, y: float, z: float, label: str = None)
```

Initialize a Marker with position (x, y, z) and an optional label. 

:param x: X coordinate of the marker. :param y: Y coordinate of the marker. :param z: Z coordinate of the marker. :param label: Optional label or identifier for the marker. 




---

<a href="../src/Marker.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_transformation`

```python
apply_transformation(transformation_matrix: ndarray)
```

Apply a 4x4 transformation matrix to the marker's position. 

:param transformation_matrix: A 4x4 transformation matrix that includes rotation and translation. 

---

<a href="../src/Marker.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `distance_to`

```python
distance_to(other)
```

Compute the Euclidean distance between this marker and another marker. 

:param other: Another Marker object. :return: The Euclidean distance between the two markers. 

---

<a href="../src/Marker.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_position`

```python
get_position()
```

Return the position of the marker as a numpy array (x, y, z). 

---

<a href="../src/Marker.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `move_by`

```python
move_by(dx: float, dy: float, dz: float)
```

Move the marker by a given amount in the x, y, and z directions. 

---

<a href="../src/Marker.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_position`

```python
set_position(x: float, y: float, z: float)
```

Set a new position for the marker. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
