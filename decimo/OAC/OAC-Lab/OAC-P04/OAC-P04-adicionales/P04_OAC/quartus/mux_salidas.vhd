library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity mux_salidas is
  port ( sal_v, sal_f : in std_logic_vector(3 downto 0);
         qsel : in std_logic;
         salidas : out std_logic_vector(3 downto 0) );
end entity;
architecture rtl of mux_salidas is
begin
  salidas <= sal_v when qsel = '1' else sal_f;
end architecture;
