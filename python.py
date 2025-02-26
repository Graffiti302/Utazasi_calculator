#Biró Botond, Dévényi Donát, Bebesi Martin, Csabai Áron
 
autopalya_seb = 117
fout_seb = 72
lakott_ter_seb = 40
benzin = 684
autopalya_fogy = 8.5
fout_fogy = 7
lakott_ter_fogy = 9.5
autopalya_matrica = 5320
 
print("Üdvözöljük az Autó út kalkulátorunkban.⏰")
print("Itt tud választani,hogy milyen úton szeretne menni,mennyit.(Autopálya/Főút/Város)🛣")
autopalya_ut = int(input("Autópály útját gépeld ide:"))
fout_ut = int(input("Fő út útját gépeld ide:"))
lakott_ter_ut = int(input("Lakott területek alatt megtett út útját gépeld ide:"))
 
autopalya_ido = autopalya_ut/autopalya_seb*60
fout_ido = fout_ut/fout_seb*60
lakott_ter_ido = lakott_ter_ut/lakott_ter_seb*60
autopalya_uzemanyag = autopalya_fogy*autopalya_ut/100
fout_uzemanyag = fout_fogy*fout_ut/100
lakott_ter_uzemanyag = lakott_ter_fogy*lakott_ter_ut/100
 
fout_elkerulve = autopalya_ut*0.75+fout_ut
lakott_ter_elkerulve = autopalya_ut*0.25+lakott_ter_ut
fout_elkerulve_ido = fout_elkerulve / fout_seb*60
lakott_ter_elkerulve_ido = lakott_ter_elkerulve/fout_seb*60
fout_elkerulve_uzemanyag = fout_fogy*fout_elkerulve/100
lakott_ter_elkerulve_uzemanyag = lakott_ter_fogy*lakott_ter_elkerulve/100
 
autopalyaval_osszeg = (autopalya_uzemanyag+fout_uzemanyag+lakott_ter_uzemanyag)*benzin+autopalya_matrica
elkerulve_osszeg = (fout_elkerulve_uzemanyag+lakott_ter_elkerulve_uzemanyag)*benzin