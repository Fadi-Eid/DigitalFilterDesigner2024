import flet as ft
import FIR_LeastSquares as FIR


class Parameter(ft.UserControl):
    def __init__(self, box_name, box_default, box_unit):
        super().__init__()
        self.box_name = box_name
        self.box_default = box_default
        self.box_unit = box_unit

        self.param_box = ft.TextField(expand=1, label=self.box_name, hint_text=self.box_default,
                                      input_filter=ft.InputFilter(
            regex_string=r"[0-9]",
            allow=True,
            replacement_string="",
        ))

    def build(self):
        self.param_unit = ft.Text(self.box_unit, weight=ft.FontWeight.BOLD)

        self.view = ft.Row(expand=1,
                        controls=[
                        self.param_box, self.param_unit
                        ]
                    )

        return self.view
    
    def value(self):
        string = self.param_box.value
        if(string==""):
            return ""
        value = float(string)
        return value
    
    def clean_all(self):
        self.param_box.value = ""
        self.update()




def main(page: ft.Page):
    page.title = "Digital Filter Designer 2024"
    page.theme_mode = "light"
    page.theme = ft.Theme(color_scheme_seed="red")
    
    page.window_width = 620        # window's width is 200 px
    page.window_height = 700       # window's height is 200 px
    #page.window_resizable = False  # window is not resizable
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    def on_keyboard(e: ft.KeyboardEvent):
        if (e.ctrl == True) and (e.key == "t" or e.key == "T"):
            if page.theme_mode == "dark":
                page.theme_mode = "light"
            else:
                page.theme_mode = "dark"
            page.update()
        if (e.ctrl == True) and (e.key == "d" or e.key == "D"):
            clear_shortcut()
        if (e.ctrl == True) and (e.key == "h" or e.key == "H"):
            open_repo()
    
    page.on_keyboard_event = on_keyboard

    sampling_input = Parameter("Sampling frequency", "e.g., 2000", "Hz")
    cutoff_input = Parameter("Cutoff frequency", "e.g., 389", "Hz")
    transition_input = Parameter("Transition width", "e.g., 20", "Hz")
    attenuation_input = Parameter("Stop Band Attenuation", "e.g., 90", "dB")

    parameter_section = ft.Column(
        controls=[
            sampling_input, transition_input, cutoff_input, attenuation_input
        ]
    )
    def display_info_true():
        sampling = sampling_input.value()
        transition = transition_input.value()
        cutoff = cutoff_input.value()
        attenuation = attenuation_input.value()
        filter = FIR.LP_Filter(attenuation, transition, cutoff, sampling)
        d = filter.Delay()
        d = str(d)
        l = filter.Length()
        l = str(l)
        delay.value = d + " ms"
        length.value = l
        page.update()




    def generate(e):
        valid = 1
        if(sampling_input.value() != ""):
            sampling = sampling_input.value()
        else:
            valid = 0
        if(transition_input.value()!= ""):
            transition = transition_input.value()
        else:
            valid = 0
        if(cutoff_input.value()!=""):
            cutoff = cutoff_input.value()
        else:
            valid = 0
        if(attenuation_input.value()!=""):
            attenuation = attenuation_input.value()
        else:
            valid = 0

        if(valid == 1):
            filter = FIR.LP_Filter(attenuation, transition, cutoff, sampling)
            filter.SaveCoeffs()
            dlg = ft.AlertDialog(
                    title=ft.Text("Coefficients generated\ncoefficients.csv")
                )
            page.dialog = dlg
            dlg.open = True
            page.update()
            display_info_true()
        else:
            delay.value = ""
            length.value = ""
            page.update()
            dlg = ft.AlertDialog(
                    title=ft.Text("Input fields cannot be empty"),
                    icon=ft.Icon(name="warning")
                )
            page.dialog = dlg
            dlg.open = True
            page.update()

        
    def validate(e):
        valid = 1
        if(sampling_input.value() != ""):
            sampling = sampling_input.value()
        else:
            valid = 0
        if(transition_input.value()!= ""):
            transition = transition_input.value()
        else:
            valid = 0
        if(cutoff_input.value()!=""):
            cutoff = cutoff_input.value()
        else:
            valid = 0
        if(attenuation_input.value()!=""):
            attenuation = attenuation_input.value()
        else:
            valid = 0
        
        if(valid == 1):
            filter = FIR.LP_Filter(attenuation, transition, cutoff, sampling)
            filter.PlotAmplitudeLinear()
            filter.PlotAmplitudeLogarithmic()
            filter.PlotImpulse()
            display_info_true()
        else:
            delay.value = ""
            length.value = ""
            page.update()
            dlg = ft.AlertDialog(
                    title=ft.Text("Input fields cannot be empty"),
                    icon=ft.Icon(name="warning")
                )
            page.dialog = dlg
            dlg.open = True
            page.update()

    def clear(e):
        cutoff_input.clean_all()
        sampling_input.clean_all()
        transition_input.clean_all()
        attenuation_input.clean_all()
        delay.value = "0.0 ms"
        length.value = "0"
        page.update()
        
    def clear_shortcut():
        cutoff_input.clean_all()
        sampling_input.clean_all()
        transition_input.clean_all()
        attenuation_input.clean_all()
        delay.value = "0.0 ms"
        length.value = "0"
        page.update()

    def open_repo():
        page.launch_url('https://github.com/Fadi-Eid/DigitalFilterDesign')  


    design_btn = ft.ElevatedButton(text="Generate filter", on_click=generate)
    validate_btn = ft.ElevatedButton(text="Validate filter", on_click=validate)
    clear_btn = ft.ElevatedButton(text="Clear input", on_click=clear)

    buttons = ft.Row(spacing=20, alignment=ft.MainAxisAlignment.CENTER, controls=[
        design_btn, validate_btn, clear_btn
    ])

    left_panel = ft.Column(controls=[parameter_section, buttons])

    # Create the right panel image
    img = ft.Image(
        src=f"./App/assets/help2.png",
        width=350,
        height=350,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10)
        #fit=ft.ImageFit.CONTAIN,
    )

    delay_box = ft.Text("Filter delay", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                        font_family="Tahoma")
    length_box = ft.Text("Filter length", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                         font_family="Tahoma")
    delay = ft.Text("0.0 ms", theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
    length = ft.Text("0", theme_style=ft.TextThemeStyle.HEADLINE_SMALL)

    delay_disp = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                           spacing=5,
                           controls=[delay_box, delay])
    length_disp = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[length_box, length])
    info_disp = ft.Column(expand=1, horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                          spacing=7,
                          controls=[delay_disp, length_disp])

    right_panel = ft.Row( width=page.window_width, controls=[img, info_disp])

    page.add(left_panel, right_panel)

ft.app(target=main, assets_dir="assets")
          