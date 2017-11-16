ALL: LAB5.EXE 

CLEAN: 
 -@erase LAB5.EXE 
 -@erase LAB5.ILK 
 -@erase LAB5.PDB 
 -@erase LAB5.OBJ 
 -@erase LAB5.LST 

LAB5.ASM: 

LAB5.OBJ: LAB5.ASM 
 ml /c /coff /Zi LAB5.ASM 

LAB5.EXE: LAB5.OBJ 
 link /debug /subsystem:console /out:LAB5.EXE /entry:start LAB5.OBJ KERNEL32.LIB IO.OBJ