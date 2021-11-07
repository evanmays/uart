## This file is a general .xdc for the ARTY Rev. A
## To use it in a project:
## - uncomment the lines corresponding to used pins
## - rename the used ports (in each line, after get_ports) according to the top level signal names in the project


# Clock signal

set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports clk]
create_clock -period 20.000 -name sys_clk_pin -waveform {0.000 10.000} -add [get_ports clk]

set_property -dict {PACKAGE_PIN A8  IOSTANDARD LVCMOS33} [get_ports sw_0]
set_property -dict {PACKAGE_PIN C11 IOSTANDARD LVCMOS33} [get_ports sw_1]

set_property -dict {PACKAGE_PIN D10 IOSTANDARD LVCMOS33} [get_ports uart_txd]
set_property -dict {PACKAGE_PIN A9  IOSTANDARD LVCMOS33} [get_ports uart_rxd]

set_property LOC E1 [get_ports led[0]]
set_property LOC G4 [get_ports led[1]]
set_property LOC H4 [get_ports led[2]]
set_property LOC K2 [get_ports led[3]]
set_property LOC H5 [get_ports led[4]]
set_property LOC J5 [get_ports led[5]]
set_property LOC T9 [get_ports led[6]]
set_property LOC T10 [get_ports led[7]]