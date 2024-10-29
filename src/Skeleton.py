import os
import sys
from typing import List, Optional
import numpy as np
import matplotlib.pyplot as plt

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR)

from RigidBody import RigidBody
from Link import Link
from Marker import Marker

class Skeleton:
    def __init__(self, label: Optional[str] = None, rigid_body: Optional[RigidBody] = None) -> None:
        """Initialize a Skeleton with an optional label and root rigid body.
        
        :param label: Optional label or identifier for the skeleton.
        :param rigid_body: Optional RigidBody defining the root transformation of the skeleton.
        """
        self.links: List[Link] = []  # Use a list to store links
        self.rigid_body = rigid_body if rigid_body else RigidBody(0, 0, 0)  # Default to origin
        self.label = label

    def add_link(self, new_link: Link) -> None:
        """Add a new link to the skeleton, connecting it to the last link if they share a marker.
        
        :param new_link: The Link object to add to the skeleton.
        :raises ValueError: If the link cannot be connected in the skeleton.
        """
        if not self.links:
            # If there are no links, add the new link as the first link
            self.links.append(new_link)
            return
        
        # Check the last link for a connection
        last_link = self.links[-1]
        
        # Try to connect the new link to the last link
        if last_link.marker2 == new_link.marker1:
            self.links.append(new_link)
        elif last_link.marker2 == new_link.marker2:
            new_link.marker1, new_link.marker2 = new_link.marker2, new_link.marker1
            self.links.append(new_link)
        else:
            # Check existing links for a connection to the new link
            for existing_link in self.links:
                if existing_link.marker2 == new_link.marker1:
                    self.links.append(new_link)
                    return
                elif existing_link.marker2 == new_link.marker2:
                    new_link.marker1, new_link.marker2 = new_link.marker2, new_link.marker1
                    self.links.append(new_link)
                    return
            raise ValueError("New link cannot connect to any existing link in the skeleton.")

    def is_continuous(self) -> bool:
        """Check if the skeleton forms a continuous chain of links.
        
        :return: True if the skeleton is continuous, False otherwise.
        """
        for i in range(len(self.links) - 1):
            if self.links[i].marker2 != self.links[i + 1].marker1:
                return False
        return True

    def apply_rigid_body_transform(self) -> None:
        """Apply the RigidBody transformation to all markers in the skeleton."""
        transformation_matrix = self.rigid_body.get_transformation_matrix()
        for link in self.links:
            link.marker1.apply_transformation(transformation_matrix)
            link.marker2.apply_transformation(transformation_matrix)

    def plot(self, ax: plt.Axes) -> None:
        """Visualize the skeleton as a 3D plot, showing markers and links."""
        if not self.links:
            print("No links to display.")
            return
        
        self.rigid_body.plot(ax)
        for link in self.links:
            link.plot(ax)

    def total_length(self) -> float:
        """Calculate the total length of all links in the skeleton.
        
        :return: The sum of the lengths of all links in the skeleton.
        """
        return sum(link.length() for link in self.links)

    def get_all_markers(self) -> List[Marker]:
        """Retrieve all unique markers in the skeleton.
        
        :return: A list of unique Marker objects used in the skeleton.
        """
        markers = {link.marker1 for link in self.links}
        markers.update(link.marker2 for link in self.links)
        return list(markers)

    def link_angles(self) -> List[float]:
        """Calculate the angles between consecutive links in the skeleton.
        
        :return: A list of angles (in radians) between consecutive links.
        """
        angles = []
        for i in range(len(self.links) - 1):
            angle = self.links[i].angle_with(self.links[i + 1])
            angles.append(angle)
        return angles

    def __repr__(self) -> str:
        """String representation of the Skeleton, showing its label and total length.
        
        :return: String representation of the Skeleton.
        """
        label_str = f"Label: {self.label}" if self.label else "No Label"
        return f"Skeleton({label_str}, Total Length: {self.total_length():.2f}, Links: {len(self.links)})"

    def get_all_links(self) -> List[Link]:
        """Retrieve all links in the skeleton in sequence.
        
        :return: A list of Link objects in the skeleton.
        """
        return self.links
