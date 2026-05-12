import bpy
import sys

zip_path = "/home/rlins/Git/blender/mcp/addon/blender_mcp_addon.zip"
try:
    bpy.ops.preferences.addon_install(filepath=zip_path)
    bpy.ops.preferences.addon_enable(module="blender_mcp_addon")
    bpy.ops.wm.save_userpref()
    print("Successfully installed and enabled blender_mcp_addon.")
except Exception as e:
    print(f"Error installing addon: {e}", file=sys.stderr)
    sys.exit(1)
