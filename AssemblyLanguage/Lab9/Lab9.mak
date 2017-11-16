ALL: LAB9.EXE 

CLEAN: 
 -@erase LAB9.EXE 
 -@erase LAB9.ILK 
 -@erase LAB9.PDB 
 -@erase LAB9.OBJ 
 -@erase LAB9.LST 

LAB9.ASM: 

LAB9.OBJ: LAB9.ASM 
 ml /c /coff /Zi LAB9.ASM 

LAB9.EXE: LAB9.OBJ 
 link /debug /subsystem:console /out:LAB9.EXE /entry:start LAB9.OBJ KERNEL32.LIB IO.OBJ