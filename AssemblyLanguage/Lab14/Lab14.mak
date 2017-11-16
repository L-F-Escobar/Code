ALL: LAB14.EXE 

CLEAN: 
 -@erase LAB14.EXE 
 -@erase LAB14.ILK 
 -@erase LAB14.PDB 
 -@erase LAB14.OBJ 
 -@erase LAB14.LST 

LAB14.ASM: 

LAB14.OBJ: LAB14.ASM 
 ml /c /coff /Zi LAB14.ASM 

LAB14.EXE: LAB14.OBJ 
 link /debug /subsystem:console /out:LAB14.EXE /entry:start LAB14.OBJ KERNEL32.LIB IO.OBJ