library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity mux_entradas is
  port ( prueba : in std_logic_vector(2 downto 0);
         X, Y, Z, W : in std_logic;
         qsel : out std_logic );
end entity;
architecture rtl of mux_entradas is
begin
  with prueba select
    qsel <= X   when "000",
            Y   when "001",
            Z   when "010",
            W   when "011",
            '1' when "100",   -- QX
            '0' when others;
end architecture;
