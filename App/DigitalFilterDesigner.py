import flet as ft
import FIR_LeastSquares as FIR


class Parameter(ft.UserControl):
    def __init__(self, box_name, box_default, box_unit):
        super().__init__()
        self.box_name = box_name
        self.box_default = box_default
        self.box_unit = box_unit

        self.param_box = ft.TextField(label=self.box_name, hint_text=self.box_default)

    def build(self):
        self.param_unit = ft.Text(self.box_unit)

        self.view = ft.Row(
                        controls=[
                        self.param_box, self.param_unit
                        ]
                    )

        return self.view
    
    def value(self):
        value = float(self.param_box.value)
        return value
    



def main(page: ft.Page):
    page.title = "Digital Filter Designer 2024"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    sampling_input = Parameter("Sampling frequency", "e.g., 2000", "Hz")
    cutoff_input = Parameter("Cutoff frequency", "e.g., 389", "Hz")
    transition_input = Parameter("Transition width", "e.g., 20", "Hz")
    attenuation_input = Parameter("Stop Band Attenuation", "e.g., 90", "dB")

    parameter_section = ft.Column(
        controls=[
            sampling_input, transition_input, cutoff_input, attenuation_input
        ]
    )

    def generate(e):
        sampling = sampling_input.value()
        transition = transition_input.value()
        cutoff = cutoff_input.value()
        attenuation = attenuation_input.value()
        filter = FIR.LP_Filter(attenuation, transition, cutoff, sampling)
        filter.SaveCoeffs()
        
    def validate(e):
        sampling = sampling_input.value()
        transition = transition_input.value()
        cutoff = cutoff_input.value()
        attenuation = attenuation_input.value()
        filter = FIR.LP_Filter(attenuation, transition, cutoff, sampling)
        filter.PlotAmplitudeLinear()
        filter.PlotAmplitudeLogarithmic()


    design_btn = ft.ElevatedButton(text="Generate filter", on_click=generate)
    validate_btn = ft.ElevatedButton(text="Validate filter", on_click=validate)

    buttons = ft.Row(controls=[
        design_btn, validate_btn
    ])


    page.add(parameter_section, buttons)

ft.app(target=main, view=ft.WEB_BROWSER)


          