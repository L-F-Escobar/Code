ALL: LAB1.EXE 

CLEAN: 
 -@erase LAB1.EXE 
 -@erase LAB1.ILK 
 -@erase LAB1.PDB 
 -@erase LAB1.OBJ 
 -@erase LAB1.LST 

LAB1.ASM: 

LAB1.OBJ: LAB1.ASM 
 ml /c /coff /Zi LAB1.ASM 

LAB1.EXE: LAB1.OBJ 
 link /debug /subsystem:console /out:LAB1.EXE /entry:start LAB1.OBJ KERNEL32.LIB IO.OBJ