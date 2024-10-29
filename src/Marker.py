import sys
import os
import math
import numpy as np
from scipy.spatial.transform import Rotation as R
from typing import Optional
import matplotlib.pyplot as plt

class Marker:
    def __init__(self, x: float, y: float, z: float, label: Optional[str] = None) -> None:
        """Initialize a Marker with position (x, y, z) and an optional label.
        
        :param x: X coordinate of the marker.
        :param y: Y coordinate of the marker.
        :param z: Z coordinate of the marker.
        :param label: Optional label or identifier for the marker.
        :raises ValueError: If x, y, or z are not finite values.
        """
        if not(math.isfinite(x)):
            raise ValueError("x must be finite")
        if not(math.isfinite(y)):
            raise ValueError("y must be finite")
        if not(math.isfinite(z)):
            raise ValueError("z must be finite")
        self.position = np.array([x, y, z])
        self.label = label
    
    def get_position(self) -> np.ndarray:
        """Return the position of the marker as a numpy array (x, y, z).
        
        :return: Numpy array representing the marker's position.
        """
        return self.position

    def set_position(self, x: float, y: float, z: float) -> None:
        """Set a new position for the marker.
        
        :param x: New X coordinate.
        :param y: New Y coordinate.
        :param z: New Z coordinate.
        """
        self.position = np.array([x, y, z])

    def distance_to(self, other: "Marker") -> float:
        """Compute the Euclidean distance between this marker and another marker.
        
        :param other: Another Marker object.
        :type other: Marker
        :return: The Euclidean distance between the two markers.
        :rtype: float
        :raises TypeError: If `other` is not a Marker instance.
        """
        if not isinstance(other, Marker):
            raise TypeError("Can only compute distance to another Marker.")
        
        return np.linalg.norm(self.position - other.position)

    def move_by(self, dx: float, dy: float, dz: float) -> None:
        """Move the marker by a given amount in the x, y, and z directions.
        
        :param dx: Amount to move in the X direction.
        :param dy: Amount to move in the Y direction.
        :param dz: Amount to move in the Z direction.
        """
        self.position += np.array([dx, dy, dz])

    def apply_transformation(self, transformation_matrix: np.ndarray) -> None:
        """Apply a 4x4 transformation matrix to the marker's position.
        
        :param transformation_matrix: A 4x4 transformation matrix that includes rotation and translation.
        :type transformation_matrix: numpy.ndarray
        :raises ValueError: If the transformation matrix is not 4x4.
        """
        if transformation_matrix.shape != (4, 4):
            raise ValueError("Transformation matrix must be a 4x4 matrix.")
        
        # Convert the position to homogeneous coordinates (x, y, z, 1)
        homogeneous_position = np.append(self.position, 1.0)
        
        # Apply the transformation matrix
        transformed_position = transformation_matrix @ homogeneous_position
        
        # Update the position (ignoring the homogeneous coordinate)
        self.position = transformed_position[:3]

    def plot(self, ax: plt.Axes, color: str = 'r', fontsize: int = 12, font_color: str = 'black') -> None:
        """Plot the marker's position and label on the given Matplotlib axis.
        
        :param ax: The Matplotlib axis to plot on.
        :param color: Color of the marker point. Default is red.
        :param fontsize: Font size of the label text. Default is 12.
        :param font_color: Color of the label text. Default is black.
        """
        # Get the marker position
        pos = self.get_position()
        
        # Plot the marker as a point
        ax.scatter(pos[0], pos[1], pos[2], color=color, s=50)
        
        # Annotate the label next to the marker
        if self.label:
            ax.text(pos[0], pos[1], pos[2], self.label, fontsize=fontsize, color=font_color)

    def __repr__(self) -> str:
        """String representation of the Marker, showing its label and position.
        
        :return: String representation of the marker.
        :rtype: str
        """
        pos_str = f"Position: {self.position}"
        label_str = f"Label: {self.label}" if self.label else "No Label"
        return f"Marker({label_str}, {pos_str})"
