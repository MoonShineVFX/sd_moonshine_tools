import os
import gradio as gr
from . import symbols

def ui():
    with gr.Blocks() as controlnet_ui:
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