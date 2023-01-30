import bpy

nb_barres = 20
meter = "Meter."
for i in range(1, nb_barres):

    #    if i<10:
    #        meter = "Meter" + ".00"
    #    elif i>=10:
    #        meter = "Meter" + ".0"

    bpy.data.objects[meter + str(i)].select_set(True)
    bpy.data.scenes['Scene'].frame_set(0)
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
                                                                 "snap_target": 'CLOSEST', "snap_point": (0, 0, 0),
                                                                 "snap_align": False, "snap_normal": (0, 0, 0),
                                                                 "gpencil_strokes": False, "cursor_transform": False,
                                                                 "texture_space": False, "remove_on_cancel": False,
                                                                 "view2d_edge_pan": False, "release_confirm": False,
                                                                 "use_accurate": False,
                                                                 "use_automerge_and_split": False})
    for obj in bpy.context.selected_objects:
        obj.name = meter + str(i + 1)

    #    if i+1>=10:
    #        meter = "Meter" + ".0"

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[meter + str(i + 1)].select_set(True)

    bpy.context.object.modifiers["Hook-Empty"].object = bpy.data.objects["Aspect"]

    ob = bpy.context.active_object
    ob.data.materials[0] = bpy.data.materials.get("Meter material Full.001")
#    nodes = bpy.data.materials.get("Meter material Full.001").node_tree.nodes
#    node = nodes['Value.002']
#    bpy.data.materials["Meter material Full.001"].node_tree.nodes["Value.002"].outputs[0].value = bpy.ops.graph.sound_bake(filepath="G:\\Perso\\Musiques\\Hades - In the Blood (ft. Ashley Barrett).mp3", low=20, high=20000)


#    for node in nodes:
#        node.select = False
#    node.select = True
#    nodes.active = node


#    bpy.ops.graph.sound_bake(filepath="G:\\Perso\\Musiques\\Hades - In the Blood (ft. Ashley Barrett).mp3", low=20, high=20000)

# bpy.ops.object.select_all(action='DESELECT')
# bpy.data.objects["Meter.001"].select_set(True)
# obj.hide_set(state)


