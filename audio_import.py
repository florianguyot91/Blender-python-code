import bpy
bpy.ops.sequencer.delete()

# Set the filepath to the audio file
audio_name = "Rammstein - Waidmanns Heil (Official Lyric Video).mp3"
audio_filepath = ".\Blender-python-code\Musics" + "\" + " + audio_name

# Switch to the VSE workspace
bpy.context.area.ui_type = 'SEQUENCE_EDITOR'

# Add a new audio strip to the VSE
bpy.ops.sequencer.sound_strip_add(
    filepath="//Musics\\"+audio_name,
    directory="Blender-python-code\\Musics\\", files=[
        {"name": audio_name,
         "name": audio_name}], relative_path=True,
    frame_start=1, channel=1)

# Get the audio strip from the VSE
audio_strip = bpy.data.scenes["Scene"].sequence_editor.sequences_all[
    audio_name]

# Set the end frame of the audio strip
audio_strip.frame_final_end = int(audio_strip.frame_start + audio_strip.frame_final_duration)

# Set the scene end frame to match the end of the audio strip
bpy.context.scene.frame_end = audio_strip.frame_final_end
bpy.context.area.ui_type = 'TEXT_EDITOR'
