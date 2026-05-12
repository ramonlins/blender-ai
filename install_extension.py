import bpy
import sys
import os

zip_path = "/home/rlins/Git/blender_mcp/addon/blender_mcp_addon.zip"

# For Blender 4.2+, we should use the extensions operator if it's an extension
try:
    # Try installing as extension first
    if hasattr(bpy.ops, "extensions"):
        print("Installing as Extension...")
        bpy.ops.extensions.package_install_file(filepath=zip_path)
    else:
        print("Extensions operator not found, falling back to legacy addon install...")
        bpy.ops.preferences.addon_install(filepath=zip_path)
    
    # The module name for enabling might be different if installed as extension
    # Extensions are usually prefixed or managed differently.
    # But let's try to enable it. 
    # In 4.2+, extensions are often auto-enabled or handled in the Extensions tab.
    
    bpy.ops.wm.save_userpref()
    print("Installation attempt finished.")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
