bl_info = {
    "name": "Path selector",
    "category": "Object",
}

import bpy
import bmesh
import socket
import json

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
        #socket_connection.sendto(bytes(context.active_object.name,'utf-8'),addr)
        mess = "number of vertices: "+str(len(context.active_object.data.vertices))
        #socket_connection.sendto(bytes(mess,'utf-8'),addr)
        sel_vert = []
        if context.active_object.mode == "EDIT":
            blender_mesh = bmesh.from_edit_mesh(context.active_object.data)
            for v in blender_mesh.verts:
                if v.select == True:
                    sel_vert.append(v)
        else:
            blender_mesh = context.active_object.data
            for v in blender_mesh.vertices:
                if v.select == True:
                    sel_vert.append(v)

        # extract coordinate data from all vertices
        all_vert = context.active_object.data.vertices
        vertex_coordinates = [ [v.co.x,v.co.y,v.co.z] for v in all_vert]
        vertex_normals = [[v.normal.x,v.normal.y,v.normal.z] for v in all_vert]

        # extract selected edges 
        selected_edges = []
        if context.active_object.mode == "EDIT":
            blender_mesh = bmesh.from_edit_mesh(context.active_object.data)
            for v in blender_mesh.edges:
                if v.select == True:
                    selected_edges.append(v)
        else:
            blender_mesh = context.active_object.data
            for v in blender_mesh.edges:
                if v.select == True:
                    selected_edges.append(v)

        # extract vertex index data from selected edges
        edges = [(e.vertices[0],e.vertices[1]) for e in selected_edges]
        mess = {'edges':edges, 'vert_loc':vertex_coordinates, 'vert_norm':vertex_normals}
        mess = json.dumps(mess)
        socket_connection.sendto(bytes(mess,'utf-8'),addr)
        
        return {'FINISHED'}            # this lets blender know the operator finished successfully.



def register():
    bpy.utils.register_class(PathSelector)


def unregister():
    bpy.utils.unregister_class(PathSelector)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
