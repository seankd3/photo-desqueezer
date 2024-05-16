import os
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

# Create a Tkinter root window (hidden)
root = Tk()
root.withdraw()

# Open a file dialog to select DNG files
file_paths = askopenfilenames(filetypes=[("DNG Files", "*.dng")])

# Process each selected DNG file
for file_path in file_paths:
    # Read the DNG file
    image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

    # Stretch the image horizontally by 1.5x
    stretched_image = cv2.resize(image, None, fx=1.5, fy=1, interpolation=cv2.INTER_LINEAR)

    # Generate the output file path with the "-desqueezed" suffix
    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(directory, f"{name}-desqueezed{ext}")

    # Save the stretched image as a new DNG file
    cv2.imwrite(output_path, stretched_image)

print("Processing completed.")