import cv2

def resize_image(input_path, output_path, width=None, height=None):
    """
    Resizes an image to the given width and/or height while maintaining aspect ratio.

    Parameters:
        input_path (str): Path to the input image.
        output_path (str): Path to save the resized image.
        width (int): Desired width. Default is None.
        height (int): Desired height. Default is None.
    """
    # Load the image
    image = cv2.imread(input_path)

    if image is None:
        print(f"Error: Unable to load image from {input_path}")
        return

    # Get original dimensions
    (orig_height, orig_width) = image.shape[:2]

    # Check if width or height is specified
    if width is None and height is None:
        print("Error: Both width and height cannot be None.")
        return

    # Calculate new dimensions while maintaining aspect ratio
    if width is not None:
        aspect_ratio = width / float(orig_width)
        new_dimensions = (width, int(orig_height * aspect_ratio))
    else:
        aspect_ratio = height / float(orig_height)
        new_dimensions = (int(orig_width * aspect_ratio), height)

    # Resize the image
    resized_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_AREA)

    # Save the resized image
    cv2.imwrite(output_path, resized_image)
    print(f"Resized image saved to {output_path}")

# Example usage
# conda activate CICFINAL
input_image_path = "./images/inha.png"  # Replace with your input image path
output_image_path = "./images/inha_small.jpg"  # Replace with your desired output image path
resize_image(input_image_path, output_image_path, width=800)
