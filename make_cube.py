import bpy
import os

# Clear the scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# 1. Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
cube = bpy.context.active_object

# 2. Enter Edit Mode
bpy.ops.object.mode_set(mode='EDIT')

# 3. Apply Bevel to vertices (corners)
# offset: how much to cut
# segments: 1 for flat chamfer, >1 for rounded
# affect: 'VERTICES' specifically to "remove corners"
bpy.ops.mesh.bevel(
    offset=0.4, 
    segments=6, 
    affect='VERTICES', 
    offset_type='OFFSET'
)

# 4. Return to Object Mode
bpy.ops.object.mode_set(mode='OBJECT')

# 5. Save the project
# We'll save it as 'beveled_cube_project.blend'
filepath = os.path.join(os.getcwd(), "beveled_cube_project.blend")
bpy.ops.wm.save_as_mainfile(filepath=filepath)

print(f"Successfully created and saved: {filepath}")
