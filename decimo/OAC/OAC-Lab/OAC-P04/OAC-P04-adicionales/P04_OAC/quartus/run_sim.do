# Simulacion RTL Practica 4 en Questa
# En Questa: File > Change Directory -> carpeta del proyecto (donde estan los .vhd)
# Luego en la consola: do run_sim.do
if {[file exists work]} { vdel -lib work -all }
vlib work
vcom -93 rom_asm.vhd mux_entradas.vhd mux_liga.vhd mux_salidas.vhd divisor.vhd registro_estado.vhd registro_salidas.vhd p4_top.vhd tb_p4.vhd
vsim -voptargs="+acc" work.tb_p4
add wave -divider ENTRADAS
add wave -radix binary /tb_p4/clk /tb_p4/rn /tb_p4/x /tb_p4/y /tb_p4/z /tb_p4/w
add wave -divider ESTADO
add wave -radix unsigned /tb_p4/dut/est_pres /tb_p4/dut/est_sig
add wave -divider MEMORIA
add wave -radix binary /tb_p4/dut/u_rom/palabra
add wave -radix binary /tb_p4/dut/prueba /tb_p4/dut/liga_f /tb_p4/dut/liga_v /tb_p4/dut/sal_f /tb_p4/dut/sal_v
add wave -divider SELECCION
add wave -radix binary /tb_p4/dut/qsel /tb_p4/dut/salidas
add wave -divider SALIDAS_TARJETA
add wave -radix binary /tb_p4/dut/s_reg /tb_p4/led
run 1900 ns
wave zoom full
