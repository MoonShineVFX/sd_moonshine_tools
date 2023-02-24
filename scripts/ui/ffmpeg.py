import os
import gradio as gr
from pathlib import Path



def ui(ffmpeg_binary=""):
    ffmped_logs = ''' '''
    if os.path.isfile(ffmpeg_binary):
        ffmped_logs += f''' ffmpeg.exe exist, ready to Go'''
    else :
        ffmped_logs += f''' ffmpeg.exe not exist'''
    
    with gr.Blocks() as ffmpeg_ui:
        with gr.Row():
            with gr.Column(): 
                ffmpeg_mode = gr.Dropdown(label="Process Mode", choices=["Video to Sequence", "Sequence to Video"],value='Video to Sequence',interactive=True)
                ffmpeg_seq_intput = gr.Textbox(label='Sequence Folder Input', visible=False, interactive=True)
                ffmpeg_movie_intput = gr.File(label='Movie File Input', visible=True, interactive=True, file_types=['video'])
                ffmpeg_seq_output = gr.Textbox(label='Sequence Folder Output', visible=True, interactive=True)
                ffmpeg_movie_output = gr.Textbox(label='Movie File Output', visible=False, interactive=True)
           
            with gr.Column(): 
                ffmpeg_bitmap_format=gr.Radio(label="Bitmap Format", choices=["jpg", "png", "exr"],value='jpg',interactive=True)
                with gr.Box(visible=True) as jpg_settings:
                    with gr.Row():
                        ffmpeg_jpg_color = gr.Radio(label="Color", choices=["BW", "RGB"],value='RGB',interactive=True)
                    with gr.Row():
                        ffmpeg_jpg_quality = gr.Slider(1, 100, label="Quality",value='80',interactive=True, step=1)
                with gr.Box(visible=False) as png_settings:
                    with gr.Row():
                        ffmpeg_png_color = gr.Radio(label="Color", choices=["BW", "RGB","RGBA"],value='RGB',interactive=True)
                        ffmpeg_png_depth = gr.Radio(label="Color Depth", choices=["8", "16"],value='8',interactive=True)
                    with gr.Row():
                        ffmpeg_png_quality = gr.Slider(0, 9, label="Compression",value='4',interactive=True, step=1)
                with gr.Box(visible=False) as exr_settings:
                    with gr.Row():
                        ffmpeg_exr_color = gr.Radio(label="Color", choices=["BW", "RGB","RGBA"],value='RGB',interactive=True)
                        ffmpeg_exr_depth = gr.Radio(label="Color Depth", choices=["Float(Half-16)", "Float(Full-32)"],value='Float(Half-16)',interactive=True)
                    with gr.Row():
                        ffmpeg_exr_codec = gr.Dropdown(label="Codec", choices=["None", "ZIP(lossless)", "ZIPS(lossless)", "DWAB(lossy)", "DWAA(lossy)"],value='ZIP(lossless)',interactive=True)
                        ffmpeg_exr_option = gr.CheckboxGroup(label="Options", choices=["Z Buffer", "Preview"],value=[],interactive=True)
                    
        with gr.Row():
            ffmpeg_cancel = gr.Button(value="Cancel")
            ffmpeg_run = gr.Button(value="Preprocess", variant='primary')

        with gr.Row():
            logs = gr.Markdown(ffmped_logs)
            
        ui_collect=dict()
        
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
            outputs=[ffmpeg_seq_intput, ffmpeg_seq_output, ffmpeg_movie_intput, ffmpeg_movie_output],
            )
        
        def update_bitmap_format(bitmap_format):
            ui_status = {
                jpg_settings:gr.update(visible=(bitmap_format == 'jpg')),
                png_settings:gr.update(visible=(bitmap_format == 'png')),
                exr_settings:gr.update(visible=(bitmap_format == 'exr')),
            }

            return ui_status
        
        ffmpeg_bitmap_format.change(
            fn=update_bitmap_format,
            inputs=[ffmpeg_bitmap_format],
            outputs=[jpg_settings,png_settings,exr_settings],
        )
 
        def run_ffmpeg(mode,seq_intput,movie_intput,seq_output,movie_output,bitmap_format,jpg_color,jpg_quality,png_color,png_depth,png_quality,exr_color,exr_depth,exr_codec,exr_option):
            color_depth=8
            if movie_intput:
                if os.path.isfile(ffmpeg_binary):
                    if mode=="Video to Sequence":
                        output_name = Path(movie_intput.orig_name).stem
                        command = r"%s -i %s -pix_fmt %s %s\%s" % (ffmpeg_binary, movie_intput, seq_output, output_name)
                        print (command)
                
            
                
        ffmpeg_run.click(
            fn=run_ffmpeg,
            inputs=[ffmpeg_mode,
                    ffmpeg_seq_intput,
                    ffmpeg_movie_intput,
                    ffmpeg_seq_output,
                    ffmpeg_movie_output,
                    ffmpeg_bitmap_format,
                    ffmpeg_jpg_color,
                    ffmpeg_jpg_quality,
                    ffmpeg_png_color,
                    ffmpeg_png_depth,
                    ffmpeg_png_quality,
                    ffmpeg_exr_color,
                    ffmpeg_exr_depth,
                    ffmpeg_exr_codec,
                    ffmpeg_exr_option],
            outputs=[],
        )
        
    return ffmpeg_ui