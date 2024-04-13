import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import exifread

def extract_metadata(image_path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            metadata = {
                'date_time': str(tags.get('EXIF DateTimeOriginal', 'N/A')),
                'camera_settings': str(tags.get('EXIF ExposureTime', 'N/A')),
                'camera_model': str(tags.get('Image Model', 'N/A')),
                'image_resolution': str(tags.get('EXIF ExifImageWidth', 'N/A')) + "x" + str(tags.get('EXIF ExifImageLength', 'N/A')),
                'gps_info': str(tags.get('GPSInfo', 'N/A')),
                'thumbnail': tags.get('JPEGThumbnail', None)
            }
            return metadata
    except Exception as e:
        return {'error': str(e)}

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png; *.gif")])
    if file_path:
        metadata = extract_metadata(file_path)
        if 'error' in metadata:
            output_date_time.delete(1.0, tk.END)
            output_camera_settings.delete(1.0, tk.END)
            output_camera_model.delete(1.0, tk.END)
            output_image_resolution.delete(1.0, tk.END)
            output_gps_location.delete(1.0, tk.END)
            output_date_time.insert(tk.END, "Error: " + metadata['error'])
            clear_metadata()
        else:
            output_date_time.delete(1.0, tk.END)
            output_camera_settings.delete(1.0, tk.END)
            output_camera_model.delete(1.0, tk.END)
            output_image_resolution.delete(1.0, tk.END)
            output_gps_location.delete(1.0, tk.END)
            output_date_time.insert(tk.END, metadata['date_time'])
            output_camera_settings.insert(tk.END, metadata['camera_settings'])
            output_camera_model.insert(tk.END, metadata['camera_model'])
            output_image_resolution.insert(tk.END, metadata['image_resolution'])
            output_gps_location.insert(tk.END, metadata['gps_info'])

            # Display thumbnail image if available
            thumbnail = metadata['thumbnail']
            if thumbnail:
                img = Image.open(file_path)
                img.thumbnail((300, 300))
                photo = ImageTk.PhotoImage(img)
                thumbnail_label.config(image=photo)
                thumbnail_label.image = photo
            else:
                thumbnail_label.config(image=None)

def clear_metadata():
    output_date_time.delete(1.0, tk.END)
    output_camera_settings.delete(1.0, tk.END)
    output_camera_model.delete(1.0, tk.END)
    output_image_resolution.delete(1.0, tk.END)
    output_gps_location.delete(1.0, tk.END)
    thumbnail_label.config(image=None)

# Create Tkinter window
root = tk.Tk()
root.title("Image Metadata Viewer")
root.geometry("600x600")
root.configure(bg='#E0E0E0')

# Create widgets
thumbnail_label = tk.Label(root, bg='white', bd=2, relief="solid")
thumbnail_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

output_date_time_label = tk.Label(root, text="Date and Time:", bg='#E0E0E0')
output_date_time_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)

output_date_time = tk.Text(root, height=2, width=50)
output_date_time.grid(row=1, column=1, sticky='w', padx=10, pady=5)

output_camera_settings_label = tk.Label(root, text="Camera Settings:", bg='#E0E0E0')
output_camera_settings_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)

output_camera_settings = tk.Text(root, height=2, width=50)
output_camera_settings.grid(row=2, column=1, sticky='w', padx=10, pady=5)

output_camera_model_label = tk.Label(root, text="Camera Model:", bg='#E0E0E0')
output_camera_model_label.grid(row=3, column=0, sticky='w', padx=10, pady=5)

output_camera_model = tk.Text(root, height=2, width=50)
output_camera_model.grid(row=3, column=1, sticky='w', padx=10, pady=5)

output_image_resolution_label = tk.Label(root, text="Image Resolution:", bg='#E0E0E0')
output_image_resolution_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)

output_image_resolution = tk.Text(root, height=2, width=50)
output_image_resolution.grid(row=4, column=1, sticky='w', padx=10, pady=5)

output_gps_location_label = tk.Label(root, text="GPS Location:", bg='#E0E0E0')
output_gps_location_label.grid(row=5, column=0, sticky='w', padx=10, pady=5)

output_gps_location = tk.Text(root, height=2, width=50)
output_gps_location.grid(row=5, column=1, sticky='w', padx=10, pady=5)

btn_open = tk.Button(root, text="Open Image", command=open_image, bg='#4CAF50', fg='white')
btn_open.grid(row=6, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()