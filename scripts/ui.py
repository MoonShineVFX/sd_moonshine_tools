import os
import gradio as gr

cn_models = {}  
refresh_symbol = '\U0001f504'       # 🔄
switch_values_symbol = '\U000021C5' # ⇅
camera_symbol = '\U0001F4F7'        # 📷
reverse_symbol = '\U000021C4'       # ⇄

class ToolButton(gr.Button, gr.components.FormComponent):
    """Small button with single emoji as text, fits inside gradio forms"""

    def __init__(self, **kwargs):
        super().__init__(variant="tool", **kwargs)

    def get_block_name(self):
        return "button"

def ui_ffmpeg():
    with gr.Blocks() as ffmpeg_ui:
        with gr.Row():
            with gr.Column(variant="panel"): 
                ffmpeg_mode = gr.Dropdown(label="Process Mode", choices=["Video to Sequence", "Sequence to Video"],value='Video to Sequence',interactive=True)
                with gr.Box():
                    ffmpeg_seq_intput = gr.Textbox(label='Sequence Folder Input', visible=False, interactive=True)
                    ffmpeg_movie_intput = gr.File(label='Movie File Input', visible=True, interactive=True)
                    ffmpeg_seq_output = gr.Textbox(label='Sequence Folder Output', visible=True, interactive=True)
                    ffmpeg_movie_output = gr.Textbox(label='Movie File Output', visible=False, interactive=True)

            def update_ffmpeg_ui(mode):
                if mode == 'Video to Sequence':
                    ui_status = {ffmpeg_seq_intput: gr.update(visible=False),
                                ffmpeg_movie_intput: gr.update(visible=True), 
                                ffmpeg_seq_output: gr.update(visible=True), 
                                ffmpeg_movie_output: gr.update(visible=False)}
                elif mode == 'Sequence to Video':
                    ui_status = {ffmpeg_seq_intput: gr.update(visible=True),
                                ffmpeg_movie_intput: gr.update(visible=False), 
                                ffmpeg_seq_output: gr.update(visible=False), 
                                ffmpeg_movie_output: gr.update(visible=True)}
                return ui_status
            
            ffmpeg_mode.change(
                fn=update_ffmpeg_ui,
                inputs=[ffmpeg_mode],
                outputs=[ffmpeg_seq_intput, ffmpeg_seq_output,ffmpeg_movie_intput,ffmpeg_movie_output],
                )
            
            with gr.Column(variant="panel"): 
                bitmap_format=gr.Radio(label="Bitmap Format", choices=["jpg", "png", "exr"],value='jpg',interactive=True)
                
        with gr.Row():
            sp_cancel = gr.Button(value="Cancel")
            sp_run = gr.Button(value="Preprocess", variant='primary')

    return ffmpeg_ui

DESCRIPTION = '''# ControlNet

This is an unofficial demo for [https://github.com/lllyasviel/ControlNet](https://github.com/lllyasviel/ControlNet).

If you are interested in trying out other base models, check out [this Space](https://huggingface.co/spaces/hysts/ControlNet-with-other-models) as well.
'''
if (SPACE_ID := os.getenv('SPACE_ID')) is not None:
    DESCRIPTION += f'''<p>For faster inference without waiting in queue, you may duplicate the space and upgrade to GPU in settings.<br/>
<a href="https://huggingface.co/spaces/{SPACE_ID}?duplicate=true">
<img style="margin-top: 0em; margin-bottom: 0em" src="https://bit.ly/3gLdBN6" alt="Duplicate Space"></a>
<p/>
'''

def ui_controlnet():
    with gr.Blocks() as controlnet_ui:
        gr.Markdown(DESCRIPTION)
        with gr.Tabs():
            with gr.TabItem('Canny'):
                gr.Button()
            with gr.TabItem('Hough'):
                gr.Button()
            with gr.TabItem('HED'):
                gr.Button()
            with gr.TabItem('Scribble'):
                gr.Button()
            with gr.TabItem('Scribble Interactive'):
                gr.Button()
            with gr.TabItem('Fake Scribble'):
                gr.Button()
            with gr.TabItem('Pose'):
                gr.Button()
            with gr.TabItem('Segmentation'):
                gr.Button()
            with gr.TabItem('Depth'):
                gr.Button()
            with gr.TabItem('Normal map'):
                gr.Button()
            
    return controlnet_ui