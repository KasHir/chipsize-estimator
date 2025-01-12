from rectpack import newPacker
import matplotlib.pyplot as plt
import os

# Block data (width, height)
blocks = [(5, 10), (5, 10), (8, 8), (8, 8), (6, 7), (4, 7), (15, 25),
          (5, 10), (5, 10), (8, 8), (8, 8), (6, 7), (4, 7), (15, 25)]

def find_minimum_chip_size_with_ids(blocks):
    # Calculate the maximum possible width and height
    max_width = sum(block[0] for block in blocks)
    max_height = sum(block[1] for block in blocks)

    # Set the minimum size to the largest single block dimension
    min_size = max(max(block[0] for block in blocks), max(block[1] for block in blocks))

    # Create output directory for saving images
    output_dir = "chip_layouts"
    os.makedirs(output_dir, exist_ok=True)

    # Search for the minimum chip size starting from min_size
    for size in range(min_size, max(max_width, max_height) + 1):
        packer = newPacker()
        for i, block in enumerate(blocks):
            packer.add_rect(*block, rid=i)  # Add block with ID
        print(f"Trying: {size} x {size}")
        packer.add_bin(size, size)  # Add a square bin of current size
        packer.pack()

        # If all blocks are successfully packed
        if len(packer.rect_list()) == len(blocks):
            # Draw and save the layout
            fig, ax = plt.subplots()
            for rect in packer.rect_list():
                x, y, w, h, rid = rect[1], rect[2], rect[3], rect[4], rect[5]
                ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor='blue', facecolor='lightblue'))
                ax.text(x + w / 2, y + h / 2, str(rid), color='red', ha='center', va='center')  # Display block ID
            plt.xlim(0, size)
            plt.ylim(0, size)
            plt.gca().set_aspect('equal', adjustable='box')

            filename = os.path.join(output_dir, f"chip_layout_{size}.png")
            plt.savefig(filename)
            plt.close()

            print(f"Saved layout image: {filename}")
            return size, size

    return None, None

# Find the minimum chip size
chip_width, chip_height = find_minimum_chip_size_with_ids(blocks)

# Output results
if chip_width and chip_height:
    print(f"Minimum chip size: {chip_width} x {chip_height}")
else:
    print("No suitable chip size found.")
