import os
import gradio as gr

# from modules import script_callbacks, shared, paths, scripts
# from modules.call_queue import wrap_gradio_gpu_call
# from modules.shared import cmd_opts, opts, OptionInfo
# from modules.ui import setup_progressbar
from pathlib import Path
from scripts.ui import ffmpeg, controlnet


ffmpeg_binary = r'C:\_Dev\Repository\AUTOMATIC1111-stable-diffusion-webui\sd_moonshine_tools\ffmpeg.exe'

def demo_ui():
    with gr.Blocks() as demo:     
        with gr.Row():
            with gr.Tab("FFmpeg"):
                with gr.Column(variant="panel"): 
                    ffmpeg.ui(ffmpeg_binary)
            with gr.Tab("ControlNet"):
                with gr.Column(variant="panel"): 
                    controlnet.ui()
        
    return demo


demo_ui().launch()