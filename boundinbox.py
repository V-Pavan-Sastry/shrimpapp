import cv2

# Function to draw the rectangle and label on the image
def draw_rectangle(image_path, xmin, xmax, ymin, ymax, label, label_font_size,i):
    if(i==0):
    # Load the image
        image = cv2.imread(image_path)
    else:
        image = cv2.imread("image_with_rectangle.jpg")


    # Convert the coordinates from float to integer
    xmin = int(xmin)
    xmax = int(xmax)
    ymin = int(ymin)
    ymax = int(ymax)

    # Draw the rectangle on the image
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 8)

    # Calculate the position for the label
    font = cv2.FONT_HERSHEY_TRIPLEX
    text_size = cv2.getTextSize(label, font, label_font_size, 2)
    text_x = xmin
    text_y = ymin - text_size[0][1]

    # Draw the background rectangle for the label
    cv2.rectangle(image, (text_x, text_y), (text_x + text_size[0][0], text_y + text_size[0][1]), (255, 255, 255), -1)

    # Write the label on the image
    cv2.putText(image, label, (text_x, text_y + text_size[0][1]), font, label_font_size, (0, 0, 255), 2)
    # Save the image
    cv2.imwrite('image_with_rectangle.jpg', image)

# Test the function
#draw_rectangle('C:/Users/pavan/Desktop/296.jpg', 100, 300, 200, 400, 'Label', 0.7)