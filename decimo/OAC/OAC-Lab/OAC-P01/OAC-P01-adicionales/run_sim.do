vlib work
vlog -work work practica1.vo
vlog -work work Waveform.vwf.vt
vsim -voptargs="+acc" -t 1ps -L cycloneive_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate_ver -L altera_lnsim_ver work.practica1_vlg_vec_tst
add wave -radix binary /*
run -all
