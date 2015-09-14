bl_info = {
    "name": "Path selector",
    "category": "Object",
}

import bpy
import socket

IP = 'localhost'
port = 5005
addr = (IP,port)


class PathSelector(bpy.types.Operator):
    """My Object Moving Script"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.path_selector"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select path"         # display name in the interface.
    #bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator#.


    def execute(self, context):        # execute() is called by blender when running the operator.
        
        # The original script
        scene = context.scene
        # create connection
        socket_connection =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("running klas aweseoma add-on")
        for obj in scene.objects:
            socket_connection.sendto(bytes(obj.name,'utf-8'),addr)

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(PathSelector)


def unregister():
    bpy.utils.unregister_class(PathSelector)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
