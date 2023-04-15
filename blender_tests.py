import bpy

bpy.data.materials["Meter material Full.001"].node_tree.nodes["Value.002"].outputs[0].keyframe_insert(
    data_path='default_value', frame=1)

bpy.data.materials["Meter material Full.001"].node_tree.nodes["Value.002"].outputs[0].keyframe_delete(
    data_path='default_value', frame=1)
