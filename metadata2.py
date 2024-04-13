import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import exifread

def extract_metadata(image_path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
                latitude = tags['GPS GPSLatitude']
                longitude = tags['GPS GPSLongitude']
                print("Latitude String:", latitude)
                print("Longitude String:", longitude)
                lat_ref = tags['GPS GPSLatitudeRef']
                lon_ref = tags['GPS GPSLongitudeRef']
                lat = float(str(latitude).replace(" ", "").replace("/", "").split(",")[0])
                lon = float(str(longitude).replace(" ", "").replace("/", "").split(",")[0])
                if str(lat_ref) == 'S':
                    lat = -lat
                if str(lon_ref) == 'W':
                    lon = -lon
                return {
                    'latitude': lat,
                    'longitude': lon,
                    'metadata': tags
                }
            else:
                return {'error': 'No GPS information found in the metadata.'}
    except Exception as e:
        return {'error': str(e)}

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png; *.gif")])
    if file_path:
        metadata = extract_metadata(file_path)
        if 'error' in metadata:
            lbl_info.config(text="Error: " + metadata['error'])
        else:
            lbl_info.config(text="Latitude: {}\nLongitude: {}".format(metadata['latitude'], metadata['longitude']))
            img = Image.open(file_path)
            img.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(img)
            lbl_image.config(image=photo)
            lbl_image.image = photo

# Create Tkinter window
root = tk.Tk()
root.title("Image Metadata Viewer")

# Create widgets
btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=10)

lbl_image = tk.Label(root)
lbl_image.pack()

lbl_info = tk.Label(root, text="")
lbl_info.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()