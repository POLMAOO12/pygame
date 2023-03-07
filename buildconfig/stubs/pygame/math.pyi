import sys
from typing import (
    Any,
    Generic,
    Iterator,
    List,
    Literal,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    final,
    overload,
    Optional
)

if sys.version_info >= (3, 9):
    from collections.abc import Collection
else:
    from typing import Collection

def clamp(value: float, min: float, max: float) -> float: ...

_TVec = TypeVar("_TVec", bound=_GenericVector)

# not implemented in code, only implemented here for ease of implementing
# typestubs. Contains attributes/methods common to Vector2 and Vector3
# Also used with _TVec generics
class _GenericVector(Collection[float]):
    epsilon: float
    __hash__: None  # type: ignore
    def __len__(self) -> int: ...
    @overload
    def __setitem__(self, key: int, value: float) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Union[Sequence[float], _TVec]) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, s: slice) -> List[float]: ...
    def __iter__(self) -> VectorIterator: ...
    def __add__(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    def __radd__(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    def __sub__(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    def __rsub__(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    @overload
    def __mul__(self: _TVec, other: Union[Sequence[float], _TVec]) -> float: ...
    @overload
    def __mul__(self: _TVec, other: float) -> _TVec: ...
    def __rmul__(self: _TVec, other: float) -> _TVec: ...
    def __truediv__(self: _TVec, other: float) -> _TVec: ...
    def __rtruediv__(self: _TVec, other: float) -> _TVec: ...
    def __floordiv__(self: _TVec, other: float) -> _TVec: ...
    def __neg__(self: _TVec) -> _TVec: ...
    def __pos__(self: _TVec) -> _TVec: ...
    def __bool__(self) -> bool: ...
    def __iadd__(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    def __isub__(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    @overload
    def __imul__(self: _TVec, other: Union[Sequence[float], _TVec]) -> float: ...
    @overload
    def __imul__(self: _TVec, other: float) -> _TVec: ...
    def __copy__(self: _TVec) -> _TVec: ...
    copy = __copy__
    def __safe_for_unpickling__(self) -> Literal[True]: ...
    def __contains__(self, other: float) -> bool: ...  # type: ignore[override]
    def dot(self: _TVec, other: Union[Sequence[float], _TVec]) -> float: ...
    def magnitude(self) -> float: ...
    def magnitude_squared(self) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self: _TVec) -> _TVec: ...
    def normalize_ip(self) -> None: ...
    def is_normalized(self) -> bool: ...
    def scale_to_length(self, value: float) -> None: ...
    def reflect(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    def reflect_ip(self: _TVec, other: Union[Sequence[float], _TVec]) -> None: ...
    def distance_to(self: _TVec, other: Union[Sequence[float], _TVec]) -> float: ...
    def distance_squared_to(
        self: _TVec, other: Union[Sequence[float], _TVec]
    ) -> float: ...
    def lerp(
        self: _TVec,
        other: Union[Sequence[float], _TVec],
        value: float,
    ) -> _TVec: ...
    def slerp(
        self: _TVec,
        other: Union[Sequence[float], _TVec],
        value: float,
    ) -> _TVec: ...
    def elementwise(self: _TVec) -> VectorElementwiseProxy[_TVec]: ...
    def angle_to(self: _TVec, other: Union[Sequence[float], _TVec]) -> float: ...
    def move_towards(
        self: _TVec,
        target: Union[Sequence[float], _TVec],
        max_distance: float,
    ) -> _TVec: ...
    def move_towards_ip(
        self: _TVec,
        target: Union[Sequence[float], _TVec],
        max_distance: float,
    ) -> None: ...
    @overload
    def clamp_magnitude(self: _TVec, max_length: float) -> _TVec: ...
    @overload
    def clamp_magnitude(
        self: _TVec, min_length: float, max_length: float
    ) -> _TVec: ...
    @overload
    def clamp_magnitude_ip(self, max_length: float) -> None: ...
    @overload
    def clamp_magnitude_ip(self, min_length: float, max_length: float) -> None: ...
    def project(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    def __round__(self: _TVec, ndigits: Optional[int]) -> _TVec: ...

# VectorElementwiseProxy is a generic, it can be an elementwiseproxy object for
# Vector2, Vector3 and vector subclass objects
@final
class VectorElementwiseProxy(Generic[_TVec]):
    def __add__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __radd__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __sub__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __rsub__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __mul__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __rmul__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __truediv__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __rtruediv__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __floordiv__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __rfloordiv__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __mod__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __rmod__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> _TVec: ...
    def __pow__(
        self,
        power: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
        mod: None = None,
    ) -> _TVec: ...
    def __rpow__(
        self,
        power: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
        mod: None = None,
    ) -> _TVec: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __gt__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> bool: ...
    def __lt__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> bool: ...
    def __ge__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> bool: ...
    def __le__(
        self,
        other: Union[float, _TVec, VectorElementwiseProxy[_TVec]],
    ) -> bool: ...
    def __abs__(self) -> _TVec: ...
    def __neg__(self) -> _TVec: ...
    def __pos__(self) -> _TVec: ...
    def __bool__(self) -> bool: ...

@final
class VectorIterator:
    def __length_hint__(self) -> int: ...
    def __iter__(self) -> Iterator[float]: ...
    def __next__(self) -> float: ...

class Vector2(_GenericVector):
    x: float
    y: float
    xx: Vector2
    xy: Vector2
    yx: Vector2
    yy: Vector2
    @overload
    def __init__(
        self: _TVec,
        x: Union[str, float, Sequence[float], _TVec] = 0,
    ) -> None: ...
    @overload
    def __init__(self, x: float, y: float) -> None: ...
    def __reduce__(self: _TVec) -> Tuple[Type[_TVec], Tuple[float, float]]: ...
    def rotate(self: _TVec, angle: float) -> _TVec: ...
    def rotate_rad(self: _TVec, angle: float) -> _TVec: ...
    def rotate_ip(self, angle: float) -> None: ...
    def rotate_rad_ip(self, angle: float) -> None: ...
    def rotate_ip_rad(self, angle: float) -> None: ...
    def cross(self: _TVec, other: Union[Sequence[float], _TVec]) -> float: ...
    def as_polar(self) -> Tuple[float, float]: ...
    def from_polar(self, polar_value: Tuple[float, float]) -> Optional[_TVec]: ...
    @overload
    def update(
        self: _TVec,
        x: Union[str, float, Sequence[float], _TVec] = 0,
    ) -> None: ...
    @overload
    def update(self, x: float = 0, y: float = 0) -> None: ...

class Vector3(_GenericVector):
    x: float
    y: float
    z: float
    xx: Vector2
    xy: Vector2
    xz: Vector2
    yx: Vector2
    yy: Vector2
    yz: Vector2
    zx: Vector2
    zy: Vector2
    zz: Vector2
    xxx: Vector3
    xxy: Vector3
    xxz: Vector3
    xyx: Vector3
    xyy: Vector3
    xyz: Vector3
    xzx: Vector3
    xzy: Vector3
    xzz: Vector3
    yxx: Vector3
    yxy: Vector3
    yxz: Vector3
    yyx: Vector3
    yyy: Vector3
    yyz: Vector3
    yzx: Vector3
    yzy: Vector3
    yzz: Vector3
    zxx: Vector3
    zxy: Vector3
    zxz: Vector3
    zyx: Vector3
    zyy: Vector3
    zyz: Vector3
    zzx: Vector3
    zzy: Vector3
    zzz: Vector3
    @overload
    def __init__(
        self: _TVec,
        x: Union[str, float, Sequence[float], _TVec] = 0,
    ) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    def __reduce__(self: _TVec) -> Tuple[Type[_TVec], Tuple[float, float, float]]: ...
    def cross(self: _TVec, other: Union[Sequence[float], _TVec]) -> _TVec: ...
    def rotate(
        self: _TVec, angle: float, axis: Union[Sequence[float], _TVec]
    ) -> _TVec: ...
    def rotate_rad(
        self: _TVec, angle: float, axis: Union[Sequence[float], _TVec]
    ) -> _TVec: ...
    def rotate_ip(
        self: _TVec, angle: float, axis: Union[Sequence[float], _TVec]
    ) -> None: ...
    def rotate_rad_ip(
        self: _TVec, angle: float, axis: Union[Sequence[float], _TVec]
    ) -> None: ...
    def rotate_ip_rad(
        self: _TVec, angle: float, axis: Union[Sequence[float], _TVec]
    ) -> None: ...
    def rotate_x(self: _TVec, angle: float) -> _TVec: ...
    def rotate_x_rad(self: _TVec, angle: float) -> _TVec: ...
    def rotate_x_ip(self, angle: float) -> None: ...
    def rotate_x_rad_ip(self, angle: float) -> None: ...
    def rotate_x_ip_rad(self, angle: float) -> None: ...
    def rotate_y(self: _TVec, angle: float) -> _TVec: ...
    def rotate_y_rad(self: _TVec, angle: float) -> _TVec: ...
    def rotate_y_ip(self, angle: float) -> None: ...
    def rotate_y_rad_ip(self, angle: float) -> None: ...
    def rotate_y_ip_rad(self, angle: float) -> None: ...
    def rotate_z(self: _TVec, angle: float) -> _TVec: ...
    def rotate_z_rad(self: _TVec, angle: float) -> _TVec: ...
    def rotate_z_ip(self, angle: float) -> None: ...
    def rotate_z_rad_ip(self, angle: float) -> None: ...
    def rotate_z_ip_rad(self, angle: float) -> None: ...
    def as_spherical(self) -> Tuple[float, float, float]: ...
    def from_spherical(self, spherical_value: Tuple[float, float, float]) -> Optional[_TVec]: ...
    @overload
    def update(
        self: _TVec,
        x: Union[str, float, Sequence[float], _TVec] = 0,
    ) -> None: ...
    @overload
    def update(self, x: int, y: int, z: int) -> None: ...

# typehints for deprecated functions, to be removed in a future version
def enable_swizzling() -> None: ...
def disable_swizzling() -> None: ...
