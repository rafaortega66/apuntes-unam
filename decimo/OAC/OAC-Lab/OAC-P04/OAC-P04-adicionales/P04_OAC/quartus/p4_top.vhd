library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- Top-level Practica 4 (DE0-Nano). Equivale al P4.bdf de la profesora.
-- X,Y,Z,W: DIP switches | KEY0: reset (activo bajo)
-- LED0..3 = S1 S2 S3 S4 | LED9..7 = estado presente (izquierda)
entity p4_top is
  generic ( DIV : natural := 25000000 );
  port ( CLOCK_50 : in std_logic;
         RESET_N  : in std_logic;
         X, Y, Z, W : in std_logic;
         LED : out std_logic_vector(9 downto 0) );
end entity;
architecture estructural of p4_top is
  signal en, rst, qsel : std_logic;
  signal est_pres, est_sig, prueba, liga_f, liga_v : std_logic_vector(2 downto 0);
  signal sal_f, sal_v, salidas, s_reg : std_logic_vector(3 downto 0);
begin
  rst <= not RESET_N;
  u_div : entity work.divisor generic map (DIV => DIV) port map (CLOCK_50, en);
  u_reg : entity work.registro_estado port map (CLOCK_50, en, rst, est_sig, est_pres);
  u_rom : entity work.rom_asm port map (est_pres, prueba, liga_f, liga_v, sal_f, sal_v);
  u_me  : entity work.mux_entradas port map (prueba, X, Y, Z, W, qsel);
  u_ml  : entity work.mux_liga port map (liga_v, liga_f, qsel, est_sig);
  u_ms  : entity work.mux_salidas port map (sal_v, sal_f, qsel, salidas);
  u_rs  : entity work.registro_salidas port map (CLOCK_50, en, rst, salidas, s_reg);
  LED(0) <= s_reg(3);  -- S1
  LED(1) <= s_reg(2);  -- S2 (negada)
  LED(2) <= s_reg(1);  -- S3 (negada)
  LED(3) <= s_reg(0);  -- S4
  LED(6 downto 4) <= "000";
  LED(9 downto 7) <= est_pres;  -- estado a la izquierda
end architecture;
