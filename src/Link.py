import os
import sys
import numpy as np
from typing import Optional
import matplotlib.pyplot as plt

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR)

from Marker import Marker

class Link:
    def __init__(self, marker1: Marker, marker2: Marker, label: Optional[str] = None) -> None:
        """Initialize a Link between two distinct markers.
        
        :param marker1: The first Marker instance.
        :param marker2: The second Marker instance.
        :param label: Optional label for the link.
        :raises ValueError: If marker1 and marker2 are the same instance.
        """
        if marker1 is marker2:
            raise ValueError("marker1 and marker2 must be distinct markers.")
        self.marker1 = marker1
        self.marker2 = marker2
        self.label = label

        # To be used for the skeleton class
        self.next_link: Optional['Link'] = None  # Reference to the next Link

    def length(self) -> float:
        """Calculate the Euclidean distance (length) between the two markers.
        
        :return: The Euclidean distance between marker1 and marker2.
        """
        return self.marker1.distance_to(self.marker2)

    def midpoint(self) -> np.ndarray:
        """Calculate the midpoint position between the two markers.
        
        :return: Numpy array representing the midpoint position between marker1 and marker2.
        """
        return (self.marker1.get_position() + self.marker2.get_position()) / 2

    def vector(self) -> np.ndarray:
        """Calculate the vector from marker1 to marker2.
        
        :return: Numpy array representing the vector from marker1 to marker2.
        """
        return self.marker2.get_position() - self.marker1.get_position()

    def is_collinear_with(self, other: "Link", tolerance: float = 1e-6) -> bool:
        """Determine if this link is collinear with another link.
        
        :param other: Another Link instance to compare with.
        :param tolerance: Tolerance for floating-point comparison (default is 1e-6).
        :return: True if the links are collinear, False otherwise.
        """
        v1 = self.vector()
        v2 = other.vector()
        cross_product = np.cross(v1, v2)
        return np.linalg.norm(cross_product) < tolerance

    def angle_with(self, other: "Link") -> float:
        """Calculate the angle (in radians) between this link and another link.
        
        :param other: Another Link instance to compare with.
        :return: The angle between the two links in radians.
        """
        v1 = self.vector()
        v2 = other.vector()
        
        # Compute the dot product and magnitudes of the vectors
        dot_product = np.dot(v1, v2)
        mag_v1 = np.linalg.norm(v1)
        mag_v2 = np.linalg.norm(v2)
        
        # Compute the cosine of the angle
        cos_theta = dot_product / (mag_v1 * mag_v2)
        
        # Clamp cos_theta to avoid floating-point errors outside valid range
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        
        # Return the angle in radians
        return np.arccos(cos_theta)

    def plot(self, ax: plt.Axes, marker_color: str = 'r', line_color: str = 'k') -> None:
        """Plot the markers and the link on the given Matplotlib axis.
        
        :param ax: The Matplotlib axis to plot on.
        :param marker_color: Color of the first marker. Default is red.
        :param line_color: Color of the line connecting the markers. Default is black.
        """
        # Get positions of the markers
        pos1 = self.marker1.get_position()
        pos2 = self.marker2.get_position()
        
        # Plot the markers
        self.marker1.plot(ax, color=marker_color)
        self.marker2.plot(ax, color=marker_color)
        
        # Plot the line connecting the markers
        ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], [pos1[2], pos2[2]], color=line_color)

    def __repr__(self) -> str:
        """String representation of the Link, showing its label and length.
        
        :return: String representation of the Link.
        """
        label_str = f"Label: {self.label}" if self.label else "No Label"
        return f"Link({label_str}, Length: {self.length():.2f})"
