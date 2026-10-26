library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- Memoria Entrada-Estado: 8 x 17 bits = 136 bits
-- palabra: prueba(3) | liga_f(3) | liga_v(3) | sal_f(4) | sal_v(4)
-- salidas: S1 S2 S3 S4  (S1,S4 estandar; S2,S3 negadas -> inactivo = 0110)
entity rom_asm is
  port ( est_pres : in  std_logic_vector(2 downto 0);
         prueba   : out std_logic_vector(2 downto 0);
         liga_f   : out std_logic_vector(2 downto 0);
         liga_v   : out std_logic_vector(2 downto 0);
         sal_f    : out std_logic_vector(3 downto 0);
         sal_v    : out std_logic_vector(3 downto 0) );
end entity;
architecture rtl of rom_asm is
  type rom_t is array (0 to 7) of std_logic_vector(16 downto 0);
  constant ROM : rom_t := (
  --       prueba  LF      LV      SF       SV
    0 => "100" & "001" & "001" & "1111" & "1111", -- E0: QX -> E1
    1 => "000" & "011" & "010" & "0010" & "0110", -- E1: X  F->E3 V->E2
    2 => "001" & "101" & "100" & "0100" & "0111", -- E2: Y  F->E5 V->E4
    3 => "010" & "000" & "110" & "0110" & "1110", -- E3: Z  F->E0 V->E6
    4 => "011" & "101" & "010" & "0010" & "0010", -- E4: W  F->E5 V->E2
    5 => "100" & "111" & "111" & "0100" & "0100", -- E5: QX -> E7
    6 => "011" & "110" & "111" & "0111" & "0010", -- E6: W  F->E6 V->E7
    7 => "100" & "000" & "000" & "1001" & "1001"  -- E7: QX -> E0
  );
  signal palabra : std_logic_vector(16 downto 0);
begin
  palabra <= ROM(to_integer(unsigned(est_pres)));
  prueba <= palabra(16 downto 14);
  liga_f <= palabra(13 downto 11);
  liga_v <= palabra(10 downto 8);
  sal_f  <= palabra(7 downto 4);
  sal_v  <= palabra(3 downto 0);
end architecture;
