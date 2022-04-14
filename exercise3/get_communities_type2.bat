@echo off
echo -----------
.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\model\256_4_4_2_15_18_p.net  .\type2\256_4_4_2_15_18_p
.\radatools\Convert_Lol_To_Clu.exe .\type2\256_4_4_2_15_18_p .\type2\256_4_4_2_15_18_p.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\model\256_4_4_4_13_18_p.net  .\type2\256_4_4_4_13_18_p
.\radatools\Convert_Lol_To_Clu.exe .\type2\256_4_4_4_13_18_p .\type2\256_4_4_4_13_18_p.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\model\rb125.net  .\type2\rb125
.\radatools\Convert_Lol_To_Clu.exe .\type2\rb125 .\type2\rb125.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\real\airports_UW.net  .\type2\airports_UW
.\radatools\Convert_Lol_To_Clu.exe .\type2\airports_UW .\type2\airports_UW.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\real\cat_cortex_sim.net  .\type2\cat_cortex_sim
.\radatools\Convert_Lol_To_Clu.exe .\type2\cat_cortex_sim .\type2\cat_cortex_sim.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\real\dolphins.net  .\type2\dolphins
.\radatools\Convert_Lol_To_Clu.exe .\type2\dolphins .\type2\dolphins.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\real\football.net  .\type2\football
.\radatools\Convert_Lol_To_Clu.exe .\type2\football .\type2\football.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\real\zachary_unwh.net  .\type2\zachary_unwh
.\radatools\Convert_Lol_To_Clu.exe .\type2\zachary_unwh .\type2\zachary_unwh.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\toy\20x2+5x2.net  .\type2\20x2+5x2
.\radatools\Convert_Lol_To_Clu.exe .\type2\20x2+5x2 .\type2\20x2+5x2.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\toy\graph3+1+3.net  .\type2\graph3+1+3
.\radatools\Convert_Lol_To_Clu.exe .\type2\graph3+1+3 .\type2\graph3+1+3.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\toy\graph4+4.net  .\type2\graph4+4
.\radatools\Convert_Lol_To_Clu.exe .\type2\graph4+4 .\type2\graph4+4.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\toy\grid-p-6x6.net  .\type2\grid-p-6x6
.\radatools\Convert_Lol_To_Clu.exe .\type2\grid-p-6x6 .\type2\grid-p-6x6.clu 4

.\radatools\Communities_Detection.exe  v  WN 'r-s-e-ll!rfr-trfr' 3  .\toy\star.net  .\type2\star
.\radatools\Convert_Lol_To_Clu.exe .\type2\star .\type2\star.clu 4

echo -----------
pause
