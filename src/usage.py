import os
import sys
import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR)

from Marker import Marker
from RigidBody import RigidBody
from Link import Link
from Skeleton import Skeleton

# 1. Create Markers for the Skeleton
# Head
marker_head = Marker(x=0.0, y=0.0, z=1.8, label="Head")
# Neck
marker_neck = Marker(x=0.0, y=0.0, z=1.6, label="Neck")
# Shoulders
marker_left_shoulder = Marker(x=-0.5, y=0.0, z=1.5, label="Left Shoulder")
marker_right_shoulder = Marker(x=0.5, y=0.0, z=1.5, label="Right Shoulder")
# Elbows
marker_left_elbow = Marker(x=-0.8, y=0.0, z=1.2, label="Left Elbow")
marker_right_elbow = Marker(x=0.8, y=0.0, z=1.2, label="Right Elbow")
# Hands
marker_left_hand = Marker(x=-1.0, y=0.0, z=1.0, label="Left Hand")
marker_right_hand = Marker(x=1.0, y=0.0, z=1.0, label="Right Hand")
# Torso
marker_torso = Marker(x=0.0, y=0.0, z=1.0, label="Torso")
# Hips
marker_left_hip = Marker(x=-0.5, y=0.0, z=0.8, label="Left Hip")
marker_right_hip = Marker(x=0.5, y=0.0, z=0.8, label="Right Hip")
# Knees
marker_left_knee = Marker(x=-0.5, y=0.0, z=0.5, label="Left Knee")
marker_right_knee = Marker(x=0.5, y=0.0, z=0.5, label="Right Knee")
# Feet
marker_left_foot = Marker(x=-0.5, y=0.0, z=0.0, label="Left Foot")
marker_right_foot = Marker(x=0.5, y=0.0, z=0.0, label="Right Foot")

# 2. Create Links between the Markers
link1 = Link(marker_head, marker_neck, label="Head-Neck")
link2 = Link(marker_neck, marker_left_shoulder, label="Neck-Left Shoulder")
link3 = Link(marker_neck, marker_right_shoulder, label="Neck-Right Shoulder")
link4 = Link(marker_left_shoulder, marker_left_elbow, label="Left Shoulder-Elbow")
link5 = Link(marker_right_shoulder, marker_right_elbow, label="Right Shoulder-Elbow")
link6 = Link(marker_left_elbow, marker_left_hand, label="Left Elbow-Hand")
link7 = Link(marker_right_elbow, marker_right_hand, label="Right Elbow-Hand")
link8 = Link(marker_neck, marker_torso, label="Neck-Torso")
link9 = Link(marker_torso, marker_left_hip, label="Torso-Left Hip")
link10 = Link(marker_torso, marker_right_hip, label="Torso-Right Hip")
link11 = Link(marker_left_hip, marker_left_knee, label="Left Hip-Knee")
link12 = Link(marker_right_hip, marker_right_knee, label="Right Hip-Knee")
link13 = Link(marker_left_knee, marker_left_foot, label="Left Knee-Foot")
link14 = Link(marker_right_knee, marker_right_foot, label="Right Knee-Foot")

# 3. Define a RigidBody with Position and Orientation
# Position at (0, 0, 1) and rotation of 0 degrees around the Z-axis
rigid_body_position = [0.0, 0.0, 1.0]
rigid_body_orientation = [0, 0, 0]  # Euler angles in radians
rigid_body = RigidBody(*rigid_body_position, orientation=rigid_body_orientation, is_quaternion=False, label="RigidBody")

# 4. Create a Skeleton and Add Links
skeleton = Skeleton(label="Human Skeleton", rigid_body=rigid_body)
skeleton.add_link(link1)
skeleton.add_link(link2)
skeleton.add_link(link3)
skeleton.add_link(link4)
skeleton.add_link(link5)
skeleton.add_link(link6)
skeleton.add_link(link7)
skeleton.add_link(link8)
skeleton.add_link(link9)
skeleton.add_link(link10)
skeleton.add_link(link11)
skeleton.add_link(link12)
skeleton.add_link(link13)
skeleton.add_link(link14)

# 5. Check Continuity of the Skeleton
is_continuous = skeleton.is_continuous()
print(f"Skeleton is continuous: {is_continuous}")

# 6. Calculate and Print Total Length of Skeleton
total_length = skeleton.total_length()
print(f"Total length of the skeleton: {total_length:.2f}")

# 7. Get All Markers in the Skeleton
all_markers = skeleton.get_all_markers()
print("Markers in the skeleton:")
for marker in all_markers:
    print(marker)

# 8. Calculate Angles Between Links
angles = skeleton.link_angles()
print("Angles between consecutive links (radians):", angles)

# 9. Apply the RigidBody Transformation to the Entire Skeleton
# skeleton.apply_rigid_body_transform()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 10. Visualize the Skeleton
skeleton.plot(ax)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Human Skeleton Visualization')
plt.legend()
plt.show()
