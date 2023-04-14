import bpy
import os

file_path = os.path.join(os.path.dirname(bpy.data.filepath), "Build_a_Castle.mp3")
original_type = bpy.context.area.type
nb_barres = 20
bar_spacing_x = 1.1
bpy.data.scenes['Scene'].frame_set(0)
tempLoaction = (0, 0, 1)
zLocation = bpy.data.objects["Aspect"].location.z
bpy.data.objects["Aspect"].location = tempLoaction
for i in range(1, nb_barres):

    # bpy.data.objects["Meter." + str(i)].select_set(True)
    bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked": True, "mode": 'TRANSLATION'},
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
                                                                 "snap_elements": {'INCREMENT'},
                                                                 "use_snap_project": False, "snap_target": 'CLOSEST',
                                                                 "use_snap_self": True, "use_snap_edit": True,
                                                                 "use_snap_nonedit": True, "use_snap_selectable": False,
                                                                 "snap_point": (0, 0, 0), "snap_align": False,
                                                                 "snap_normal": (0, 0, 0), "gpencil_strokes": False,
                                                                 "cursor_transform": False, "texture_space": False,
                                                                 "remove_on_cancel": False, "view2d_edge_pan": False,
                                                                 "release_confirm": False, "use_accurate": False,
                                                                 "use_automerge_and_split": False})
    bpy.ops.object.make_single_user(object=True, obdata=True, material=True, animation=False, obdata_animation=False)

    for obj in bpy.context.selected_objects:
        obj.name = "Meter." + str(i + 1)

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["Meter." + str(i + 1)].select_set(True)

    bpy.context.object.modifiers["Hook-Empty"].object = bpy.data.objects["Aspect"]

    # TO DO copy materials into objects and link the sound as f-curve

    ob = bpy.context.active_object

    ob.data.materials[0] = bpy.data.materials.get("Meter material Full.001").copy()
    ob.data.materials[0].name = ("Meter material Full." + str(i + 1))
    bpy.context.area.type = "GRAPH_EDITOR"

    bpy.data.materials["Meter material Full." + str(i + 1)].node_tree.nodes["Value.002"].outputs[0].keyframe_insert(
        data_path='default_value', frame=1)

    bpy.ops.graph.sound_bake(filepath=file_path, low=100*i, high=100*(i+1), attack=0.2)

bpy.data.objects["Aspect"].location.z = zLocation
bpy.context.area.type = original_type
