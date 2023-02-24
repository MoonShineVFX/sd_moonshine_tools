import os
import gradio as gr

from modules import script_callbacks, shared, paths, scripts
from modules.call_queue import wrap_gradio_gpu_call
from modules.shared import cmd_opts, opts, OptionInfo
from modules.ui import setup_progressbar
from pathlib import Path
from scripts.ui import ffmpeg, controlnet

def on_ui_tabs():
    with gr.Blocks() as moonshine_tools_interface:
        with gr.Row():
            with gr.Tab("FFmpeg"):
                with gr.Column(variant="panel"): 
                    ffmpeg.ui()
            with gr.Tab("ControlNet"):
                with gr.Column(variant="panel"): 
                    controlnet.ui()
                            
    return (moonshine_tools_interface, "Moonshine Tools", "moonshine_interface"), 

setting_path = str(Path(paths.script_path) / "sd_moonshine_tools")
os.makedirs(setting_path, exist_ok=True)
ffmpeg_path = ("%s/ffmpeg.exe" % setting_path)
sequence_root = ("%s/sequence" % setting_path)
os.makedirs(sequence_root, exist_ok=True)
video_root = ("%s/video" % setting_path)
os.makedirs(video_root, exist_ok=True)

def on_ui_settings():
    section = ('sd_moonshine_tools', "MoonshineTools")
    opts.add_option("ffmpeg_binary_path", OptionInfo(ffmpeg_path, "FFmpeg executable binary file path", section=section))
    opts.add_option("ffmpeg_frames", OptionInfo(sequence_root, "sequence root", section=section))
    opts.add_option("ffmpeg_video", OptionInfo(video_root, "video root", section=section))


script_callbacks.on_ui_settings(on_ui_settings)
script_callbacks.on_ui_tabs(on_ui_tabs)
