import bpy

# Set the filepath to the audio file
audio_filepath = "G:\Perso\Documents\Blender_projects\Tests\Blender-python-code\Build_a_Castle.mp3"

# Switch to the VSE workspace
bpy.context.area.ui_type = 'SEQUENCE_EDITOR'

# Add a new audio strip to the VSE
bpy.ops.sequencer.sound_strip_add(filepath=audio_filepath, frame_start=1, channel=1)

# Get the audio strip from the VSE
audio_strip = bpy.data.scenes["Scene"].sequence_editor.sequences_all["Build_a_Castle.mp3"]

# Set the end frame of the audio strip
audio_strip.frame_final_end = int(audio_strip.frame_start + audio_strip.frame_final_duration)

# Set the scene end frame to match the end of the audio strip
bpy.context.scene.frame_end = audio_strip.frame_final_end
