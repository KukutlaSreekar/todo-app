import PySimpleGUI as sg


class Matrix(values):
    def __init__(self):
        self.values = values
        self.m_1_row1, self.m_1_row2, self.m_1_row3 = self.matrix_construct

        # Creating rows for cofactor and adjoint matrices
        self.mm_1_row1_0_ = +((self.m_1_row2[1] * self.m_1_row3[2]) - (self.m_1_row2[2] * self.m_1_row3[1]))
        self.mm_1_row1_1_ = -((self.m_1_row2[0] * self.m_1_row3[2]) - (self.m_1_row2[2] * self.m_1_row3[0]))
        self.mm_1_row1_2_ = +((self.m_1_row2[0] * self.m_1_row3[1]) - (self.m_1_row2[1] * self.m_1_row3[0]))
        self.mm_1_row2_0_ = -((self.m_1_row1[1] * self.m_1_row3[2]) - (self.m_1_row1[2] * self.m_1_row3[1]))
        self.mm_1_row2_1_ = +((self.m_1_row1[0] * self.m_1_row3[2]) - (self.m_1_row1[2] * self.m_1_row3[0]))
        self.mm_1_row2_2_ = -((self.m_1_row1[0] * self.m_1_row3[1]) - (self.m_1_row1[1] * self.m_1_row3[0]))
        self.mm_1_row3_0_ = +((self.m_1_row1[1] * self.m_1_row2[2]) - (self.m_1_row1[2] * self.m_1_row2[1]))
        self.mm_1_row3_1_ = -((self.m_1_row1[0] * self.m_1_row2[2]) - (self.m_1_row1[2] * self.m_1_row2[0]))
        self.mm_1_row3_2_ = +((self.m_1_row1[0] * self.m_1_row2[1]) - (self.m_1_row1[1] * mself._1_row2[0]))

    def determinant(self):
        det = self.m_1_row1[0] * (self.m_1_row2[1] * self.m_1_row3[2] - self.m_1_row2[2] * self.m_1_row3[1]) \
              - self.m_1_row1[1] * (self.m_1_row2[0] * self.m_1_row3[2] - self.m_1_row2[2] * self.m_1_row3[0]) \
              + self.m_1_row1[2] * (self.m_1_row2[0] * self.m_1_row3[1] - self.m_1_row2[1] * self.m_1_row3[0])
        return det

    def cofactor(self):

        content = f"""[   {self.mm_1_row1_0_} , {self.mm_1_row1_1_} , {self.mm_1_row1_2_}   ] 
                      |   {self.mm_1_row2_0_} , {self.mm_1_row2_1_} , {self.mm_1_row2_2_}   | 
                      [   {self.mm_1_row3_0_} , {self.mm_1_row3_1_} , {self.mm_1_row3_2_}   ]"""

        return content

    def adjoint(self):

        content = f"""[   {self.mm_1_row1_0_} , {self.mm_1_row2_0_} , {self.mm_1_row3_0_}   ] 
                      |   {self.mm_1_row1_1_} , {self.mm_1_row2_1_} , {self.mm_1_row3_1_}   | 
                      [   {self.mm_1_row1_2_} , {self.mm_1_row2_2_} , {self.mm_1_row3_2_}   ]"""

        return content

    @property
    def matrix_construct(self):
        matrix_1 = []
        for key, value in self.values.items():
            x = self.values[key]
            x = x.split(",")
            x = [int(element) for element in x]
            matrix_1.append(x)
        return matrix_1


class UserInput(values):

    def row1(self):
        Input_row1 = sg.InputText(tooltip="Enter the first row of the matrix as x, y, z", key="row1")
        return Input_row1

    def row2(self):
        Input_row2 = sg.InputText(tooltip="Enter the second row of the matrix as x, y, z", key="row2")
        return Input_row2

    def row3(self):
        Input_row3 = sg.InputText(tooltip="Enter the third row of the matrix as x, y, z", key="row3")
        return Input_row3


def execute_matrix_gui():
    user_input = UserInput()
    calculate_button = sg.Button("Calculate det", key="button")
    exit_button = sg.Button("Exit", key="exit")
    cofactor_matrix_button = sg.Button("Cofactor Matrix", key="cofactor")
    adjoint_matrix_button = sg.Button("Adjoint Matrix", key="adjoint")
    text1 = sg.Text("Row 1 =")
    text2 = sg.Text("Row 2 =")
    text3 = sg.Text("Row 3 =")
    text_result = sg.Text('', key='result')
    window = sg.Window("Matrix calculator", layout=[[text1, user_input.row1()],
                                                    [text2, user_input.row2()],
                                                    [text3, user_input.row3()],
                                                    [calculate_button, text_result, exit_button, cofactor_matrix_button,
                                                     adjoint_matrix_button]], font=('Helvetica', 10))

    while True:
        event, values = window.read()
        matrix_a = Matrix(values)
        if event == sg.WIN_CLOSED:
            break
        if event == "exit":
            break
        if event == "button":
            window['result'].update(value=matrix_a.determinant())
        if event == "cofactor":
            sg.popup(matrix_a.cofactor())
        if event == "adjoint":
            sg.popup(matrix_a.adjoint())

    window.close()


execute_matrix_gui()