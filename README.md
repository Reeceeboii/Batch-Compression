# Batch-Compression

This was born out of a need to create different size versions of large images being used on my photography website. Some DSLR images can be 4MB, 5MB or sometimes even 6MB or larger in size, which is in no world a sensible size for an image on a website to be.

This small Python script (which is simply a custom wrapper around the [ImageMagick](https://github.com/ImageMagick/ImageMagick) binaries) allows me to create renamed and reduced file size version of each image in a particular destination.

Images can often be reduced in their size by a significant amount. The script both shrinks and compresses.
As an example, a 4.29mb JPG can come out the other end at 62.9kb. A huge reduction is storage requirements and network load
and you get an image perfect to place on to a website.

On my photography site, the original size images are available for download, or for viewing, but the smaller images are the ones displayed on the site by default, saving the end user from having to download lots of full resolution DSLR images.

# Prerequisites
  The ImageMagick binaries should be installed on your system and accessible via the terminal (i.e. make sure they're globally executable else this script won't function). If ImageMagick is not installed, look up a tutorial for your particular OS.

  You also need Python 3. MacOS comes bundled with this, but for Linux & Windows you may need to do this yourself.


# Installation on Linux systems
      * Run install.sh with sudo privileges.
  * Make sure script is executable: `~$ sudo chmod +x bc.py`
  * Move file to `/bin`: `~$ sudo mv bc.py /bin`
    * or `~$ sudo cp bc.py /bin` if you want to keep another copy from the source

# Use on Windows (via WSL)
Make sure Python is installed. Then, using WSL, install imagemagick: `sudo apt-get install imagemagick`. Clone the repo into a
destination of your choosing and either use `~$ sudo chmod +x ./src/bc.py && install.sh` to install, or just execute the script directly.
As WSL provides Windows filesystem access, everything should just work no matter where the images are residing on your system (inside or outside of WSL's filesystem).


# Usage
The command is in the format `~$ bc.py <path to folder> <compression percentage>`.

Note that providing a compression percentage is optional, the default argument if nothing is provided is 50%.

For example, `~$ bc.py /home/reece/Pictures/uploads` would compress (**default quality 50%**) and rename all pictures in the `/uploads` folder.

... `~$ bc.py /home/reece/Pictures/uploads 25` would compress (**quality 25%**) and rename all pictures in the `/uploads` folder.


NOTE: if the file path contains any spaces, wrap it in quotes, i.e. the file path `/home/reece/Pictures/my uploads` would need to be passed as an argument like this: `~$ bc.py "/home/reece/Pictures/my uploads"`

## A much easier option is to open the terminal in the destination folder, and then just use the current working directory as the argument, this would then simply become `~$ bc.py .`

### Also, the '`-compressed`' string being appended to the file names is hardcoded since that's the way I needed the script laid out originally. This can very easily be changed though if something else is needed for your use case.

# Output
Running this script doubles the number of images in the folder. Each file has its name changed from its original to a new
UUID4 value (this is due to me needing the images to be unique amongst many other potentially conflicting file names in an S3 bucket).
There is a renamed full size original, and then a renamed compressed version with `-compressed` appended to the end such that there is an easy programmatic way of working out which images are which.

# Example

#### Pre execution

```
└───|/cat-pictures
│   └── image1.jpg
│   └── image2.jpg
│   └── image3.jpg
│   └── image4.jpg
```

#### Post execution
```
└───|/cat-pictures
│   └── _00c456d5-15fb-4ec8-ae89-9c5d0052ac98.jpg
│   └── _00c456d5-15fb-4ec8-ae89-9c5d0052ac98-compressed.jpg
│   └── _0afeec17-b19b-4a56-a3a0-9e4c2e2f1f0e.jpg
│   └── _0afeec17-b19b-4a56-a3a0-9e4c2e2f1f0e-compressed.jpg
│   └── _9b4d309e-8cb1-448a-abc1-68c425feb5bc.jpg
│   └── _9b4d309e-8cb1-448a-abc1-68c425feb5bc-compressed.jpg
│   └── _81b52e96-6858-452f-a0ea-ea4b20e550f6.jpg
│   └── _81b52e96-6858-452f-a0ea-ea4b20e550f6-compressed.jpg
```


![Terminal example](res/terminal-example.png)
