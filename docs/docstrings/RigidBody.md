<!-- markdownlint-disable -->

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `RigidBody`






---

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L4"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RigidBody`




<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    x: float,
    y: float,
    z: float,
    orientation=None,
    is_quaternion=False,
    label: str = None
)
```

Initialize a RigidBody with position (x, y, z) and orientation. 

:param x: X coordinate of the body. :param y: Y coordinate of the body. :param z: Z coordinate of the body. :param orientation: Orientation as either a quaternion or Euler angles in radians.  If None, default orientation is used (identity rotation). :param is_quaternion: If True, 'orientation' is treated as a quaternion, otherwise Euler angles (radians). 




---

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_euler`

```python
as_euler(degrees=False)
```

Return the orientation as Euler angles (x, y, z) in degrees. 

:param degrees: Bool variable to choose if the return should be in degrees. 

---

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_quaternion`

```python
as_quaternion()
```

Return the orientation as a quaternion (x, y, z, w). 

---

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_inverse_transformation_matrix`

```python
get_inverse_transformation_matrix()
```

Return the inverse of the 4x4 transformation matrix. The inverse is calculated as following. 

| R^T(3x3)    -R^T * T(3x1)  | |   0  0  0         1        | 

Where R^T is the transpose (inverse) of the rotation matrix, and T is the translation vector. 

---

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_transformation_matrix`

```python
get_transformation_matrix()
```

Return the 4x4 transformation matrix that includes both the rotation and the translation. 

The matrix is in the form: 

| R(3x3)  T(3x1)  | |  0 0 0    1     | 

---

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_orientation`

```python
update_orientation(orientation, is_quaternion=False)
```

Update the orientation of the rigid body. 

---

<a href="https://github.com/<you github account>/<your repo>/blob/master/src/RigidBody.py#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_position`

```python
update_position(x: float, y: float, z: float)
```

Update the position of the rigid body. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
