ALL: LAB2.EXE 

CLEAN: 
 -@erase LAB2.EXE 
 -@erase LAB2.ILK 
 -@erase LAB2.PDB 
 -@erase LAB2.OBJ 
 -@erase LAB2.LST 

LAB2.ASM: 

LAB2.OBJ: LAB2.ASM 
 ml /c /coff /Zi LAB2.ASM 

LAB2.EXE: LAB2.OBJ 
 link /debug /subsystem:console /out:LAB2.EXE /entry:start LAB2.OBJ KERNEL32.LIB IO.OBJ
 







