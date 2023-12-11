import math
import bpy
import os


def delete_f_curves():
    bpy.context.area.type = "GRAPH_EDITOR"
    bpy.ops.anim.channels_delete()


def import_audio(file_path, chanel):
    bpy.ops.sequencer.delete()
    # Set the filepath to the audio file
    audio_name = os.path.basename(file_path)
    # Switch to the VSE workspace
    bpy.context.area.type = 'SEQUENCE_EDITOR'
    # Add a new audio strip to the VSE
    bpy.ops.sequencer.sound_strip_add(
        filepath=file_path,
        directory=os.path.dirname(file_path),
        files=[
            {
                "name": audio_name,
                "name": audio_name
            }
        ],
        relative_path=True,
        frame_start=1,
        channel=chanel)
    # Get the audio strip from the VSE
    audio_strip = bpy.data.scenes["Scene"].sequence_editor.sequences_all[os.path.basename(file_path[2:])]
    # Set the end frame of the audio strip
    audio_strip.frame_final_end = int(audio_strip.frame_start + audio_strip.frame_final_duration)
    # Set the scene end frame to match the end of the audio strip
    bpy.context.scene.frame_end = audio_strip.frame_final_end
    bpy.context.area.type = 'TEXT_EDITOR'


def audio_processing(file_path, bar_count, spacing, attack, release, min_freq, max_freq):
    print("File path : " + bpy.path.abspath(file_path))
    original_type = bpy.context.area.type
    bar_spacing_x = spacing
    meter = "Meter."
    bpy.data.scenes['Scene'].frame_set(1)
    tempLocation = (0, 0, 1)
    zLocation = bpy.data.objects["Aspect"].location.z
    bpy.data.objects["Aspect"].location = tempLocation
    min_frequency = min_freq
    max_frequency = max_freq
    context = bpy.context

    delete_f_curves()

    remove_previous_meters()

    for area in context.screen.areas:
        if area != context.area:
            break
    bpy.context.view_layer.objects.active = bpy.data.objects["Meter.1"]
    bpy.data.objects["Meter.1"].select_set(True)
    for i in range(1, bar_count):

        loga_frequency_min = math.pow(10,
                                      (((math.log10(max_frequency - min_frequency)) / bar_count) * i)) + min_frequency
        loga_frequency_max = math.pow(10,
                                      (((math.log10(max_frequency - min_frequency)) / bar_count) * (
                                              i + 1))) + min_frequency

        bpy.data.objects[meter + str(i)].select_set(True)

        context.area.type = 'VIEW_3D'
        print("Selected objects:", bpy.context.selected_objects)
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked": True, "mode": 'TRANSLATION'},
                                             TRANSFORM_OT_translate={"value": (bar_spacing_x, 0, 0),
                                                                     "orient_type": 'GLOBAL',
                                                                     "orient_matrix": ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                                                                     "orient_matrix_type": 'GLOBAL',
                                                                     "constraint_axis": (False, False, False),
                                                                     "mirror": False, "use_proportional_edit": False,
                                                                     "proportional_edit_falloff": 'SMOOTH',
                                                                     "proportional_size": 1,
                                                                     "use_proportional_connected": False,
                                                                     "use_proportional_projected": False, "snap": False,
                                                                     "snap_elements": {'INCREMENT'},
                                                                     "use_snap_project": False,
                                                                     "snap_target": 'CLOSEST', "use_snap_self": True,
                                                                     "use_snap_edit": True, "use_snap_nonedit": True,
                                                                     "use_snap_selectable": False,
                                                                     "snap_point": (0, 0, 0), "snap_align": False,
                                                                     "snap_normal": (0, 0, 0), "gpencil_strokes": False,
                                                                     "cursor_transform": False, "texture_space": False,
                                                                     "remove_on_cancel": False,
                                                                     "use_duplicated_keyframes": False,
                                                                     "view2d_edge_pan": False, "release_confirm": False,
                                                                     "use_accurate": False, "alt_navigation": True,
                                                                     "use_automerge_and_split": False})

        print("End of duplicate_move_linked !")

        bpy.ops.object.make_single_user(object=True,
                                        obdata=True,
                                        material=True,
                                        animation=False,
                                        obdata_animation=False
                                        )
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

        bpy.ops.graph.sound_to_samples(filepath=file_path, low=loga_frequency_min, high=loga_frequency_max,
                                       attack=attack,
                                       release=release)
        print("Hello from the end of for !")

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[meter + str(1)].select_set(True)
    bpy.context.area.type = "NODE_EDITOR"
    bpy.data.materials["Meter material Full.001"].node_tree.nodes["Value.002"].outputs[0].keyframe_insert(
        data_path='default_value', frame=1)
    bpy.context.area.type = "GRAPH_EDITOR"
    loga_frequency_first_bar = math.pow(10,
                                        (((math.log10(max_frequency - min_frequency)) / bar_count) * 1)) + min_frequency
    bpy.ops.graph.sound_to_samples(filepath=file_path, low=20, high=loga_frequency_first_bar, attack=attack,
                                   release=release)
    bpy.data.objects["Aspect"].location.z = zLocation
    bpy.context.area.type = original_type
    bpy.context.area.ui_type = 'PROPERTIES'
    print("Hello from the end of bars !")


def remove_previous_meters():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["Aspect"].select_set(True)
    bpy.data.objects["Height"].select_set(True)
    bpy.data.objects["Spacing"].select_set(True)
    bpy.data.objects["Camera"].select_set(True)
    bpy.data.objects["Intensity"].select_set(True)
    bpy.data.objects["Meter.1"].select_set(True)
    bpy.ops.object.select_all(action='INVERT')
    bpy.ops.object.delete(use_global=False, confirm=False)
    bpy.ops.outliner.orphans_purge(do_recursive=True)


bpy.types.WindowManager.show_mlt_interface = bpy.props.BoolProperty(name="Show MLT",
                                                                    description="When True, Show the MLT interface",
                                                                    default=False)


class RENDER_OT_generate_visualizer(bpy.types.Operator):
    bl_idname = "object.frequencies_generate"
    bl_label = "Generate Frequencies"
    bl_description = "Generates frequencies"

    @classmethod
    def poll(self, context):
        scene = context.scene
        if scene.open_filebrowser == "":
            return False
        elif context.scene.min_freq >= context.scene.max_freq:
            return False
        else:
            return True

    def execute(self, context):
        audio_file = bpy.path.abspath(context.scene.open_filebrowser)
        import_audio(audio_file, context.scene.chanel)
        audio_processing(audio_file,
                         context.scene.bz_bar_count,
                         context.scene.bz_spacing,
                         context.scene.attack,
                         context.scene.release,
                         context.scene.min_freq,
                         context.scene.max_freq)
        return {'FINISHED'}


class FREQUENCIES_PT_ui(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Frequencies"
    bl_context = "scene"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene
        row = layout.row()
        row.prop(scene, "open_filebrowser", icon="SOUND")
        row = layout.row()
        row.prop(scene, "bz_bar_count")
        row = layout.row()
        row.prop(scene, "bz_spacing")
        row = layout.row()
        row.prop(scene, "chanel")
        row = layout.row()
        row.prop(scene, "attack")
        row = layout.row()
        row.prop(scene, "release")
        cf = layout.column_flow(columns=2, align=False)
        cf.prop(scene, "min_freq")
        cf.prop(scene, "max_freq")

        row = layout.row()
        row.operator("object.frequencies_generate", icon="FILE_REFRESH")


def initprop():
    bpy.types.Scene.open_filebrowser = bpy.props.StringProperty(
        name="Audio Path",
        description="Define path of the audio file",
        subtype="FILE_PATH",
    )
    bpy.types.Scene.min_freq = bpy.props.IntProperty(
        name="Min frequency",
        description="Minimum frequency from where to start",
        default=20,
        min=20,
        max=20000
    )
    bpy.types.Scene.max_freq = bpy.props.IntProperty(
        name="Max frequency",
        description="Maximum frequency from where to start",
        default=20000,
        min=1,
        max=20000
    )
    bpy.types.Scene.bz_bar_count = bpy.props.IntProperty(
        name="Bar Count",
        description="The number of bars to make",
        default=30,
        min=1
    )
    bpy.types.Scene.bz_spacing = bpy.props.FloatProperty(
        name="Spacing",
        description="Spacing between bars",
        default=1.1,
        min=0
    )
    bpy.types.Scene.chanel = bpy.props.IntProperty(
        name="Chanel",
        description="Chanel of audio",
        default=1,
        min=1
    )
    bpy.types.Scene.attack = bpy.props.FloatProperty(
        name="Attack",
        description="Attack time",
        default=0.005,
        min=0,
        max=5
    )
    bpy.types.Scene.release = bpy.props.FloatProperty(
        name="Release",
        description="Release time",
        default=0.2,
        min=0,
        max=2
    )


def register():
    initprop()
    bpy.utils.register_class(RENDER_OT_generate_visualizer)
    bpy.utils.register_class(FREQUENCIES_PT_ui)


def unregister():
    bpy.utils.unregister_class(RENDER_OT_generate_visualizer)
    bpy.utils.unregister_class(FREQUENCIES_PT_ui)


if __name__ == "__main__":
    register()
