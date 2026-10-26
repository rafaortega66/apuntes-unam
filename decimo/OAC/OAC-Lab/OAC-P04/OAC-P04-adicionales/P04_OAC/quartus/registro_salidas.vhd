library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity registro_salidas is
  port ( clk, en, rst : in std_logic;
         salidas_in  : in  std_logic_vector(3 downto 0);
         salidas_out : out std_logic_vector(3 downto 0) );
end entity;
architecture rtl of registro_salidas is
  signal q : std_logic_vector(3 downto 0) := "0110";  -- todas inactivas
begin
  process(clk, rst) begin
    if rst = '1' then q <= "0110";
    elsif rising_edge(clk) then
      if en = '1' then q <= salidas_in; end if;
    end if;
  end process;
  salidas_out <= q;
end architecture;
