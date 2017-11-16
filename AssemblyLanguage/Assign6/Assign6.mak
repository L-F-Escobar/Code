ALL: Assign6.EXE 

CLEAN: 
 -@erase Assign6.EXE 
 -@erase Assign6.ILK 
 -@erase Assign6.PDB 
 -@erase Assign6.OBJ 
 -@erase Assign6.LST 

Assign6.ASM: 

Assign6.OBJ: Assign6.ASM 
 ml /c /coff /Zi Assign6.ASM 

Assign6.EXE: Assign6.OBJ 
 link /debug /subsystem:console /out:Assign6.EXE /entry:start Assign6.OBJ KERNEL32.LIB IO.OBJ

