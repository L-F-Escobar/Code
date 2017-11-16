ALL: Assign7.EXE 

CLEAN: 
 -@erase Assign7.EXE 
 -@erase Assign7.ILK 
 -@erase Assign7.PDB 
 -@erase Assign7.OBJ 
 -@erase Assign7.LST 

Assign7.ASM: 

Assign7.OBJ: Assign7.ASM 
 ml /c /coff /Zi Assign7.ASM 

Assign7.EXE: Assign7.OBJ 
 link /debug /subsystem:console /out:Assign7.EXE /entry:start Assign7.OBJ KERNEL32.LIB IO.OBJ