# Batch-Compression

This was born out of a need to create different size versions of large images being used on my photography website. Some DSLR images can be 4MB, 5MB or sometimes even 6MB or larger in size, which is in no world a sensible size for an image on a website to be.

This small Python script (which is simply a custom wrapper around the [ImageMagick](https://github.com/ImageMagick/ImageMagick) binaries) allows me to create:

  * Renamed full resolution and file size versions of the image
  * Renamed reduced resolution and reduced file size version of the image

The former is available for download, or for viewing, but the latter smaller image is the one displayed on the site by default, saving the end user from having to download lots of full resolution DSLR images.


# Installation on Linux systems
  * Make sure script is executable: `sudo chmod +x bc.py`
  * Move file to `/bin`: `sudo mv bc.py /bin`

# Usage
The command is in the format `bc.py <path to folder>`.

For example, `bc.py /home/reece/Pictures/uploads` would compress and rename all pictures in the `/uploads` folder.
