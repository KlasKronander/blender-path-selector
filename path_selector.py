# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



bl_info = {
    "name": "Path selector",
    "category": "Object",
}

import bpy
import bmesh
import socket
import json


class PathSelector(bpy.types.Operator):
    # blender will use this as a tooltip for menu items and buttons.
    """My Object Moving Script"""
    # unique identifier for buttons and menu items to reference.
    bl_idname = "object.path_selector"
    # display name in the interface.
    bl_label = "Select path"
    # bl_options = {'REGISTER', 'REDO'}  # enable undo for the operator
    IP = bpy.props.StringProperty(name="Path server IP", default="localhost")
    port = bpy.props.IntProperty(name="port", default=5005)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    # execute() is called by blender when running the operator.
    def execute(self, context):
        # create connection
        socket_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # socket_connection.sendto(bytes(context.active_object.name,'utf-8'),addr)
        mess = "number of vertices: "+str(len(context.active_object.data.vertices))
        # socket_connection.sendto(bytes(mess,'utf-8'),addr)
        sel_vert = []
        if context.active_object.mode == "EDIT":
            blender_mesh = bmesh.from_edit_mesh(context.active_object.data)
            for v in blender_mesh.verts:
                if v.select is True:
                    sel_vert.append(v)
        else:
            blender_mesh = context.active_object.data
            for v in blender_mesh.vertices:
                if v.select is True:
                    sel_vert.append(v)

        # extract coordinate data from all vertices
        all_vert = context.active_object.data.vertices
        vertex_coordinates = [[v.co.x, v.co.y, v.co.z] for v in all_vert]
        vertex_normals = [[v.normal.x, v.normal.y, v.normal.z] for v in all_vert]

        # extract selected edges
        selected_edges = []
        if context.active_object.mode == "EDIT":
            # the syntax is a little different depending on if we are in EDIT mode or not
            blender_mesh = bmesh.from_edit_mesh(context.active_object.data)
            for v in blender_mesh.edges:
                if v.select is True:
                    selected_edges.append(v)
                    edges = [(e.verts[0].index, e.verts[1].index) for e in selected_edges]
        else:
            # if we are not in edit mode things are a bit easier
            blender_mesh = context.active_object.data
            for v in blender_mesh.edges:
                if v.select is True:
                    selected_edges.append(v)
                    edges = [(e.vertices[0], e.vertices[1]) for e in selected_edges]

        # extract vertex index data from selected edges

        mess = {'edges': edges, 'vert_loc': vertex_coordinates, 'vert_norm': vertex_normals}
        mess = json.dumps(mess)
        addr = (self.IP, self.port)
        socket_connection.sendto(bytes(mess, "utf-8"), addr)
        self.report({'INFO'}, "sent message to: "+self.IP+" port: "+str(self.port))
        # this lets blender know the operator finished successfully.
        return {'FINISHED'}


def register():
    bpy.utils.register_class(PathSelector)


def unregister():
    bpy.utils.unregister_class(PathSelector)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
