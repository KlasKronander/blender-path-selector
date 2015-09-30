
# Add-on for extracting path data from blender
Blender is a fantastic machine with incredible mesh object navigation, selection and editing properties. This is an add-on for Blender which allows to export select information from blender models.

## Setup
Open Blender, navigato to file->user preferences and click the add-ons tab. Click the button to install a new addon, and select the path_selector.py file in the dialog that appears.

This will copy the add-on to the relevant place. For development, it is a good idea to locate this copied file and replace it with a link to the file in the repo, so that you dont have to reinstall the add-on every time you changed it.

## Usage
Load the model from which you want to select vertices. First, we will define the frame of reference in which we would like to have our vertices described.
### Origin selection
1. Select the object (right or left-click, depending on your system setup), and press tab to enter object edit mode.
2. Make sure vertex-select is selected (hover over the symbols in the icon bar below the 3d window)
3. Right or left click (depending on your system) on the vertex that you want to use as a reference frame.
4. Once the SINGLE vertex is selected, navigate to mesh -> snap -> cursor-to-selected. This moves the crosshair to the selected vertex.
5. press tab to leave object edit mode.
6. press spacebar and type "Set origin"
6. select "origin to 3d cursor"
7. you should now see that the origin has moved to the desired location.


*** Vertex selection
Now that we have selected our desired frame of reference, let's select a few vertices as a simple path description.

1. Select the object (right or left-click, depending on your system setup), and press tab to enter object edit mode.
2. Make sure vertex-select is selected (hover over the symbols in the icon bar below the 3d window)
3. Select the vertices you like by clicking on them. You can also use the circle or box select tools by pressing c or b on the keyboard.
4. When you have fininshed your selection, press spacebar to bring up the searchable function browser. Type "Select path" and press enter.
5. A dialog will appear that allows you to enter an IP address and port. Once you press "OK", a udp package containing the selection information as a python dictionary will be sent to the provided IP port. 