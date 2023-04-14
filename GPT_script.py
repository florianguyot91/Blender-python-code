import bpy

# Set up scene and objects
scene = bpy.context.scene
objs = [bpy.data.objects["Meter.1"]]  # Replace with your own object names
num_objs = len(objs)

# Set up sound properties
sound_path = "/path/to/audio/file.mp3"
bpy.ops.sound.open(filepath=sound_path)
sound = bpy.data.sounds[-1]

# Bake sound to f-curves
bpy.ops.graph.sound_bake('INVOKE_DEFAULT', sound=sound.name, frame_start=scene.frame_start, frame_end=scene.frame_end,
                         visual_keying=True, snap=False, use_cyclic=False, bake_types={'FCURVES'}, buffer_factor=1.2,
                         update_scene_stats=True, cursor_follow=False, cursor_select=False, bake_sound=True,
                         use_existing=True, use_all_actions=True, filter_blender=False, filter_backup=False,
                         filter_image=False, filter_movie=False, filter_python=False, filter_font=False,
                         filter_text=False, filter_sound=True, filter_collada=False, filter_folder=True,
                         filter_btx=False, filter_id=True, filter_ani=False, filter_blenlib=False, filter_script=False,
                         filter_fcurve=False, filter_gpencil=False, sort_method='FILE_SORT_ALPHA',
                         context='AUDIO_SEQUENCE_EDITOR')

for i in range(num_objs):
    # Add new f-curve to each object and assign the appropriate frequency range
    fcurve = objs[i].animation_data.action.fcurves.new(data_path="scale", index=2)  # Z scale
    fcurve.sound = sound
    fcurve.sound_property = "FREQUENCY"
    fcurve.array_index = i / num_objs  # Assign frequency range based on object index

# Add graph editor window and switch to f-curve mode
bpy.context.area.type = "GRAPH_EDITOR"
bpy.context.space_data.graph_editor.show_only_selected = False
bpy.ops.graph.sound_bake_channels(mode='SOUND')

# Set graph editor view to show full frequency range
for area in bpy.context.screen.areas:
    if area.type == "GRAPH_EDITOR":
        region = area.regions[-1]
        region.view2d.min_y = 0
        region.view2d.max_y = 1

# Done!
