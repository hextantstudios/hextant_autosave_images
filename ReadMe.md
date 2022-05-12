# Blender Add-on: Autosave Images

A simple addon/plugin for Blender to automatically save new or modified images (textures) whenever the main Blender file is saved.

By default, Blender does *not* save newly created images -- including ones you may have spent quite a while working on using its texture painting tools. While it *will* prompt to save new or modified images when you exit, it does not save (even internally packed) images when saving the main `.blend` file. This behavior makes it easy to lose *all* one's texture painting work by a random crash or by ignoring the prompt when exiting by thinking that it has been previously saved.

I'm unclear why the Blender developers have not implemented this basic functionality even as an option. It's clear from the countless Blender tutorials that scream "Make *sure* you click *Image / Save* to save your texturing work!!!" that this is definitely a problem. 

Perhaps it's related to *[this bug](https://developer.blender.org/T95721)* which results in Blender forgetting the settings that were used to originally save an external image file. This can result in image files saved in some formats such as OpenEXR changing in size from 800kB to **64MB** because Blender resets its compression setting to *None*. (Note that images that are packed internally within the `.blend` file appear to compress well as do externally saved PNGs -- though not as well as manually setting the lossless compression level to 100%.)

While this is unfortunate, I would much rather *not* lose my work than waste a little disk space until this secondary issue is fixed! So after finding a great [suggestion on Stack Exchange](https://blender.stackexchange.com/a/15782), I thought I'd update it to save both external and internal images -- hopefully avoiding any loss of work.

## Installation

* Download the latest release from [here](https://github.com/hextantstudios/hextant_autosave_images/releases/download/latest/hextant_autosave_images.zip) or clone it using *git* to your custom Blender `...\scripts\addons\` folder.
* From Blender's Main Menu:
  * *Edit / Preferences*
  * Click the *Install* button and select the downloaded zip file.
  * Check the check-box next to the addon to activate it.

## Use

* Any time the currently edited file is saved, the images will also be saved. 
* New images that have not been manually saved to an external file will be packed into the `.blend` file. These can be saved later to an external file from the Image Editor window's menu: *Image / Save As*

## Known Issues

* The only known issue is the side effect from *[this bug](https://developer.blender.org/T95721)* which results in Blender forgetting the settings that were to originally save an external image file. Hopefully this will be fixed soon as it certainly impacts those using version control for their projects.

## License

This work is licensed under [GNU General Public License Version 3](https://download.blender.org/release/GPL3-license.txt).
