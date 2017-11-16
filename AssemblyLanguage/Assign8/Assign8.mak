ALL: Assign8.EXE 

CLEAN: 
 -@erase Assign8.EXE 
 -@erase Assign8.ILK 
 -@erase Assign8.PDB 
 -@erase Assign8.OBJ 
 -@erase Assign8.LST 

Assign8.ASM: 

Assign8.OBJ: Assign8.ASM 
 ml /c /coff /Zi Assign8.ASM 

Assign8.EXE: Assign8.OBJ 
 link /debug /subsystem:console /out:Assign8.EXE /entry:start Assign8.OBJ KERNEL32.LIB IO.OBJ