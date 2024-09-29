import cv2

def cap_camera(): 
    # Load the image and convert to grayscale
    image = cv2.imread('captured_image.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # Threshold the image to create a binary image (Moon will appear white)
    _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours to find the largest one (likely the Moon)
    for contour in contours:
        # Get the area and filter out small objects
        area = cv2.contourArea(contour)
        if area > 500:  # Adjust this threshold based on your images
            # Get the bounding box (x, y) coordinates of the contour
            (x, y, w, h) = cv2.boundingRect(contour)
            
            # Draw a rectangle around the detected Moon
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Calculate the center of the Moon
            moon_center = (x + w//2, y + h//2)
            print(f"Moon center at: {moon_center}")
