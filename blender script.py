import math
import bpy
import os

file_path = os.path.join(os.path.dirname(bpy.data.filepath),
                         "Musics/Rhapsody - The Magic of the Wizards Dream.mp3")
original_type = bpy.context.area.type
nb_barres = 20
bar_spacing_x = 1.1
meter = "Meter."
bpy.data.scenes['Scene'].frame_set(1)
tempLocation = (0, 0, 1)
zLocation = bpy.data.objects["Aspect"].location.z
bpy.data.objects["Aspect"].location = tempLocation
min_frequency = 20
max_frequency = 20000

bpy.ops.outliner.orphans_purge(do_recursive=True)



context = bpy.context

for area in context.screen.areas:
    if area != context.area:
        break

override = {'region': area.regions[0]}

for i in range(1, nb_barres):

    loga_frequency_min = math.pow(10, (((math.log10(max_frequency - min_frequency)) / nb_barres) * i)) + min_frequency
    loga_frequency_max = math.pow(10,
                                  (((math.log10(max_frequency - min_frequency)) / nb_barres) * (i + 1))) + min_frequency

    bpy.data.objects[meter + str(i)].select_set(True)
    context.area.type = 'VIEW_3D'
    bpy.ops.object.duplicate_move_linked(override, OBJECT_OT_duplicate={"linked": True, "mode": 'TRANSLATION'},
                                         TRANSFORM_OT_translate={"value": (1.1, 0, 0), "orient_axis_ortho": 'X',
                                                                 "orient_type": 'GLOBAL',
                                                                 "orient_matrix": ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                                                                 "orient_matrix_type": 'GLOBAL',
                                                                 "constraint_axis": (True, False, False),
                                                                 "mirror": False, "use_proportional_edit": False,
                                                                 "proportional_edit_falloff": 'SMOOTH',
                                                                 "proportional_size": 1,
                                                                 "use_proportional_connected": False,
                                                                 "use_proportional_projected": False, "snap": False,
                                                                 "snap_target": 'CLOSEST', "snap_point": (0, 0, 0),
                                                                 "snap_align": False, "snap_normal": (0, 0, 0),
                                                                 "gpencil_strokes": False, "cursor_transform": False,
                                                                 "texture_space": False, "remove_on_cancel": False,
                                                                 "view2d_edge_pan": False, "release_confirm": False,
                                                                 "use_accurate": False,
                                                                 "use_automerge_and_split": False})
    bpy.ops.object.make_single_user(object=True, obdata=True, material=True, animation=False, obdata_animation=False)

    for obj in bpy.context.selected_objects:
        obj.name = meter + str(i + 1)

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[meter + str(i + 1)].select_set(True)

    bpy.context.object.modifiers["Hook-Empty"].object = bpy.data.objects["Aspect"]

    ob = bpy.context.active_object

    ob.data.materials[0] = bpy.data.materials.get("Meter material Full.001").copy()
    ob.data.materials[0].name = ("Meter material Full." + str(i + 1))
    bpy.context.area.type = "NODE_EDITOR"

    bpy.data.materials["Meter material Full." + str(i + 1)].node_tree.nodes["Value.002"].outputs[0].keyframe_insert(
        data_path='default_value', frame=1)
    bpy.context.area.type = "GRAPH_EDITOR"

    bpy.ops.graph.sound_bake(filepath=file_path, low=loga_frequency_min, high=loga_frequency_max, attack=0.2)

bpy.data.objects[meter + str(1)].select_set(True)

bpy.context.area.type = "NODE_EDITOR"

bpy.data.materials["Meter material Full.001"].node_tree.nodes["Value.002"].outputs[0].keyframe_insert(
    data_path='default_value', frame=1)
bpy.context.area.type = "GRAPH_EDITOR"

loga_frequency_first_bar = math.pow(10, (((math.log10(max_frequency - min_frequency)) / nb_barres) * 1)) + min_frequency

bpy.ops.graph.sound_bake(filepath=file_path, low=20, high=loga_frequency_first_bar, attack=0.2)

bpy.data.objects["Aspect"].location.z = zLocation
bpy.context.area.type = original_type
