library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 50 MHz -> pulso de habilitacion cada DIV ciclos (25M = 0.5 s)
entity divisor is
  generic ( DIV : natural := 25000000 );
  port ( clk : in std_logic; en : out std_logic );
end entity;
architecture rtl of divisor is
  signal cnt : natural range 0 to DIV-1 := 0;
begin
  process(clk) begin
    if rising_edge(clk) then
      if cnt = DIV-1 then cnt <= 0; en <= '1';
      else cnt <= cnt + 1; en <= '0'; end if;
    end if;
  end process;
end architecture;
