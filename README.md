# metadata-extraction-tool
Metadata Extraction tool - This is a Tkinter-based GUI application written in Python that allows the user to open an image file and view its metadata, including date and time, camera settings, camera model, image resolution, and GPS location. I have used exif samples from a github repo. 

1. Libraries used: Tkinter for the GUI, The Pillow library (or PIL) is used for image processing tasks such as opening, manipulating, and saving many different image file formats, The Exifread library that allows you to read and extract metadata from image files.

2. Then we define the functions - 
•	extract_metadata(image_path): Opens the image file specified by image_path 
•	open_image(): Opens a file dialog to select an image file, extracts its metadata using extract_metadata(), and displays the metadata in the GUI.
•	clear_metadata(): Clears the displayed metadata in the GUI.

3. Create a Tkinter window - Creates a Tkinter window with the title "Image Metadata Viewer" and a size of 600x600 pixels.

4. Creating the widgets - 
•	thumbnail_label: Label widget to display a thumbnail image of the selected image. 
•	output_date_time, output_camera_settings, output_camera_model, output_image_resolution, output_gps_location: Text widget to display the corresponding metadata.
•	btn_open: Button widget to open the image file and display its metadata.

5. We use the grid() method to place the widgets in the window in a layout.

6. Lastly, run the loop to run the application.
