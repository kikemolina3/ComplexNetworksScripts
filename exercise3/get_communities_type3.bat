@echo off
echo -----------
.\radatools\Communities_Detection.exe  v  WN l 1  .\model\256_4_4_2_15_18_p.net  .\type3\256_4_4_2_15_18_p
.\radatools\Convert_Lol_To_Clu.exe .\type3\256_4_4_2_15_18_p .\type3\256_4_4_2_15_18_p.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\model\256_4_4_4_13_18_p.net  .\type3\256_4_4_4_13_18_p
.\radatools\Convert_Lol_To_Clu.exe .\type3\256_4_4_4_13_18_p .\type3\256_4_4_4_13_18_p.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\model\rb125.net  .\type3\rb125
.\radatools\Convert_Lol_To_Clu.exe .\type3\rb125 .\type3\rb125.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\real\airports_UW.net  .\type3\airports_UW
.\radatools\Convert_Lol_To_Clu.exe .\type3\airports_UW .\type3\airports_UW.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\real\cat_cortex_sim.net  .\type3\cat_cortex_sim
.\radatools\Convert_Lol_To_Clu.exe .\type3\cat_cortex_sim .\type3\cat_cortex_sim.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\real\dolphins.net  .\type3\dolphins
.\radatools\Convert_Lol_To_Clu.exe .\type3\dolphins .\type3\dolphins.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\real\football.net  .\type3\football
.\radatools\Convert_Lol_To_Clu.exe .\type3\football .\type3\football.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\real\zachary_unwh.net  .\type3\zachary_unwh
.\radatools\Convert_Lol_To_Clu.exe .\type3\zachary_unwh .\type3\zachary_unwh.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\toy\20x2+5x2.net  .\type3\20x2+5x2
.\radatools\Convert_Lol_To_Clu.exe .\type3\20x2+5x2 .\type3\20x2+5x2.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\toy\graph3+1+3.net  .\type3\graph3+1+3
.\radatools\Convert_Lol_To_Clu.exe .\type3\graph3+1+3 .\type3\graph3+1+3.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\toy\graph4+4.net  .\type3\graph4+4
.\radatools\Convert_Lol_To_Clu.exe .\type3\graph4+4 .\type3\graph4+4.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\toy\grid-p-6x6.net  .\type3\grid-p-6x6
.\radatools\Convert_Lol_To_Clu.exe .\type3\grid-p-6x6 .\type3\grid-p-6x6.clu 4

.\radatools\Communities_Detection.exe  v  WN l 1  .\toy\star.net  .\type3\star
.\radatools\Convert_Lol_To_Clu.exe .\type3\star .\type3\star.clu 4

echo -----------
pause
