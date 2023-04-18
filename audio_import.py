import bpy

# Set the filepath to the audio file
audio_filepath = ".\Blender-python-code\Post Malone, Swae Lee - Sunflower (Spider-Man_ Into the Spider-Verse).mp3"
audio_name = "Build_a_Castle.mp3"

# Switch to the VSE workspace
bpy.context.area.ui_type = 'SEQUENCE_EDITOR'

# Add a new audio strip to the VSE
bpy.ops.sequencer.sound_strip_add(
    filepath="//" + audio_name,
    directory="Blender-python-code\\",
    files=[{
        "name": audio_name,
        "name": audio_name}],
    relative_path=True, frame_start=0, channel=1)

# Get the audio strip from the VSE
audio_strip = bpy.data.scenes["Scene"].sequence_editor.sequences_all[
    audio_name]

# Set the end frame of the audio strip
audio_strip.frame_final_end = int(audio_strip.frame_start + audio_strip.frame_final_duration)

# Set the scene end frame to match the end of the audio strip
bpy.context.scene.frame_end = audio_strip.frame_final_end
bpy.context.area.ui_type = 'TEXT_EDITOR'
