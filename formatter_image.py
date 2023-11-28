from imutils.perspective import four_point_transform
import cv2
import numpy
def process_image(image_path):
    # Load image, grayscale, Gaussian blur, Otsu's threshold
    image = cv2.imread(image_path)  # Load the input image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur to the grayscale image
    #thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)[1]  # Apply Otsu's threshold to the blurred image
    #thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # Apply Otsu's threshold to the blurred image
    #thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1)
    # Find contours and sort for largest contour
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the thresholded image
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]  # Check OpenCV version to ensure compatibility
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)  # Sort the contours by area in descending order

    displayCnt = None

    for c in cnts:
        # Perform contour approximation
        peri = cv2.arcLength(c, True)  # Calculate the perimeter of the contour
        approx = cv2.approxPolyDP(c, 0.03 * peri, True)  # Approximate the contour with a simpler polygon
        if len(approx) == 4 and cv2.contourArea(approx) > 1000:  # If the polygon has 4 sides and area is greater than 1000
            displayCnt = approx  # Store the contour approximation
            break

    # Draw contour on the original image
    cv2.drawContours(image, [displayCnt], -1, (0, 255, 0), 3)

    # Obtain birds' eye view of image
    warped = four_point_transform(image, displayCnt.reshape(4, 2))  # Apply perspective transform to obtain birds' eye view

    # Display the images
    cv2.imwrite(image_path, warped)