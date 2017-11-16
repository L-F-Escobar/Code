ALL: LAB11.EXE 

CLEAN: 
 -@erase LAB11.EXE 
 -@erase LAB11.ILK 
 -@erase LAB11.PDB 
 -@erase LAB11.OBJ 
 -@erase LAB11.LST 

LAB11.ASM: 

LAB11.OBJ: LAB11.ASM 
 ml /c /coff /Zi LAB11.ASM 

LAB11.EXE: LAB11.OBJ 
 link /debug /subsystem:console /out:LAB11.EXE /entry:start LAB11.OBJ KERNEL32.LIB IO.OBJ