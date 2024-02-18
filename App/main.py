import flet as ft
import FIR_LeastSquares as FIR
import time


class Parameter(ft.UserControl):
    def __init__(self, box_name, box_default, box_unit):
        super().__init__()
        self.box_name = box_name
        self.box_default = box_default
        self.box_unit = box_unit

        self.param_box = ft.TextField(expand=1, label=self.box_name, hint_text=f"e.g., {self.box_default}",
                                      input_filter=ft.InputFilter(
            regex_string=r"[0-9]",
            allow=True,
            replacement_string="",
        ), height=70)

    

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

    def set_to_default(self):
        self.param_box.value = self.box_default
        self.update()

    def error(self, message):
        self.param_box.error_text = message
        self.update()




def main(page: ft.Page):
    page.title = "Digital Filter Designer 2024"
    page.theme_mode = "light"
    page.theme = ft.Theme(color_scheme_seed="blue")
    page.scroll = ft.ScrollMode.AUTO
    
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
            open_repo(0)
        if (e.ctrl == True) and (e.key == "n" or e.key == "N"):
            sampling_input.set_to_default()
            transition_input.set_to_default()
            cutoff_input.set_to_default()
            attenuation_input.set_to_default()
        if (e.ctrl == True) and (e.key == "r" or e.key == "R"):
            # compute length and delay only
            valid = 1
            if(sampling_input.value() == ""):
                sampling_input.error("this field is required")
                valid = 0
            else:
                sampling_input.error("")
            if(cutoff_input.value() == ""):
                cutoff_input.error("this field is required")
                valid = 0
            else:
                cutoff_input.error("")
            if(attenuation_input.value() == ""):
                attenuation_input.error("this field is required")
                valid = 0
            else:
                attenuation_input.error("")
            if(transition_input.value() == ""):
                transition_input.error("this field is required")
                valid = 0
            else:
                transition_input.error("")
            
            if valid == 1:
                sampling_input.error("")
                cutoff_input.error("")
                attenuation_input.error("")
                transition_input.error("")
                display_info_true()
            
    
    page.on_keyboard_event = on_keyboard

    sampling_input = Parameter("Sampling frequency", "2000", "Hz")
    cutoff_input = Parameter("Cutoff frequency", "400", "Hz")
    transition_input = Parameter("Transition width", "20", "Hz")
    attenuation_input = Parameter("Stop Band Attenuation", "57", "dB")

    parameter_section = ft.Column(
        controls=[
            sampling_input, transition_input, cutoff_input, attenuation_input
        ],
        width=550
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

    def generate_and_save_filter(e: ft.FilePickerResultEvent):
        sampling = sampling_input.value()
        cutoff = cutoff_input.value()
        attenuation = attenuation_input.value()
        transition = transition_input.value()
        page.splash = ft.ProgressBar()
        design_btn.disabled = True
        validate_btn.disabled = True
        clear_btn.disabled = True
        page.update()
        time.sleep(2)
        page.splash = None
        page.update()
        filter = FIR.LP_Filter(attenuation, transition, cutoff, sampling)

        filter.SaveCoeffs(e.path)
        dlg = ft.AlertDialog(
                icon=ft.Icon(name="Done"),
                title=ft.Text("Coefficients generated"),
                bgcolor=ft.colors.GREEN_200
            )
        page.dialog = dlg
        dlg.open = True
        page.update()
        display_info_true()
        design_btn.disabled = False
        validate_btn.disabled = False
        clear_btn.disabled = False
        page.update()
        
        

    def generate(e):
        valid = 1
        if(sampling_input.value() == ""):
            sampling_input.error("this field is required")
            valid = 0
        else:
            sampling_input.error("")
        if(cutoff_input.value() == ""):
            cutoff_input.error("this field is required")
            valid = 0
        else:
            cutoff_input.error("")
        if(attenuation_input.value() == ""):
            attenuation_input.error("this field is required")
            valid = 0
        else:
            attenuation_input.error("")
        if(transition_input.value() == ""):
            transition_input.error("this field is required")
            valid = 0
        else:
            transition_input.error("")
        
        if valid == 1:
            sampling_input.error("")
            cutoff_input.error("")
            attenuation_input.error("")
            transition_input.error("")
            file_picker = ft.FilePicker(on_result=generate_and_save_filter)
            page.overlay.append(file_picker)
            page.update()
            file_picker.get_directory_path()
        
        else:
            delay.value = ""
            length.value = ""
            page.update()

        
    def validate(e):
        valid = 1
        if(sampling_input.value() != ""):
            sampling_input.error("")
            sampling = sampling_input.value()
        else:
            sampling_input.error("this field is required")
            valid = 0
        if(transition_input.value()!= ""):
            transition_input.error("")
            transition = transition_input.value()
        else:
            transition_input.error("this field is required")
            valid = 0
        if(cutoff_input.value()!=""):
            cutoff_input.error("")
            cutoff = cutoff_input.value()
        else:
            cutoff_input.error("this field is required")
            valid = 0
        if(attenuation_input.value()!=""):
            attenuation_input.error("")
            attenuation = attenuation_input.value()
        else:
            attenuation_input.error("this field is required")
            valid = 0
        
        if(valid == 1):
            sampling_input.error("")
            cutoff_input.error("")
            attenuation_input.error("")
            transition_input.error("")
            page.splash = ft.ProgressBar()
            design_btn.disabled = True
            validate_btn.disabled = True
            clear_btn.disabled = True
            page.update()
            time.sleep(2)
            page.splash = None
            page.update()
            filter = FIR.LP_Filter(attenuation, transition, cutoff, sampling)
            filter.PlotAmplitudeLinear()
            filter.PlotAmplitudeLogarithmic()
            filter.PlotImpulse()
            display_info_true()
            dlg = ft.AlertDialog(
                icon=ft.Icon(name="Done"),
                title=ft.Text("     Plots are Ready"),
                bgcolor=ft.colors.GREEN_300
            )
            page.dialog = dlg
            dlg.open = True
            page.update()
            design_btn.disabled = False
            validate_btn.disabled = False
            clear_btn.disabled = False
            page.update()
            
        else:
            delay.value = ""
            length.value = ""
            page.update()

    def clear(e):
        sampling_input.error("")
        cutoff_input.error("")
        attenuation_input.error("")
        transition_input.error("")
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

    def open_repo(x):
        page.launch_url('https://github.com/Fadi-Eid/DigitalFilterDesign')

    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.GREEN_300,
        leading=ft.Icon(ft.icons.INBOX, color=ft.colors.LIGHT_BLUE_100, size=40),
        content=ft.Text(
            "\n CTRL + H  to open GitHub docs\n CTRL + T to change the theme\n" + 
            " CTRL + D to delete input values\n CTRL + N to fill the fields with default values\n" + 
            " CTRL + R to compute specified filter length and delay" + "\n"
        ),
        actions=[
            ft.TextButton("Close", on_click=close_banner),
        ],
    )

    def show_banner_click(e):
        if page.banner.open == False:
            page.banner.open = True
            page.update()
        else:
            page.banner.open = False
            page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("Digital Filter Designer 2024 - FIR",
                      color=ft.colors.GREY_800,
                      size=16,
                      weight=ft.FontWeight.W_200,),
        leading_width=40,
        toolbar_height=40,
        center_title=False,
        bgcolor=ft.colors.BLUE_100,
        actions=[
            ft.IconButton(ft.icons.HELP, on_click=show_banner_click)
        ],
    )


    help_buton = ft.IconButton(icon=ft.icons.LINK, on_click=open_repo)
    design_btn = ft.ElevatedButton(text="Generate filter", on_click=generate)
    validate_btn = ft.ElevatedButton(text="Validate filter", on_click=validate)
    clear_btn = ft.ElevatedButton(text="Clear input", on_click=clear)

    buttons = ft.Row(spacing=20, alignment=ft.MainAxisAlignment.CENTER, controls=[
        design_btn, validate_btn, clear_btn, help_buton
    ], scroll=True)

    left_panel = ft.Column(controls=[parameter_section, buttons])

    # Create the right panel image
    img = ft.Image(
        src=f"./assets/help2.png",
        width=320,
        height=320,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(5)
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
          