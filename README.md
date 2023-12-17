# Audio Visualizer

This Blender Python script generates a frequency-based audio visualizer using Blender's animation and sequencing capabilities. The script creates a set of bars representing different frequency ranges, and their heights are animated based on the audio input.

## Features
- Import audio file into Blender's Video Sequence Editor (VSE).
- Generate a set of bars representing different frequency ranges.
- Animate the bars based on the audio input, creating a dynamic visualizer.

## How to Use
1. **Installation:**
   - Copy and paste the script into Blender's Text Editor.
   - Run the script to register the custom operators and properties.

2. **User Interface:**
   - Go to the "Properties" panel in Blender.
   - Find the "Frequencies" tab.
   - Set the parameters for audio visualization:
      - **Audio Path:** Path to the audio file.
      - **Min Frequency:** Minimum frequency for visualization.
      - **Max Frequency:** Maximum frequency for visualization.
      - **Bar Count:** Number of bars to create.
      - **Spacing:** Spacing between bars.
      - **Channel:** Audio channel to use.
      - **Attack:** Attack time for audio processing.
      - **Release:** Release time for audio processing.
   - Click the "Generate Frequencies" button to generate the audio visualizer.

3. **Animation Playback:**
   - After running the script, switch to the "Graph Editor" to see the animated curves.
   - Play the animation to see the generated visualizer reacting to the audio.

## Notes
- The script works best with audio files that have a clear and distinct frequency range.
- Adjust the parameters to achieve the desired visual effect.

## Custom Operators and Properties
- `object.frequencies_generate`: Operator for generating the visualizer.
- `FREQUENCIES_PT_ui`: Panel for setting parameters in the "Properties" editor.

## Custom Properties
- `open_filebrowser`: Path to the audio file.
- `min_freq`: Minimum frequency for visualization.
- `max_freq`: Maximum frequency for visualization.
- `bz_bar_count`: Number of bars to create.
- `bz_spacing`: Spacing between bars.
- `chanel`: Audio channel to use.
- `attack`: Attack time for audio processing.
- `release`: Release time for audio processing.
- `show_mlt_interface`: Toggle to show/hide the MLT interface.

## Additional Information
- The script uses Blender's Video Sequence Editor (VSE) and 3D View functionalities to create and animate the visualizer.
- The audio processing involves creating duplicate meter objects and animating their properties based on the audio spectrum.

Feel free to customize and experiment with the parameters to achieve different visual effects!
