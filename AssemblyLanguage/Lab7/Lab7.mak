ALL: LAB7.EXE 

CLEAN: 
 -@erase LAB7.EXE 
 -@erase LAB7.ILK 
 -@erase LAB7.PDB 
 -@erase LAB7.OBJ 
 -@erase LAB7.LST 

LAB7.ASM: 

LAB7.OBJ: LAB7.ASM 
 ml /c /coff /Zi LAB7.ASM 

LAB7.EXE: LAB7.OBJ 
 link /debug /subsystem:console /out:LAB7.EXE /entry:start LAB7.OBJ KERNEL32.LIB IO.OBJ