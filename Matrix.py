
#Matrix1
"""
m_1_row1 = "Temp"
m_1_row1 = input("Enter the first row of the first matrix as x, y, z")
m_1_row1 = m_1_row1.split(",")
m_1_row1 = [int(element) for element in m_1_row1]
m_1_row2 = "Temp"
m_1_row2 = input("Enter the first row of the first matrix as x, y, z")
m_1_row2 = m_1_row2.split(",")
m_1_row2 = [int(element) for element in m_1_row2]
m_1_row3 = "Temp"
m_1_row3 = input("Enter the first row of the first matrix as x, y, z")
m_1_row3 = m_1_row2.split(",")
m_1_row3 = [int(element) for element in m_1_row3]
"""






'''
matrix_1 = []
i = 0
while i < 3:
    i += 1
    x = input("Enter the first row of the first matrix as x, y, z")
    x = x.split(",")
    x = [int(element) for element in x]
    matrix_1.append(x)



m_1_row1, m_1_row2, m_1_row3 = matrix_1

det = m_1_row1[0]*(m_1_row2[1]*m_1_row3[2] - m_1_row2[2]*m_1_row3[1]) - m_1_row1[1]*(m_1_row2[0]*m_1_row3[2] - m_1_row2[2]*m_1_row3[0]) \
      + m_1_row1[2]*(m_1_row2[0]*m_1_row3[1] - m_1_row2[1]*m_1_row3[0])

print(det)
'''
import PySimpleGUI as sg

Input_row1 = sg.InputText(tooltip="Enter the first row of the matrix as x, y, z", key="row1")
Input_row2 = sg.InputText(tooltip="Enter the second row of the matrix as x, y, z",key="row2")
Input_row3 = sg.InputText(tooltip="Enter the third row of the matrix as x, y, z",key="row3")
calculate_button = sg.Button("Calculate det", key="button")
exit_button = sg.Button("Exit", key="exit")
cofactor_matrix_button = sg.Button("Cofactor Matrix", key="cofactor")
adjoint_matrix_button = sg.Button("Adjoint Matrix", key="adjoint")
text1 = sg.Text("Row 1 =")
text2 = sg.Text("Row 2 =")
text3 = sg.Text("Row 3 =")
text_result = sg.Text('', key='result')

window = sg.Window("Matrix calculator", layout=[[text1, Input_row1],
                                                     [text2, Input_row2],
                                                     [text3, Input_row3],
                                                     [calculate_button, text_result, exit_button, cofactor_matrix_button, adjoint_matrix_button]],font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED:
        break
    if event == "exit":
        break
    if event == "button":
        matrix_1 = []
        for key, value in values.items():
                x = values[key]
                x = x.split(",")
                x = [int(element) for element in x]
                matrix_1.append(x)
        m_1_row1, m_1_row2, m_1_row3 = matrix_1
        det = m_1_row1[0]*(m_1_row2[1]*m_1_row3[2] - m_1_row2[2]*m_1_row3[1]) \
              - m_1_row1[1]*(m_1_row2[0]*m_1_row3[2] - m_1_row2[2]*m_1_row3[0]) \
              + m_1_row1[2]*(m_1_row2[0]*m_1_row3[1] - m_1_row2[1]*m_1_row3[0])
        window['result'].update(value=det)
    if event == "cofactor":
        matrix_1 = []
        for key, value in values.items():
            x = values[key]
            x = x.split(",")
            x = [int(element) for element in x]
            matrix_1.append(x)
        m_1_row1, m_1_row2, m_1_row3 = matrix_1
        mm_1_row1_0_ = +((m_1_row2[1] * m_1_row3[2]) - (m_1_row2[2] * m_1_row3[1]))
        mm_1_row1_1_ = -((m_1_row2[0] * m_1_row3[2]) - (m_1_row2[2] * m_1_row3[0]))
        mm_1_row1_2_ = +((m_1_row2[0] * m_1_row3[1]) - (m_1_row2[1] * m_1_row3[0]))
        mm_1_row2_0_ = -((m_1_row1[1] * m_1_row3[2]) - (m_1_row1[2] * m_1_row3[1]))
        mm_1_row2_1_ = +((m_1_row1[0] * m_1_row3[2]) - (m_1_row1[2] * m_1_row3[0]))
        mm_1_row2_2_ = -((m_1_row1[0] * m_1_row3[1]) - (m_1_row1[1] * m_1_row3[0]))
        mm_1_row3_0_ = +((m_1_row1[1] * m_1_row2[2]) - (m_1_row1[2] * m_1_row2[1]))
        mm_1_row3_1_ = -((m_1_row1[0] * m_1_row2[2]) - (m_1_row1[2] * m_1_row2[0]))
        mm_1_row3_2_ = +((m_1_row1[0] * m_1_row2[1]) - (m_1_row1[1] * m_1_row2[0]))

        sg.popup(f"[   {mm_1_row1_0_} , {mm_1_row1_1_} , {mm_1_row1_2_}   ] \n "
                 f"|   {mm_1_row2_0_} , {mm_1_row2_1_} , {mm_1_row2_2_}   | \n "
                 f"[   {mm_1_row3_0_} , {mm_1_row3_1_} , {mm_1_row3_2_}   ]")

    if event == "adjoint":
        matrix_1 = []
        for key, value in values.items():
            x = values[key]
            x = x.split(",")
            x = [int(element) for element in x]
            matrix_1.append(x)
        m_1_row1, m_1_row2, m_1_row3 = matrix_1
        mm_1_row1_0_ = +((m_1_row2[1] * m_1_row3[2]) - (m_1_row2[2] * m_1_row3[1]))
        mm_1_row1_1_ = -((m_1_row2[0] * m_1_row3[2]) - (m_1_row2[2] * m_1_row3[0]))
        mm_1_row1_2_ = +((m_1_row2[0] * m_1_row3[1]) - (m_1_row2[1] * m_1_row3[0]))
        mm_1_row2_0_ = -((m_1_row1[1] * m_1_row3[2]) - (m_1_row1[2] * m_1_row3[1]))
        mm_1_row2_1_ = +((m_1_row1[0] * m_1_row3[2]) - (m_1_row1[2] * m_1_row3[0]))
        mm_1_row2_2_ = -((m_1_row1[0] * m_1_row3[1]) - (m_1_row1[1] * m_1_row3[0]))
        mm_1_row3_0_ = +((m_1_row1[1] * m_1_row2[2]) - (m_1_row1[2] * m_1_row2[1]))
        mm_1_row3_1_ = -((m_1_row1[0] * m_1_row2[2]) - (m_1_row1[2] * m_1_row2[0]))
        mm_1_row3_2_ = +((m_1_row1[0] * m_1_row2[1]) - (m_1_row1[1] * m_1_row2[0]))

        sg.popup(f"[   {mm_1_row1_0_} , {mm_1_row2_0_} , {mm_1_row3_0_}   ] \n "
                 f"|   {mm_1_row1_1_} , {mm_1_row2_1_} , {mm_1_row3_1_}   | \n "
                 f"[   {mm_1_row1_2_} , {mm_1_row2_2_} , {mm_1_row3_2_}   ]")


window.close()

























