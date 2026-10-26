library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity registro_estado is
  port ( clk, en, rst : in std_logic;   -- rst activo en alto
         est_sig  : in  std_logic_vector(2 downto 0);
         est_pres : out std_logic_vector(2 downto 0) );
end entity;
architecture rtl of registro_estado is
  signal q : std_logic_vector(2 downto 0) := "000";
begin
  process(clk, rst) begin
    if rst = '1' then q <= "000";
    elsif rising_edge(clk) then
      if en = '1' then q <= est_sig; end if;
    end if;
  end process;
  est_pres <= q;
end architecture;
