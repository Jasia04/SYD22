import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import math  # Importing math for trigonometric calculations

# Recursive function to draw branches of the tree
def draw_branch(x, y, angle, branch_length, depth, reduction_factor, left_angle, right_angle, ax):
    if depth == 0:  # Base case: stop when depth reaches 0
        return

    # Calculating the end point of the current branch using angle and length
    x_end = x + branch_length * math.cos(math.radians(angle))
    y_end = y + branch_length * math.sin(math.radians(angle))

    # Drawing the current branch
    ax.plot([x, x_end], [y, y_end],
            color='brown' if depth == original_depth else 'green',  # Trunk = brown, branches = green
            linewidth=depth)  # Line width decreases with depth

    # Recursive call to draw the left branch
    draw_branch(x_end, y_end,
                angle + left_angle,  # Turn left
                branch_length * reduction_factor,  # Shorten branch
                depth - 1, reduction_factor, left_angle, right_angle, ax)

    # Recursive call to draw the right branch
    draw_branch(x_end, y_end,
                angle - right_angle,  # Turn right
                branch_length * reduction_factor,  # Shorten branch
                depth - 1, reduction_factor, left_angle, right_angle, ax)

# --------- USER INPUT PARAMETERS ---------
left_angle = float(input("Enter left branch angle: "))              # Angle to the left for branching
right_angle = float(input("Enter right branch angle: "))            # Angle to the right for branching
starting_length = float(input("Enter starting branch length: "))    # Initial branch (trunk) length
depth = int(input("Enter recursion depth: "))                       # Number of recursive layers
original_depth = depth                                              # Save original depth for styling
reduction = float(input("Enter branch length reduction factor (e.g., 0.7): "))  # Reduction factor
# -----------------------------------------

# Creating a new figure and axis for plotting
fig, ax = plt.subplots()
ax.set_aspect('equal')        # Keep x and y scales equal
ax.axis('off')                # Hide the axis for better tree appearance

# Start drawing from the bottom center (x=0, y=0), pointing straight up (angle = 90 degrees)
draw_branch(x=0, y=0,
            angle=90,
            branch_length=starting_length,
            depth=depth,
            reduction_factor=reduction,
            left_angle=left_angle,
            right_angle=right_angle,
            ax=ax)

# Showing the resulting tree
plt.show()
