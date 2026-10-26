# DE10-Lite (MAX 10 10M50DAF484C7G) - Tools > Tcl Scripts... > Run
set_global_assignment -name FAMILY "MAX 10"
set_global_assignment -name DEVICE 10M50DAF484C7G
set_global_assignment -name TOP_LEVEL_ENTITY p4_top
set_location_assignment PIN_P11 -to CLOCK_50
set_location_assignment PIN_B8  -to RESET_N
# Entradas: SW0=X  SW1=Y  SW2=Z  SW3=W
set_location_assignment PIN_C10 -to X
set_location_assignment PIN_C11 -to Y
set_location_assignment PIN_D12 -to Z
set_location_assignment PIN_C12 -to W
# LEDR0..3 = S1..S4 | LEDR9..7 = estado (izquierda)
set_location_assignment PIN_A8  -to LED[0]
set_location_assignment PIN_A9  -to LED[1]
set_location_assignment PIN_A10 -to LED[2]
set_location_assignment PIN_B10 -to LED[3]
set_location_assignment PIN_D13 -to LED[4]
set_location_assignment PIN_C13 -to LED[5]
set_location_assignment PIN_E14 -to LED[6]
set_location_assignment PIN_D14 -to LED[7]
set_location_assignment PIN_A11 -to LED[8]
set_location_assignment PIN_B11 -to LED[9]
