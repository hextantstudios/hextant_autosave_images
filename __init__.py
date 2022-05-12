# Copyright 2022 by Hextant Studios. https://HextantStudios.com
# This work is licensed under GNU General Public License Version 3.
# License: https://download.blender.org/release/GPL3-license.txt

bl_info = {
    "name": "Auto Save Images",
    "author": "Hextant Studios",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "",
    "description": "Saves all modified images when saving the Blender file.",
    "doc_url": "https://github.com/hextantstudios/hextant_autosave_images",
    "category": "System"
}

import bpy
from bpy.app.handlers import persistent, save_pre

# Saves any modified external images and pack others.
@persistent
def save_modified_images(_):    
    for image in bpy.data.images:
        if image.is_dirty:            
            bpy.ops.image.save_all_modified()
            return

def register():
    if save_modified_images not in save_pre:
        save_pre.append(save_modified_images)

def unregister():
    if save_modified_images in save_pre:
        save_pre.remove(save_modified_images)
