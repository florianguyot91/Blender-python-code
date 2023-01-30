import bpy

nb_barres = 20
meter = "Meter."
bpy.data.scenes['Scene'].frame_set(0)
tempLoaction = (0, 0, 1)
bpy.data.objects["Aspect"].location = tempLoaction
for i in range(1, nb_barres):

    bpy.data.objects[meter + str(i)].select_set(True)
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
    bpy.ops.object.make_single_user(object=True, obdata=True, material=True, animation=False, obdata_animation=False)

    for obj in bpy.context.selected_objects:
        obj.name = meter + str(i + 1)

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[meter + str(i + 1)].select_set(True)

    bpy.context.object.modifiers["Hook-Empty"].object = bpy.data.objects["Aspect"]

    ob = bpy.context.active_object
    ob.data.materials[0] = bpy.data.materials.get("Meter material Full.001")

    nodes = bpy.data.materials.get("Meter material Full.001").node_tree.nodes
    node = nodes['Value.002']

    #    mat = bpy.data.materials.get("Meter material Full.001")

    #    mat.node_tree.nodes["Music"].inputs[0].default_value = 0.5

    nodes.node.outputs[0].value = bpy.ops.graph.sound_bake(filepath="C:\\Users\\axelf\\PycharmProjects\\Blender-python-code\\Build a Castle.mp3", low=20, high=20000, attack=0.2)


#    bpy.data.materials["Meter material Full.001"].node_tree.nodes["Value.002"].outputs[0].value = bpy.ops.graph.sound_bake(filepath="G:\\Perso\\Musiques\\Hades - In the Blood (ft. Ashley Barrett).mp3", low=20, high=20000)


#    for node in nodes:
#        node.select = False
#    node.select = True
#    nodes.active = node


#    bpy.ops.graph.sound_bake(filepath="G:\\Perso\\Musiques\\Hades - In the Blood (ft. Ashley Barrett).mp3", low=20, high=20000)

bpy.data.objects["Aspect"].location = (0, 0, 0.25)

# bpy.ops.object.select_all(action='DESELECT')
# bpy.data.objects["Meter.1"].select_set(True)
# obj.hide_set(state)


