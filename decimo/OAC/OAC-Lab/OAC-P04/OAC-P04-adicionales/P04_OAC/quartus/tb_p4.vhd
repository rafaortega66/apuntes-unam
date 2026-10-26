library ieee;
use ieee.std_logic_1164.all;
entity tb_p4 is end entity;
architecture sim of tb_p4 is
  signal clk : std_logic := '0';
  signal rn  : std_logic := '0';
  signal x, y, z, w : std_logic := '0';
  signal led : std_logic_vector(9 downto 0);
begin
  dut: entity work.p4_top generic map (DIV => 2)
       port map (clk, rn, x, y, z, w, led);
  clk <= not clk after 10 ns;
  process begin
    wait for 50 ns; rn <= '1';
    x<='0'; y<='0'; z<='0'; w<='0'; wait for 400 ns;  -- E0 E1 E3 E0
    x<='1'; y<='1'; w<='1';         wait for 400 ns;  -- E1 E2 E4 E2
    y<='0';                         wait for 400 ns;  -- E2 E5 E7 E0
    x<='0'; z<='1'; w<='0';         wait for 300 ns;  -- E3 E6 E6
    w<='1';                         wait for 300 ns;  -- E7 E0
    wait;
  end process;
end architecture;
