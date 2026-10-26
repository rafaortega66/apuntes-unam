library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity mux_liga is
  port ( liga_v, liga_f : in std_logic_vector(2 downto 0);
         qsel : in std_logic;
         est_sig : out std_logic_vector(2 downto 0) );
end entity;
architecture rtl of mux_liga is
begin
  est_sig <= liga_v when qsel = '1' else liga_f;
end architecture;
